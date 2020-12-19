import sys 
from PyQt5.QtWidgets import QApplication
from texteditor import ReaderMainWindow

APP = QApplication(sys.argv)

reader = ReaderMainWindow()

sys.exit(APP.exec_())