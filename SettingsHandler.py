from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog, QDirModel
from SettingsWindow import Ui_SettingDialog
import hashlib
import base64
_author__ = 'Luke Zambella'


class SettingsDialog(QDialog):
    string_buffer = ""
    salt_mine = base64.b64decode("CxFghrnJf4957Ngj568fLkIHJpg(i4,Kamgoaio")
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.ui = Ui_SettingDialog()
        self.ui.setupUi(self)
        self.file_io = open("settings.txt", 'w')

    # confirm settings
    def on_okButton_pressed(self):
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
        if len(self.ui.lineEdit.text()) > 0:
            self.string_buffer += "USERNAME:" + self.ui.lineEdit.text() + "\n"
        if len(self.ui.lineEdit_2.text()) > 0:
            self.string_buffer += "PASSWORD:" + base64.b64encode(self.ui.lineEdit_2.text()) + self.salt_mine + "\n"
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
        try:
            if len(self.ui.age_limit.text()) > 0:
                self.stringBuffer += "AGE_LIMIT:" + int(self.ui.age_limit.text()) + "\n"
        except:
            print("not an int")
        self.file_io.write(self.string_buffer)
        self.file_io.close()
        self.close()


'''
    def on_selectDirButton_pressed(self):
        file_dialog = QDirModel
        file_dialog.__init__()
        QFileDialog.getExistingDirectory()
'''