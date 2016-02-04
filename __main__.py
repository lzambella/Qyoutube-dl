#!/usr/bin/env python
"""__main__.py: Main execution program"""
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QTableWidgetItem
from MainWindow import Ui_MainWindow
from about import Ui_About
from PyQt5 import QtCore, uic
import sys
import io
from SettingsHandler import SettingsDialog
import youtube_dl
__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"
__version__ = "0.1"


class Qyoutube_dl(QMainWindow):
    api_key = ""

    def __init__(self):
        super(Qyoutube_dl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def on_actionAbout_triggered(self):
        dialog = QDialog()
        dialog.ui = Ui_About()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    def on_actionSettings_triggered(self):
        dialog = SettingsDialog()
        dialog.__init__()
        dialog.exec_()

    def on_pushButton_pressed(self):
        url = self.ui.lineEdit.text()
        key_file = open("key.txt")
        # Check if URL is valid (I know youtube-dl supports different website)
        if key_file.__sizeof__() > 0:
            api_key = key_file.readLine()
        if 'youtube.com' in url and 'watch' in url:
            next_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(next_row)
            # Fill the row
            self.ui.tableWidget.setItem(next_row, 1, QTableWidgetItem(url))  # Add URL
            # If an api key exists
            if len(api_key) > 0:
                # TODO: add api calls
                text = "placeholder"

        else:
            self.ui.consoleOutput.setPlainText("Not a youtube link!")

    def on_pushButton_2_pressed(self):
        # TODO: this shouldn't work
        for video in self.ui.tableWidget.columnAt(1):
            youtube_dl.main(video)

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    prgm = Qyoutube_dl()
    prgm.__init__()
    prgm.show()
    sys.exit(app.exec_())
