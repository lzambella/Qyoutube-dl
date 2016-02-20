#!/usr/bin/env python
"""__main__.py: Main execution program"""
import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt5.QtCore import pyqtSlot, Qt
from Compiled_UI.MainWindow import Ui_MainWindow
from Compiled_UI.about import Ui_About
from Controllers.SettingsController import SettingsDialog
from youtube_dl import version
import subprocess

__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"
__version__ = "0.2"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_actionAbout_triggered(self):
        dialog = QDialog()
        dialog.ui = Ui_About()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(Qt.WA_DeleteOnClose)
        dialog.exec_()

    @pyqtSlot()
    def on_actionSettings_triggered(self):
        dialog = SettingsDialog()
        dialog.__init__()
        dialog.exec_()

    @pyqtSlot()
    def on_pushButton_pressed(self):
        url = self.ui.lineEdit.text()
        # Fill the row
        if len(url) > 10:
            self.ui.url_list.addItem(url)
        self.ui.lineEdit.setText('')

    @pyqtSlot()
    def on_pushButton_2_pressed(self):
        argv = []
        for x in range(0, self.ui.url_list.count()):
            argv.append(self.ui.url_list.itemAt(x))
        try:
            subprocess.Popen(['python', 'youtube_dl/__main__.py'] + argv, shell=True)
        except Exception as e:
            print(e)
        self.ui.url_list.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = MainWindow()
    program.show()
    print("Software version: " + __version__)
    print("Youtube_dl version: " + version.__version__)
    sys.exit(app.exec_())