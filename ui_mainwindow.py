# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(756, 488)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_frame = QFrame(self.left_frame)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(194, 192, 196);\n"
"	border-radius: 15px;\n"
"}")
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)
        self.target_button = QPushButton(self.input_frame)
        self.target_button.setObjectName(u"target_button")
        self.target_button.setGeometry(QRect(20, 40, 113, 32))
        self.keyword_button = QPushButton(self.input_frame)
        self.keyword_button.setObjectName(u"keyword_button")
        self.keyword_button.setGeometry(QRect(20, 80, 113, 32))
        self.start_button = QPushButton(self.input_frame)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(20, 160, 113, 32))
        self.exit_button = QPushButton(self.input_frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(190, 160, 113, 32))
        self.page_spin_box = QSpinBox(self.input_frame)
        self.page_spin_box.setObjectName(u"page_spin_box")
        self.page_spin_box.setGeometry(QRect(260, 40, 48, 24))
        self.page_spin_box.setMinimum(1)
        self.page_spin_box.setMaximum(5)
        self.page_spin_box.setDisplayIntegerBase(10)
        self.page_label = QLabel(self.input_frame)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setGeometry(QRect(180, 40, 60, 20))
        self.page_label.setAlignment(Qt.AlignCenter)
        self.time_interval_label_2 = QLabel(self.input_frame)
        self.time_interval_label_2.setObjectName(u"time_interval_label_2")
        self.time_interval_label_2.setGeometry(QRect(170, 80, 68, 20))
        self.time_interval_label_2.setAlignment(Qt.AlignCenter)
        self.time_interval_spin_box = QSpinBox(self.input_frame)
        self.time_interval_spin_box.setObjectName(u"time_interval_spin_box")
        self.time_interval_spin_box.setGeometry(QRect(260, 80, 48, 24))
        self.time_interval_spin_box.setMinimum(2)
        self.time_interval_spin_box.setMaximum(8)
        self.time_interval_spin_box.setSingleStep(2)
        self.time_interval_spin_box.setDisplayIntegerBase(10)

        self.verticalLayout.addWidget(self.input_frame)

        self.log_frame = QFrame(self.left_frame)
        self.log_frame.setObjectName(u"log_frame")
        self.log_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(194, 192, 196);\n"
"	border-radius: 15px;\n"
"}")
        self.log_frame.setFrameShape(QFrame.StyledPanel)
        self.log_frame.setFrameShadow(QFrame.Raised)
        self.log_label = QLabel(self.log_frame)
        self.log_label.setObjectName(u"log_label")
        self.log_label.setGeometry(QRect(140, 10, 60, 16))
        self.log_label.setAlignment(Qt.AlignCenter)
        self.log_plain_text_edit = QPlainTextEdit(self.log_frame)
        self.log_plain_text_edit.setObjectName(u"log_plain_text_edit")
        self.log_plain_text_edit.setGeometry(QRect(10, 30, 311, 171))
        self.log_plain_text_edit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: white;\n"
"}")
        self.log_plain_text_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.log_frame)


        self.horizontalLayout.addWidget(self.left_frame)

        self.link_frame = QFrame(self.centralwidget)
        self.link_frame.setObjectName(u"link_frame")
        self.link_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(194, 192, 196);\n"
"	border-radius: 15px;\n"
"}")
        self.link_frame.setFrameShape(QFrame.StyledPanel)
        self.link_frame.setFrameShadow(QFrame.Raised)
        self.link_plain_text_edit = QPlainTextEdit(self.link_frame)
        self.link_plain_text_edit.setObjectName(u"link_plain_text_edit")
        self.link_plain_text_edit.setGeometry(QRect(13, 37, 331, 411))
        self.link_plain_text_edit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: white;\n"
"}")
        self.link_plain_text_edit.setReadOnly(True)
        self.link_label = QLabel(self.link_frame)
        self.link_label.setObjectName(u"link_label")
        self.link_label.setGeometry(QRect(160, 13, 60, 16))
        self.link_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.link_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ub124\uc774\ubc84 \uac00\uaca9 \ud2b8\ub798\ucee4", None))
        self.target_button.setText(QCoreApplication.translate("MainWindow", u"\uc2a4\ud1a0\uc5b4\uba85", None))
        self.keyword_button.setText(QCoreApplication.translate("MainWindow", u"\ud0a4\uc6cc\ub4dc", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"\uc911\uc9c0", None))
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"\ud398\uc774\uc9c0 \uc218: ", None))
        self.time_interval_label_2.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04 \uac04\uaca9:", None))
        self.log_label.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8", None))
        self.link_label.setText(QCoreApplication.translate("MainWindow", u"\ub9c1\ud06c", None))
    # retranslateUi

