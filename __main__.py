#!/usr/bin/env python
"""__main__.py: Main execution program"""
import sys
from PyQt5.QtWidgets import QApplication
from Controllers.MainWindowController import MainWindow
from youtube_dl import version as yt_version
import Version as prgm_version

if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = MainWindow()
    program.show()
    print("Software version: " + prgm_version.__version__)
    print("Youtube_dl version: " + yt_version.__version__)
    sys.exit(app.exec_())
