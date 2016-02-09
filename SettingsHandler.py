from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog, QDirModel
from SettingsWindow import Ui_SettingDialog
import SettingsWindow
import io
_author__ = 'Luke Zambella'


class SettingsDialog(QDialog):
    string_buffer = ""

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
        self.close()


'''
    def on_selectDirButton_pressed(self):
        file_dialog = QDirModel
        file_dialog.__init__()
        QFileDialog.getExistingDirectory()
'''