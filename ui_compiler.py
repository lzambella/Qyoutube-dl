from PyQt5.uic import compileUi
__author__ = 'luke'

def compile_ui():
    compileUi(open("UI_Files/about.ui"), open("Compiled_UI/about.py",'w'))
    compileUi(open("UI_Files/main_window.ui"), open("Compiled_UI/MainWindow.py", 'w'))
compile_ui()
