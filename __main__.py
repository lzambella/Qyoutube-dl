#!/usr/bin/env python
"""__main__.py: Main execution program"""
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QWidget
from MainWindow import Ui_MainWindow
from about import Ui_About
import sys

__author__ = "Luke Zambella"
__copyright__ = "Copyright 2016"


class Qyoutube_dl(QMainWindow):
    def __init__(self):
        super(Qyoutube_dl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.actionAbout.triggered.connect(AboutWindow.__init__)


class AboutWindow(QDialog):
        def __init__(self):
            super(AboutWindow, self).__init__()
            self.about_dialog = Ui_About()
            self.about_dialog.setupUi(self)
            self.exec_()


# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    prgm = Qyoutube_dl()
    prgm.__init__()
    prgm.show()
    sys.exit(app.exec_())
