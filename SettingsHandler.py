from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog, QDirModel
from SettingsWindow import Ui_SettingDialog
import hashlib
import base64
_author__ = 'Luke Zambella'


class SettingsDialog(QDialog):
    string_buffer = ""
    salt_mine = base64.b64decode("zsdfrhjk")

    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.ui = Ui_SettingDialog()
        self.ui.setupUi(self)
        self.loadSettings()  # Load saved settings

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
            self.string_buffer += "IGNORE_WARNINGS\n"
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
            self.stringBuffer += "FORCE_PRINT_JSON\n"

        buffer = self.ui.age_limit.text()
        try:
            if len(buffer) > 0:
                self.string_buffer += "AGE_LIMIT:" + buffer + "\n"
        except:
            print("age_limit type not int")
        buffer = self.ui.min_views.text()
        try:
            if len(buffer) > 0:
                self.string_buffer += "MIN_VIEWS:" + buffer + "\n"
        except:
            print("min_views type not int")
        buffer = self.ui.max_views.text()
        try:
            if len(buffer) > 0:
                self.string_buffer += "MAX_VIEWS:" + buffer + "\n"
        except:
            print("max_views type not int")
        buffer = self.ui.record_file.text()
        if len(buffer) > 0:
            self.string_buffer += "FILE_PATH:" + buffer + "\n"
        file_io.write(self.string_buffer)
        file_io.close()
        self.close()

    def loadSettings(self):
        settings_reader = open("settings.txt", 'r')
        while True:
            line = settings_reader.readline()
            if line == "":
                break
            if line == "QUIET_MODE":
                self.ui.quietCheckBox.setChecked(True)
            if line == "VERBOSE_MODE" and not self.ui.quietCheckBox.isChecked():
                self.ui.verboseCheckBox.setChecked(True)
            if line == "NO_WARNINGS" and not self.ui.quietCheckBox.isChecked():
                self.ui.warningsCheckBox.setChecked(True)
            if line == "IGNORE_WARNINGS" and not self.ui.quietCheckBox.isChecked():
                self.ui.ignoreCheckBox.setChecked(True)
            



    def on_select_record_file_button_pressed(self):
        dialog = QFileDialog()
        dialog.__init__()
        self.ui.record_file.setText((QFileDialog.getExistingDirectory(dialog, "Select Directory")))
'''
    def on_selectDirButton_pressed(self):
        file_dialog = QDirModel
        file_dialog.__init__()
        QFileDialog.getExistingDirectory()
'''