#!/usr/bin/env python
"""__main__.py: Main execution program"""
import sys
import youtube_dl
import youtube_dl.version
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QTableWidgetItem
from PyQt5.QtGui import QTextCursor, QColor
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
from Compiled_UI.MainWindow import Ui_MainWindow
from Compiled_UI.about import Ui_About
from Controllers.SettingsController import SettingsDialog
from youtube_dl import version
import threading
import subprocess

__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"
__version__ = "0.2"


class OutLog:
    def __init__(self, edit, out=None, color=None):
        """(edit, out=None, color=None) -> can write stdout, stderr to a
        QTextEdit.
        edit = QTextEdit
        out = alternate stream ( can be the original sys.stdout )
        color = alternate color (i.e. color stderr a different color)
        """
        self.edit = edit
        self.out = None
        self.color = color

    def write(self, m):
        # if self.color:
        # tc = self.edit.textColor()
        # self.edit.setTextColor(self.color)

        self.edit.moveCursor(QTextCursor.End)
        self.edit.insertPlainText(m)

        # if self.color:
        # self.edit.setTextColor(tc)

        if self.out:
            self.out.write(m)

    def flush(self):
        pass

    def fileno(self):
        pass


class WriteStream(object):
    def __init__(self, stream_queue):
        self.queue = stream_queue

    def write(self, text):
        self.queue.put(text)


class StreamReceiver(QObject):
    signal = pyqtSignal(str)

    def __init__(self, stream_queue, *args, **kwargs):
        QObject.__init__(self, *args, **kwargs)
        self.queue = stream_queue

    @pyqtSlot()
    def run(self):
        while True:
            text = self.queue.get()
            self.signal.emit(text)


class ThreadedFunction(threading.Thread):
    def run(self, argv):
        youtube_dl.main(argv)


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
        next_row = self.ui.tableWidget.rowCount()
        # Fill the row
        if len(url) > 10:
            self.ui.tableWidget.insertRow(next_row)
            self.ui.tableWidget.setItem(next_row, 0, QTableWidgetItem(url))  # Add URL
        self.ui.lineEdit.setText('')

    @pyqtSlot()
    def on_pushButton_2_pressed(self):
        argv = []
        try:
            settings_reader = open("settings.txt", 'r')
            quiet_check = False
            while True:
                line = settings_reader.readline()
                if line is "":
                    break
                elif "QUIET_MODE" in line:
                    argv.append('--quiet')
                    quiet_check = True
                elif "VERBOSE_MODE" in line and not quiet_check:
                    argv.append('--verbose')
                elif "NO_WARNINGS" in line and not quiet_check:
                    argv.append('--no-warnings')
                elif "IGNORE_ERRORS" in line and not quiet_check:
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
            subprocess.Popen(['python', 'youtube_dl/__main__.py'] + argv, shell=True)
        except Exception as e:  # youtube-dl always has some sort of exception
            print(e)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(0)


def download_thread(argv):
    youtube_dl.main(argv)


def gui_thread():
    app = QApplication(sys.argv)
    program = MainWindow()
    program.show()
    print("Software version: " + __version__)
    print("Youtube_dl version: " + version.__version__)
    sys.exit(app.exec_())

# Main entry point
if __name__ == "__main__":
    main_thread = threading.Thread()
    main_thread.daemon = True
    main_thread.setDaemon(gui_thread())
    main_thread.start()
