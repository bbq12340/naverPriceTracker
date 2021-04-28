# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MyDialog(object):
    def setupUi(self, MyDialog):
        if not MyDialog.objectName():
            MyDialog.setObjectName(u"MyDialog")
        MyDialog.resize(480, 123)
        self.input_text_edit = QTextEdit(MyDialog)
        self.input_text_edit.setObjectName(u"input_text_edit")
        self.input_text_edit.setGeometry(QRect(20, 20, 361, 78))
        self.ok_button = QPushButton(MyDialog)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(380, 30, 91, 31))
        self.cancel_button = QPushButton(MyDialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(380, 60, 91, 31))

        self.retranslateUi(MyDialog)

        QMetaObject.connectSlotsByName(MyDialog)
    # setupUi

    def retranslateUi(self, MyDialog):
        MyDialog.setWindowTitle(QCoreApplication.translate("MyDialog", u"Dialog", None))
        self.ok_button.setText(QCoreApplication.translate("MyDialog", u"Ok", None))
        self.cancel_button.setText(QCoreApplication.translate("MyDialog", u"Cancel", None))
    # retranslateUi

