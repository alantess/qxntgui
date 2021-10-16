import sys
import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from app.ui_splashscreen import Ui_SplashScreen
from app.ui_qxnt import Ui_QxntGui

counter = 0


class QuantWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_QxntGui()
        self.ui.setupUi(self)


class MainDisplay(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.splash_screen = Ui_SplashScreen()
        self.splash_screen.setupUi(self)
        self.ui = QuantWindow()
        ## DROP SHADOW EFFECT
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.splash_screen.DropShadowFrame.setGraphicsEffect(self.shadow)
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(10)
        qr = self.frameGeometry()
        center = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(center)
        self.move(qr.topLeft())
        self.show()

    def progress(self):
        global counter
        # SET VALUE TO PROGRESS BAR
        self.splash_screen.progressBar.setValue(counter)
        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            # CLOSE SPLASH SCREEN
            self.close()
            self.ui.show()

        # INCREASE COUNTER
        counter += 1
