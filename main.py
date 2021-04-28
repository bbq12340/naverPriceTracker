import logging
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QMessageBox, QDialog
from PySide2.QtCore import QThread, QFile, QDir

from ui_mainwindow import Ui_MainWindow
from myDialog import Ui_MyDialog
from logger import logger
from worker import Worker


class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = parent
        # self.widget = QPlainTextEdit(parent)
        # self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class KeywordDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MyDialog()
        self.ui.setupUi(self)
        self.text_init()
        self.ui.ok_button.clicked.connect(self.handle_ok)
        self.ui.cancel_button.clicked.connect(self.handle_cancel)

    def text_init(self):
        with open('logs/keywords.txt', 'r', encoding='utf-8-sig') as f:
            keywords = f.read()
        self.ui.input_text_edit.setText(keywords)

    def handle_ok(self):
        with open('logs/keywords.txt', 'w', encoding='utf-8-sig') as f:
            f.write(self.ui.input_text_edit.toPlainText())
        self.accept()

    def handle_cancel(self):
        self.reject()


class TargetDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MyDialog()
        self.ui.setupUi(self)
        self.text_init()
        self.ui.ok_button.clicked.connect(self.handle_ok)
        self.ui.cancel_button.clicked.connect(self.handle_cancel)

    def text_init(self):
        with open('logs/targets.txt', 'r', encoding='utf-8-sig') as f:
            targets = f.read()
        self.ui.input_text_edit.setText(targets)

    def handle_ok(self):
        with open('logs/targets.txt', 'w', encoding='utf-8-sig') as f:
            f.write(self.ui.input_text_edit.toPlainText())
        self.accept()

    def handle_cancel(self):
        self.reject()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        logTextBox = QTextEditLogger(self.ui.log_plain_text_edit)
        logTextBox.setFormatter(logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(logTextBox)
        self.ui.target_button.clicked.connect(self.handle_target_input)
        self.ui.keyword_button.clicked.connect(self.handle_keyword_input)
        self.ui.start_button.clicked.connect(self.handle_start)
        self.ui.exit_button.clicked.connect(self.handle_exit)

    def handle_target_input(self):
        inputDlg = TargetDialog()
        inputDlg.exec_()

    def handle_keyword_input(self):
        inputDlg = KeywordDialog()
        inputDlg.exec_()

    def handle_exit(self):
        self.worker.finished.emit()

    # def handle_start(self):
    #     self.thread = QThread()
    #     self.worker = Worker(self.query_list, self.ui.delaySpinBox.text())
    #     self.worker.moveToThread(self.thread)
    #     self.thread.started.connect(self.worker.run)
    #     self.worker.finished.connect(self.thread.quit)
    #     self.worker.finished.connect(self.worker.deleteLater)
    #     self.thread.finished.connect(self.thread.deleteLater)
    #     self.worker.progress.connect(self.ui.progressBar.setValue)
    #     self.thread.start()
    #     self.ui.buttonFrame.setEnabled(False)
    #     self.ui.inputFrame.setEnabled(False)
    #     self.thread.finished.connect(self.handle_finished)

    def handle_start(self):
        self.pages = self.ui.page_spin_box.text()
        self.intervals = self.ui.time_interval_spin_box.text()
        with open('logs/targets.txt', 'r', encoding='utf-8-sig') as f:
            self.targets = f.read().split(',')
        with open('logs/keywords.txt', 'r', encoding='utf-8-sig') as f:
            self.keywords = f.read().split(',')
        self.ui.target_button.setEnabled(False)
        self.ui.keyword_button.setEnabled(False)
        self.ui.page_spin_box.setEnabled(False)
        self.ui.time_interval_spin_box.setEnabled(False)
        self.thread = QThread()
        self.worker = Worker(self.targets, self.keywords,
                             self.pages, self.intervals)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.rest.connect(self.handle_rest)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        self.thread.finished.connect(self.handle_finished)

    def handle_finished(self):
        logger.info("프로그램을 중지하였습니다. 다시 시작해주세요.")
        self.ui.target_button.setEnabled(True)
        self.ui.keyword_button.setEnabled(True)
        self.ui.page_spin_box.setEnabled(True)
        self.ui.time_interval_spin_box.setEnabled(True)

    def handle_rest(self):
        with open('logs/result.txt', 'r', encoding='utf-8-sig') as f:
            links_txt = f.read()
        print(links_txt)
        self.ui.link_plain_text_edit.setPlainText(links_txt)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
