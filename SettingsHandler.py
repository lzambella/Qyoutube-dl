from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from SettingsWindow import Ui_Dialog
import SettingsWindow
_author__ = 'Luke Zambella'


class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
