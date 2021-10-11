# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowuYwTUQ.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_QxntGui(object):
    def setupUi(self, QxntGui):
        if not QxntGui.objectName():
            QxntGui.setObjectName(u"QxntGui")
        QxntGui.resize(962, 673)
        self.centralwidget = QWidget(QxntGui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.data = QListView(self.centralwidget)
        self.data.setObjectName(u"data")

        self.gridLayout.addWidget(self.data, 4, 0, 1, 1)

        self.open_orders = QListView(self.centralwidget)
        self.open_orders.setObjectName(u"open_orders")

        self.gridLayout.addWidget(self.open_orders, 0, 0, 1, 1)

        self.history = QListView(self.centralwidget)
        self.history.setObjectName(u"history")

        self.gridLayout.addWidget(self.history, 4, 2, 1, 1)

        self.stock_img = QLabel(self.centralwidget)
        self.stock_img.setObjectName(u"stock_img")
        self.stock_img.setMaximumSize(QSize(700, 350))
        self.stock_img.setPixmap(QPixmap(u"../../Pictures/shutterstock_775889491.jpg"))

        self.gridLayout.addWidget(self.stock_img, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        QxntGui.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(QxntGui)
        self.statusbar.setObjectName(u"statusbar")
        QxntGui.setStatusBar(self.statusbar)

        self.retranslateUi(QxntGui)

        QMetaObject.connectSlotsByName(QxntGui)
    # setupUi

    def retranslateUi(self, QxntGui):
        QxntGui.setWindowTitle(QCoreApplication.translate("QxntGui", u"MainWindow", None))
        self.stock_img.setText("")
    # retranslateUi

