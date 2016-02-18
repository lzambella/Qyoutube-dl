#!/usr/bin/env python
"""__main__.py: Main execution program"""
import sys
import youtube_dl
import youtube_dl.version
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QTableWidgetItem
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QObject, pyqtSignal, QThread, pyqtSlot, Qt
from queue import Queue
from Compiled_UI.MainWindow import Ui_MainWindow
from Compiled_UI.about import Ui_About
from Controllers.SettingsController import SettingsDialog

__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"
__version__ = "0.2"


class WriteStream(object):
    def __init__(self, queue):
        self.queue = queue

    def write(self, text):
        self.queue.put(text)


class StreamReceiver(QObject):
    signal = pyqtSignal(str)

    def __init__(self, queue, *args, **kwargs):
        QObject.__init__(self, *args, **kwargs)
        self.queue = queue

    @pyqtSlot()
    def run(self):
        while True:
            text = self.queue.get()
            self.signal.emit(text)


class ConsoleWriter(QObject):
    @pyqtSlot()
    def run(self, argv):
            video_downloader = youtube_dl
            video_downloader.main(argv)


class Qyoutube_dl(QMainWindow):
    video_downloader = youtube_dl.YoutubeDL()

    def __init__(self):
        super(Qyoutube_dl, self).__init__()
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
        self.ui.tableWidget.insertRow(next_row)
        # Fill the row
        self.ui.tableWidget.setItem(next_row, 0, QTableWidgetItem(url))  # Add URL
        self.ui.lineEdit.setText('')

    @pyqtSlot()
    def start_thread(self, argv):
        q_thread = QThread()
        console_writer = ConsoleWriter()
        console_writer.moveToThread(q_thread)
        q_thread.started.connect(console_writer.run(argv))
        q_thread.start()

    @pyqtSlot(str)
    def append_text(self, text):
        self.ui.plainTextEdit.moveCursor(QTextCursor.End)
        self.ui.plainTextEdit.insertPlainText(text)

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
                    argv.append('-quiet')
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
            self.start_thread(argv)
        except:  # youtube-dl always has some sort of exception
            pass
        self.ui.tableWidget.clear()  # Remove all the videos from the list
        self.ui.tableWidget.clearContents()

# Main entry point
if __name__ == "__main__":
    queue = Queue()
    # Redirect stderr and sdtout to the programs built in console
    sys.stdout = WriteStream(queue)
    sys.stderr = WriteStream(queue)
    app = QApplication(sys.argv)
    program = Qyoutube_dl()
    program.show()
    # Start a thread that reads for console output
    thread = QThread()
    my_receiver = StreamReceiver(queue)
    my_receiver.signal.connect(program.append_text)
    my_receiver.moveToThread(thread)
    thread.started.connect(my_receiver.run)
    thread.start()
    print("Software version: " + __version__)
    app.exec_()
