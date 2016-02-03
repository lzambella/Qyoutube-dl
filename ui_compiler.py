from PyQt5.uic import compileUi
__author__ = 'luke'

def compile_ui():
    compileUi(open("about.ui"), open("about.py",'w'))
    compileUi(open("Qyoutube-dl_main.ui"), open("MainWindow.py", 'w'))
    compileUi(open("settings.ui"), open("SettingsWindow.py", 'w'))
compile_ui()
