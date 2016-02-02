#!/usr/bin/env python
"""__main__.py: Main execution program"""
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from MainWindow import Ui_MainWindow
from about import Ui_About
from PyQt5 import QtCore, uic
import sys
from SettingsHandler import SettingsDialog

__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"
__version__ = "0.1"

class Qyoutube_dl(QMainWindow):
    def __init__(self):
        super(Qyoutube_dl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAbout.triggered.connect(self.on_actionAbout_clicked)
        self.ui.actionSettings.triggered.connect(self.on_actionSettings_clicked)

    def on_actionAbout_clicked(self):
        dialog = QDialog()
        dialog.ui = Ui_About()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    def on_actionSettings_clicked(self):
        dialog = SettingsDialog()
        dialog.__init__()
        dialog.exec_()


def compile_ui():
    uic.compileUi(open("about.ui"), open("about.py",'w'))
    uic.compileUi(open("Qyoutube-dl_main.ui"), open("MainWindow.py", 'w'))
    uic.compileUi(open("settings.ui"), open("SettingsWindow.py", 'w'))
# Main entry point
if __name__ == "__main__":
    #compile_ui()
    app = QApplication(sys.argv)
    prgm = Qyoutube_dl()
    prgm.__init__()
    prgm.show()
    sys.exit(app.exec_())
