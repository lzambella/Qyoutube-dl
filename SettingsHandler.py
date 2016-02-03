from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog, QDirModel
from SettingsWindow import Ui_SettingDialog
import SettingsWindow
import io
_author__ = 'Luke Zambella'


class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.ui = Ui_SettingDialog()
        self.ui.setupUi(self)

    def on_setKeyButton_pressed(self):
        file = io.open("key.txt", 'w')
        file.write(self.ui.keyLine.text())

    def on_okButton_pressed(self):
        self.close()
'''
    def on_selectDirButton_pressed(self):
        file_dialog = QDirModel
        file_dialog.__init__()
        QFileDialog.getExistingDirectory()
'''