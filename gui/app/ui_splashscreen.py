# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreentPcuKt.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(640, 451)
        icon = QIcon()
        icon.addFile(u"../etc/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setStyleSheet(
            u"QFrame {\n"
            "	background-color: rgb(21, 34, 56);\n"
            "	color: rgb(189, 158, 217);\n"
            "border-radius:10px;\n"
            "\n"
            "}"
        )
        self.DropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.DropShadowFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(80, 0, 480, 231))
        self.logo.setMaximumSize(QSize(480, 720))
        font = QFont()
        font.setFamily(u"Kinnari")
        font.setPointSize(41)
        font.setBold(True)
        font.setItalic(True)
        self.logo.setFont(font)
        self.logo.setPixmap(QPixmap(u"../etc/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.DropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 240, 551, 23))
        self.progressBar.setStyleSheet(
            u"QProgressBar{\n"
            "\n"
            '	font: oblique 11pt "Kinnari";\n'
            "	color: rgb(15, 30, 56);\n"
            "	border-radius:10px;\n"
            "	border-style:none;\n"
            "text-align:center;\n"
            "}\n"
            "\n"
            "\n"
            "QProgressBar::chunk{\n"
            "	background-color: rgb(56, 26, 42);\n"
            "border-radius:10px;\n"
            "	\n"
            "\n"
            "}"
        )
        self.progressBar.setValue(24)
        self.loader_text = QLabel(self.DropShadowFrame)
        self.loader_text.setObjectName(u"loader_text")
        self.loader_text.setGeometry(QRect(10, 310, 601, 31))
        font1 = QFont()
        font1.setFamily(u"Kinnari")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(True)
        self.loader_text.setFont(font1)
        self.loader_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.loader_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.DropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SplashScreen)
        self.statusbar.setObjectName(u"statusbar")
        SplashScreen.setStatusBar(self.statusbar)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(
            QCoreApplication.translate("SplashScreen", u"Vigilant Driving", None)
        )
        self.logo.setText("")
        self.loader_text.setText(
            QCoreApplication.translate("SplashScreen", u"Loading...", None)
        )

    # retranslateUi
