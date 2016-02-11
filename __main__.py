#!/usr/bin/env python
"""__main__.py: Main execution program"""
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QTableWidgetItem

import youtube_dl
import youtube_dl.version
from Compiled_UI.MainWindow import Ui_MainWindow
from Compiled_UI.about import Ui_About
from Controllers.SettingsController import SettingsDialog

__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"
__version__ = "0.1"


class Qyoutube_dl(QMainWindow):
    string_buffer = ""
    video_downloader = youtube_dl.YoutubeDL()

    def __init__(self):
        super(Qyoutube_dl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        sys.stdout = self.string_buffer
        self.ui.consoleOutput.appendPlainText("Software version: " + __version__ + '\n')
        self.ui.consoleOutput.appendPlainText("Youtube-dl version: " + youtube_dl.version.__version__ + '\n')

    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        dialog = QDialog()
        dialog.ui = Ui_About()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    @QtCore.pyqtSlot()
    def on_actionSettings_triggered(self):
        dialog = SettingsDialog()
        dialog.__init__()
        dialog.exec_()

    @QtCore.pyqtSlot()
    def on_pushButton_pressed(self):
        url = self.ui.lineEdit.text()
        next_row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(next_row)
        # Fill the row
        self.ui.tableWidget.setItem(next_row, 0, QTableWidgetItem(url))  # Add URL
        self.ui.lineEdit.setText('')

    def on_pushButton_2_pressed(self):
        argv = []
        settings_reader = open("settings.txt", 'r')
        while True:
            line = settings_reader.readline()
            if line is "":
                break
            elif "QUIET_MODE" in line:
                argv.append('quiet')
            elif "VERBOSE_MODE" in line and not self.ui.quietCheckBox.isChecked():
                argv.append('verbose')
            elif "NO_WARNINGS" in line and not self.ui.quietCheckBox.isChecked():
                argv.append('no_warnings')
            elif "IGNORE_ERRORS" in line and not self.ui.quietCheckBox.isChecked():
                argv.append('ignoreerrors')
            elif "PREVENT_FILE_OVERWRITE" in line:
                argv.append('nooverwrites')
            elif "FORCE_PRINT_URL" in line:
                argv.append('forceurl')
            elif "FORCE_PRINT_TITLE" in line:
                argv.append('forcetitle')
            elif "FORCE_PRINT_ID" in line:
                argv.append('forceid')
            elif "FORCE_PRINT_THUMBNAIL" in line:
                argv.append('forcethumbnail')
            elif "FORCE_PRINT_DESCRIPTION" in line:
                argv.append('forcedescription')
            elif "FORCE_PRINT_FINAL_FILENAME" in line:
                argv.append('forcefilename')
            elif "FORCE_PRINT_DURATION" in line:
                argv.append('forcedescription')
            elif "FORCE_PRINT_JSON" in line:
                argv.append('forcejson')
            elif "AGE_LIMIT:" in line:
                argv.append('age_limit ' + line.split(':')[1])
            elif "MIN_VIEWS:" in line:
                argv.append('min_views ' + line.split(':')[1])
            elif "MAX_VIEWS:" in line:
                argv.append('max_views ' + line.split(':')[1])
            elif "FILE_PATH:" in line:
                foo = "bar"


# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    prgm = Qyoutube_dl()
    prgm.__init__()
    prgm.show()
    sys.exit(app.exec_())
