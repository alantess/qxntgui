#!/usr/bin/env python3

import os
import sys
from datetime import datetime

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from app.ui_display import MainDisplay


def main():
    app = QApplication(sys.argv)
    window = MainDisplay()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
