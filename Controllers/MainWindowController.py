from PyQt5.QtWidgets import QMainWindow, QDialog, QFileDialog
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
    def on_clear_list_pressed(self):
        self.ui.url_list.clear()

    # Execute the downloader
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

    @pyqtSlot()
    def on_load_batch_file_pressed(self):
            file = QFileDialog.getOpenFileName()
            with open(file[0]) as f:
                lines = f.read().splitlines()
            self.batch_load(lines)

    def check_settings(self):
        # Video selection
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
            print("On date field is filled, skipping before date field.")
        if len(self.ui.date_after.text()) > 0 and not len(self.ui.on_date.text()) > 0:
            self.argv.append("--dateafter")
            self.argv.append(self.ui.date_after.text())
            print("On date field is filled, skipping after date field.")
        # Filesystem options
        if self.ui.video_id_name.isChecked():
            self.argv.append("--id")
        if self.ui.restrict_filename.isChecked():
            self.argv.append("--restrict-filenames")
        if self.ui.no_overwrites.isChecked():
            self.argv.append("--no-overwrites")
        if self.ui.write_info_json.isChecked():
            self.argv.append("--write-info-json")
        if self.ui.write_description.isChecked():
            self.argv.append("--write-description")
        if self.ui.write_annotations.isChecked():
            self.argv.append("--write-annotations")
        # Verbosity
        if self.ui.quiet_mode.isChecked():
            self.argv.append("--quiet")
        if self.ui.verbose_mode.isChecked() and not self.ui.quiet_mode.isChecked():
            self.argv.append("--verbose")
        if self.ui.ignore_warnings.isChecked() and not self.ui.quiet_mode.isChecked():
            self.argv.append("--ignore-warnings")
        if self.ui.ignore_errors.isChecked() and not self.ui.quiet_mode.isChecked():
            self.argv.append("--ignore-errors")
        # Subtitle options
        if self.ui.write_sub.isChecked():
            self.argv.append("--write-sub")
        if self.ui.write_auto_sub.isChecked():
            self.argv.append("--write-auto-sub")
        if self.ui.all_subs.isChecked():
            self.argv.append("--all-subs")
        # Download options
        if len(self.ui.max_download_rate.text()) > 0 and self.is_integer(self.ui.max_download_rate.text()):
            self.argv.append("--rate-limit")
            self.argv.append(self.ui.max_download_rate.text())
        if len(self.ui.num_retries.text()) > 0 and self.is_integer(self.ui.num_retries.text()):
            self.argv.append("--retries")
            self.argv.append(self.ui.num_retries.text())
        if len(self.ui.buffer_size.text()) > 0 and self.is_integer(self.ui.buffer_size.text()):
            self.argv.append("--buffer-size")
            self.argv.append(self.ui.buffer_size.text())

    def batch_load(self, url_list):
        for x in url_list:
            if 'http://' in x or 'https://' in x:
                self.ui.url_list.addItem(x)

    def is_integer(self, value):
        try:
            i = int(value)
            return True
        except ValueError:
            return False
