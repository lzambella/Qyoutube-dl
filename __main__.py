#!/usr/bin/env python
"""__main__.py: Main execution program"""
import sys
import os
import threading
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QTableWidgetItem

import youtube_dl
import youtube_dl.version
from Compiled_UI.MainWindow import Ui_MainWindow
from Compiled_UI.about import Ui_About
from Controllers.SettingsController import SettingsDialog
from io import StringIO
__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"
__version__ = "0.1"


class Qyoutube_dl(QMainWindow):
    video_downloader = youtube_dl.YoutubeDL()
    s = StringIO()

    def __init__(self):
        super(Qyoutube_dl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # sys.stdout = self.s

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
        try:
            settings_reader = open("settings.txt", 'r')
            while True:
                line = settings_reader.readline()
                self.quiet_check = False
                if line is "":
                    break
                elif "QUIET_MODE" in line:
                    argv.append('-quiet')
                    self.quiet_check = True
                elif "VERBOSE_MODE" in line and not self.quiet_check:
                    argv.append('--verbose')
                elif "NO_WARNINGS" in line and not self.quiet_check:
                    argv.append('--no-warnings')
                elif "IGNORE_ERRORS" in line and not self.quiet_check:
                    argv.append('--ignore-errors')
                elif "PREVENT_FILE_OVERWRITE" in line:
                    argv.append('--no-overwrites')
                elif "AGE_LIMIT:" in line:
                    argv.append('--age-limit ')
                    argv.append(line.split(':')[1])
                elif "MIN_VIEWS:" in line:
                    argv.append('--min-views ')
                    argv.append(line.split(':')[1])
                elif "MAX_VIEWS:" in line:
                    argv.append('--max-views')
                    argv.append(line.split(':')[1])
                elif "PLAYLIST_START:" in line:
                    argv.append('--playlist-start')
                    argv.append(line.split(':')[1])
                elif "PLAYLIST_END:" in line:
                    argv.append('--playlist-end')
                    argv.append(line.split(':')[1])
                # elif "FILE_PATH:" in line:
                #    argv.append('-o \"' + line.split('::')[1] + '/%(title)s-%(id)s.%(ext)s' + '\"')
        except FileNotFoundError:
            print("No settings file found. Inputting zero arguments.")
        for x in range(0, self.ui.tableWidget.rowCount()):
            argv.append(self.ui.tableWidget.itemAt(0, x).text())
        try:
            thread = threading.Thread(target=youtube_dl.main(argv))
            thread.daemon = True
            thread.start()
        except:
            print('Something happened.')

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    prgm = Qyoutube_dl()
    prgm.__init__()
    prgm.show()
    sys.exit(app.exec_())
