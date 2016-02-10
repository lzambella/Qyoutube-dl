import base64

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog

from Compiled_UI.SettingsWindow import Ui_SettingDialog

_author__ = 'Luke Zambella'


class SettingsDialog(QDialog):
    string_buffer = ""
    salt_mine = base64.b64decode("zsdfrhjk")

    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.ui = Ui_SettingDialog()
        self.ui.setupUi(self)
        self.load_settings()  # Load saved settings

    @QtCore.pyqtSlot()
    def on_buttonBox_accepted(self):
        file_io = open("settings.txt", 'w')
        if self.ui.quietCheckBox.isChecked():
            self.string_buffer += "QUIET_MODE\n"
        if self.ui.verboseCheckBox.isChecked() and not self.ui.quietCheckBox.isChecked():
            self.string_buffer += "VERBOSE_MODE\n"
        if self.ui.warningsCheckBox.isChecked() and not self.ui.quietCheckBox.isChecked():
            self.string_buffer += "NO_WARNINGS\n"
        if self.ui.ignoreCheckBox.isChecked() and not self.ui.quietCheckBox.isChecked():
            self.string_buffer += "IGNORE_ERRORS\n"
        if self.ui.overwriteCheckBox.isChecked():
            self.string_buffer += "PREVENT_FILE_OVERWRITE\n"
            """
        if len(self.ui.lineEdit.text()) > 0:
            self.string_buffer += "USERNAME:" + self.ui.lineEdit.text() + "\n"
        if len(self.ui.lineEdit_2.text()) > 0:
            buffer = base64.b64encode(self.ui.lineEdit_2.text().encode())
            self.string_buffer += "PASSWORD:" + str(buffer) + "\n"
            """
        if self.ui.forceurl.isChecked():
            self.string_buffer += "FORCE_PRINT_URL\n"
        if self.ui.forcetitle.isChecked():
            self.string_buffer += "FORCE_PRINT_TITLE\n"
        if self.ui.forceid.isChecked():
            self.string_buffer += "FORCE_PRINT_ID\n"
        if self.ui.forcethumbnail.isChecked():
            self.string_buffer += "FORCE_PRINT_THUMBNAIL\n"
        if self.ui.forcedescription.isChecked():
            self.string_buffer += "FORCE_PRINT_DESCRIPTION\n"
        if self.ui.forcefilename.isChecked():
            self.string_buffer += "FORCE_PRINT_FINAL_FILENAME\n"
        if self.ui.forceduration.isChecked():
            self.string_buffer += "FORCE_PRINT_DURATION\n"
        if self.ui.forcejson.isChecked():
            self.string_buffer += "FORCE_PRINT_JSON\n"
        buffer = self.ui.age_limit.text()
        if len(buffer) > 0:
            self.string_buffer += "AGE_LIMIT:" + buffer + "\n"
        buffer = self.ui.min_views.text()
        if len(buffer) > 0:
            self.string_buffer += "MIN_VIEWS:" + buffer + "\n"
        buffer = self.ui.max_views.text()
        if len(buffer) > 0:
            self.string_buffer += "MAX_VIEWS:" + buffer + "\n"
        buffer = self.ui.record_file.text()
        if len(buffer) > 0:
            self.string_buffer += "FILE_PATH::" + buffer + "\n"
        file_io.write(self.string_buffer)
        file_io.close()
        self.close()

    def load_settings(self):
        settings_reader = open("settings.txt", 'r')
        while True:
            line = settings_reader.readline()
            if line is "":
                break
            elif "QUIET_MODE" in line:
                self.ui.quietCheckBox.setChecked(True)
            elif "VERBOSE_MODE" in line and not self.ui.quietCheckBox.isChecked():
                self.ui.verboseCheckBox.setChecked(True)
            elif "NO_WARNINGS" in line and not self.ui.quietCheckBox.isChecked():
                self.ui.warningsCheckBox.setChecked(True)
            elif "IGNORE_ERRORS" in line and not self.ui.quietCheckBox.isChecked():
                self.ui.ignoreCheckBox.setChecked(True)
            elif "PREVENT_FILE_OVERWRITE" in line:
                self.ui.overwriteCheckBox.setChecked(True)
            elif "FORCE_PRINT_URL" in line:
                self.ui.forceurl.setCheckable(True)
            elif "FORCE_PRINT_TITLE" in line:
                self.ui.forcetitle.setChecked(True)
            elif "FORCE_PRINT_ID" in line:
                self.ui.forceid.setChecked(True)
            elif "FORCE_PRINT_THUMBNAIL" in line:
                self.ui.forcethumbnail.setChecked(True)
            elif "FORCE_PRINT_DESCRIPTION" in line:
                self.ui.forcedescription.setChecked(True)
            elif "FORCE_PRINT_FINAL_FILENAME" in line:
                self.ui.forcefilename.setChecked(True)
            elif "FORCE_PRINT_DURATION" in line:
                self.ui.forceduration.setChecked(True)
            elif "FORCE_PRINT_JSON" in line:
                self.ui.forcejson.setChecked(True)
            elif "AGE_LIMIT:" in line:
                self.ui.age_limit.setText(line.split(':')[1])
            elif "MIN_VIEWS:" in line:
                self.ui.min_views.setText(line.split(':')[1])
            elif "MAX_VIEWS:" in line:
                self.ui.max_views.setText(line.split(':')[1])
            elif "FILE_PATH:" in line:
                self.ui.record_file.setText(line.split('::')[1])

    def on_select_record_file_button_pressed(self):
        dialog = QFileDialog()
        dialog.__init__()
        self.ui.record_file.setText((QFileDialog.getExistingDirectory(dialog, "Select Directory")))
