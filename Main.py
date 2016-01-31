#!/usr/bin/env python
"""Main.py: Main execution program"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow
from PyQt5.uic import compileUi
import MainWindow


import os.path
__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"


def setup_ui():
    ui_file = open("Qyoutube-dl_main.ui")
    compileUi(uifile=ui_file, pyfile=open("MainWindow.py", 'w'))

def __main__():
    # Generates a UI every time in case its been changed
    setup_ui()
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

__main__()
