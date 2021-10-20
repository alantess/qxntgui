# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coinbaseqTPmwl.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_CoinbaseAPIDialog(object):
    def setupUi(self, CoinbaseAPIDialog):
        if not CoinbaseAPIDialog.objectName():
            CoinbaseAPIDialog.setObjectName(u"CoinbaseAPIDialog")
        CoinbaseAPIDialog.resize(320, 240)
        CoinbaseAPIDialog.setMinimumSize(QSize(320, 240))
        CoinbaseAPIDialog.setMaximumSize(QSize(320, 240))
        font = QFont()
        font.setFamily(u"Ubuntu Condensed")
        font.setBold(True)
        font.setItalic(True)
        CoinbaseAPIDialog.setFont(font)
        CoinbaseAPIDialog.setStyleSheet(u"border-bottom-color: rgb(19, 56, 18);")
        self.buttonBox = QDialogButtonBox(CoinbaseAPIDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayoutWidget = QWidget(CoinbaseAPIDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 291, 161))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamily(u"Gideon Roman")
        font1.setBold(True)
        font1.setItalic(False)
        self.title.setFont(font1)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.api_key_label = QLabel(self.verticalLayoutWidget)
        self.api_key_label.setObjectName(u"api_key_label")
        font2 = QFont()
        font2.setFamily(u"FreeSerif")
        font2.setBold(True)
        font2.setItalic(False)
        self.api_key_label.setFont(font2)

        self.verticalLayout.addWidget(self.api_key_label)

        self.api_key_input = QLineEdit(self.verticalLayoutWidget)
        self.api_key_input.setObjectName(u"api_key_input")
        self.api_key_input.setStyleSheet(u"QLineEdit{\n"
"border-radius:3px;\n"
"}\n"
"QLineEdit::hover {\n"
"border:2px solid;\n"
"	border-color: rgb(130, 134, 166);\n"
"}\n"
"")
        self.api_key_input.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.api_key_input)

        self.api_key_secret_label = QLabel(self.verticalLayoutWidget)
        self.api_key_secret_label.setObjectName(u"api_key_secret_label")
        self.api_key_secret_label.setFont(font2)

        self.verticalLayout.addWidget(self.api_key_secret_label)

        self.api_secrets_input = QLineEdit(self.verticalLayoutWidget)
        self.api_secrets_input.setObjectName(u"api_secrets_input")
        self.api_secrets_input.setStyleSheet(u"QLineEdit{\n"
"border-radius:3px;\n"
"}\n"
"QLineEdit::hover {\n"
"border:2px solid;\n"
"	border-color: rgb(130, 134, 166);\n"
"}\n"
"")
        self.api_secrets_input.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.api_secrets_input)


        self.retranslateUi(CoinbaseAPIDialog)
        self.buttonBox.accepted.connect(CoinbaseAPIDialog.accept)
        self.buttonBox.rejected.connect(CoinbaseAPIDialog.reject)

        QMetaObject.connectSlotsByName(CoinbaseAPIDialog)
    # setupUi

    def retranslateUi(self, CoinbaseAPIDialog):
        CoinbaseAPIDialog.setWindowTitle(QCoreApplication.translate("CoinbaseAPIDialog", u"Coinbase API", None))
        self.title.setText(QCoreApplication.translate("CoinbaseAPIDialog", u"Connect to Coinbase", None))
        self.api_key_label.setText(QCoreApplication.translate("CoinbaseAPIDialog", u"API Key", None))
        self.api_key_secret_label.setText(QCoreApplication.translate("CoinbaseAPIDialog", u"API Secrets", None))
    # retranslateUi

