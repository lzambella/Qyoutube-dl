from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import pyqtSlot, Qt
from Compiled_UI.MainWindow import Ui_MainWindow
from Compiled_UI.about import Ui_About
import sys
import subprocess


class MainWindow(QMainWindow):
    argv = []

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
    def on_pushButton_pressed(self):
        url = self.ui.lineEdit.text()
        # Fill the row
        if len(url) > 10:
            self.ui.url_list.addItem(url)
        self.ui.lineEdit.setText('')

    @pyqtSlot()
    def on_pushButton_2_pressed(self):
        if self.ui.url_list.count() > 0:
            self.check_settings()
            for x in range(0, self.ui.url_list.count()):
                self.argv.append(self.ui.url_list.item(x).text())
            try:
                subprocess.Popen([sys.executable, 'youtube_dl/__main__.py'] + self.argv, shell=False)
            except Exception as e:
                print(e)
            self.ui.url_list.clear()
        else:
            print("ERROR: No URLs were given.")
        self.argv.clear()

    def check_settings(self):
        if len(self.ui.age_limit.text()) > 0 and self.is_integer(self.ui.age_limit.text()):
            self.argv.append("--age-limit")
            self.argv.append(self.ui.age_limit.text())
        if len(self.ui.min_views.text()) > 0 and self.is_integer(self.ui.min_views.text()):
            self.argv.append("--min-views")
            self.argv.append(self.ui.min_views.text())
        if len(self.ui.max_views.text()) > 0 and self.is_integer((self.ui.max_views.text())):
            self.argv.append("--max-views")
            self.argv.append(self.ui.max_views.text())
        if len(self.ui.min_file_size.text()) > 0 and self.is_integer(self.ui.min_file_size.text()):
            self.argv.append("--min-filesize")
            self.argv.append(self.ui.min_file_size.text())
        if len(self.ui.max_file_size.text()) > 0 and self.is_integer(self.ui.max_file_size.text()):
            self.argv.append("--max_filesize")
            self.argv.append(self.ui.max_file_size.text())
        if len(self.ui.playlist_start.text()) > 0 and self.is_integer(self.ui.playlist_start.text()):
            self.argv.append("--playlist-start")
            self.argv.append(self.ui.playlist_start.text())
        if len(self.ui.playlist_end.text()) > 0 and self.is_integer(self.ui.playlist_end.text()):
            self.argv.append("--playlist-end")
            self.argv.append(self.ui.playlist_start.text())
        if len(self.ui.playlist_list.text()) > 0:
            self.argv.append("--playlist-items")
            self.argv.append(self.ui.playlist_list.text())
        if len(self.ui.on_date.text()) > 0:
            self.argv.append("--date")
            self.argv.append(self.ui.on_date.text())
        if len(self.ui.date_before.text()) > 0 and not len(self.ui.on_date.text()) > 0:
            self.argv.append("--datebefore")
            self.argv.append(self.ui.date_before.text())
        if len(self.ui.date_after.text()) > 0 and not len(self.ui.on_date.text()) > 0:
            self.argv.append("--dateafter")
            self.argv.append(self.ui.date_after.text())
        if len(self.ui.filter.text()) > 0:
            self.argv.append("--match-filter")
            self.argv.append(self.ui.filter.text())

    def is_integer(self, value):
        try:
            i = int(value)
            return True
        except ValueError:
            return False
