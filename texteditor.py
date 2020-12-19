from ui_texteditor import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtPrintSupport import *
import os

class ReaderMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self, *args, **kwargs):
		super(ReaderMainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)
		self.show()

		self.openAction.triggered.connect(self.open_file)
		self.saveAction.triggered.connect(self.save_file)
		self.saveAsAction.triggered.connect(self.saveas_file)
		self.printAction.triggered.connect(self.print)
		self.actionAbout.triggered.connect(self.aboutAction)

	def splitext(self, p):
		return os.path.splitext(p)[1].lower()

	def set_updated_title(self):
		self.setWindowTitle("{0} - Solid".format(os.path.basename(self.path) if self.path else "Untitled"))

	def open_file(self):
		path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file","", "Text documents (*.txt);")

		try:
			with open(path, 'rU') as file:
				text = file.read()
		except Exception as exp:
			self.dialog_error(str(exp))

		else:
			self.path = path
			self.editor.setText(text)
			self.set_updated_title()

	def save_file(self):
		if self.path is None:
			return self.saveas_file()
		
		text = self.editor.toPlainText()

		try:
			with open(self.path, 'w') as file:
				file.write(text)

		except Exception as e:
			self.dialog_critical(str(e))

	def saveas_file(self):
		path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);")

		if not path:
			return 
		
		text = self.editor.toPlainText()

		try:
			with open(path, 'w') as file:
				file.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path
			self.set_updated_title()

	def print(self):
		dlg = QPrintDialog()
		if dlg.exec_():
			self.editor.print_(dlg.printer())


	def dialog_error(self, s):
		dlg = QtWidgets.QMessageBox(self)
		dlg.setText(s)
		dlg.setIcon(QtWidgets.QMessageBox.Critical)
		dlg.show()
	
	def aboutAction(self):
		about = QtWidgets.QMessageBox.about(self, 'About', "This my text editor that I've created using PyQt5")
