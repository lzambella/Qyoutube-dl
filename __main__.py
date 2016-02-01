#!/usr/bin/env python
"""__main__.py: Main execution program"""
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from MainWindow import Ui_MainWindow
from about import Ui_About
from PyQt5 import QtCore
import sys

__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"


class Qyoutube_dl(QMainWindow):
    def __init__(self):
        super(Qyoutube_dl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAbout.triggered.connect(self.on_actionAbout_clicked)

    def on_actionAbout_clicked(self):
        dialog = QDialog()
        dialog.ui = Ui_About()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    prgm = Qyoutube_dl()
    prgm.__init__()
    prgm.show()
    sys.exit(app.exec_())
