# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdfreader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

FONT_SIZES = range(8,144,2)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        label_font = QFont('Arial', 10, QFont.Bold)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(720, 480)
        MainWindow.setWindowIcon(QIcon('images/logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setFont(label_font)

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setFont(label_font)

        self.menuApp = QtWidgets.QMenu(self.menubar)
        self.menuApp.setObjectName("menuApp")
        self.menuApp.setFont(label_font)
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.editor = QtWidgets.QTextEdit()
        # Open file
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionOpen_file.setIcon(QIcon('images/file.png'))
        # About action
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setIcon(QIcon('images/about.png'))
        self.actionAbout.setShortcut('Ctrl+I')
        # Action Quit
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setIcon(QIcon('images/quit.png'))
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.triggered.connect(self.close)
        # Open action in toolbar
        self.openAction = QtWidgets.QAction()
        self.openAction.setIcon(QIcon('images/open.png'))
        self.openAction.setCheckable(True)
        self.openAction.setStatusTip("Open file")
        self.openAction.setIconText('Open file')
        # Save action in toolbar
        self.saveAction = QtWidgets.QAction()
        self.saveAction.setIcon(QIcon('images/save.png'))
        self.saveAction.setCheckable(True)
        self.saveAction.setStatusTip("Save file")
        self.saveAction.setIconText('Save file')
        # Save as action in toolbar
        self.saveAsAction = QtWidgets.QAction()
        self.saveAsAction.setIcon(QIcon('images/save_as.png'))
        self.saveAsAction.setCheckable(True)
        self.saveAsAction.setStatusTip("Save as")
        self.saveAsAction.setIconText('Save as')
        # Print action in toolbar
        self.printAction = QtWidgets.QAction()
        self.printAction.setIcon(QIcon('images/print.png'))
        self.printAction.setCheckable(True)
        self.printAction.setStatusTip("Print")
        self.printAction.setIconText('Print')
        # Cut action in toolbar
        self.cutAction = QtWidgets.QAction()
        self.cutAction.setIcon(QIcon('images/cut.png'))
        self.cutAction.setCheckable(True)
        self.cutAction.setStatusTip("Cut")
        self.cutAction.setIconText('Cut')
        self.cutAction.setShortcut(QtGui.QKeySequence.Cut)
        self.cutAction.triggered.connect(self.editor.cut)
        # Copy action in toolbar
        self.copyAction = QtWidgets.QAction()
        self.copyAction.setIcon(QIcon('images/copy.png'))
        self.copyAction.setCheckable(True)
        self.copyAction.setStatusTip("Paste")
        self.copyAction.setIconText('Copy')
        self.cutAction.setShortcut(QtGui.QKeySequence.Copy)
        self.copyAction.triggered.connect(self.editor.copy)
        # Undo action in toolbar
        self.undoAction = QtWidgets.QAction()
        self.undoAction.setIcon(QIcon('images/undo.png'))
        self.undoAction.setCheckable(True)
        self.undoAction.setStatusTip("Undo")
        self.undoAction.setIconText('Undo')
        self.undoAction.setShortcut(QtGui.QKeySequence.Undo)
        self.undoAction.triggered.connect(self.editor.undo)
        # Paste action in toolbar
        self.pasteAction = QtWidgets.QAction()
        self.pasteAction.setIcon(QIcon('images/paste.png'))
        self.pasteAction.setCheckable(True)
        self.pasteAction.setStatusTip("Paste")
        self.pasteAction.setIconText('Paste')
        self.cutAction.setShortcut(QtGui.QKeySequence.Paste)
        self.pasteAction.triggered.connect(self.editor.paste)
        # Menu action connection
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.saveAction)
        self.menuFile.addAction(self.saveAsAction)
        self.menuApp.addAction(self.actionAbout)
        self.menuApp.addAction(self.actionQuit)
        self.menubar.addAction(self.menuApp.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.vboxLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        # Filetoolbar and all its connections
        self.file_toolbar = QtWidgets.QToolBar('File Toolbar')
        self.file_toolbar.addAction(self.openAction)
        self.file_toolbar.addAction(self.saveAction)
        self.file_toolbar.addAction(self.saveAsAction)
        self.file_toolbar.addAction(self.printAction)
        # Font selection widget
        self.fonts = QtWidgets.QFontComboBox()
        self.fonts.currentFontChanged.connect(self.editor.setCurrentFont)
        # Font size selection widget
        self.font_size = QtWidgets.QComboBox()
        self.font_size.addItems([str(s) for s in FONT_SIZES])
        self.font_size.currentIndexChanged[str].connect(lambda s: self.editor.setFontPointSize(float(s)) )
        # Bold action
        self.actionBold = QtWidgets.QAction(MainWindow)
        self.actionBold.setIcon(QIcon('images/bold.png'))
        self.actionBold.setStatusTip("Bold")
        self.actionBold.setCheckable(True)
        self.actionBold.setIconText('Bold')
        self.actionBold.triggered.connect(lambda x: self.editor.setFontWeight(QtGui.QFont.Bold if x else QtGui.QFont.Normal))
        self.actionBold.setShortcut(QtGui.QKeySequence.Bold)
        # Italic action
        self.actionItalic = QtWidgets.QAction(MainWindow)
        self.actionItalic.setIcon(QIcon('images/italic.png'))
        self.actionItalic.setStatusTip("Italic")
        self.actionItalic.setCheckable(True)
        self.actionItalic.setIconText('Italic')
        self.actionItalic.triggered.connect(self.editor.setFontItalic)
        self.actionItalic.setShortcut(QtGui.QKeySequence.Italic)
        # Underline action
        self.actionUnderline = QtWidgets.QAction(MainWindow)
        self.actionUnderline.setIcon(QIcon('images/underline.png'))
        self.actionUnderline.setStatusTip("Underline")
        self.actionUnderline.setCheckable(True)
        self.actionUnderline.setIconText('Underline')
        self.actionUnderline.triggered.connect(self.editor.setFontUnderline)
        self.actionUnderline.setShortcut(QtGui.QKeySequence.Underline)
        # Align left action
        self.actionAlignLeft = QtWidgets.QAction(MainWindow)
        self.actionAlignLeft.setIcon(QIcon('images/leftSide.png'))
        self.actionAlignLeft.setStatusTip("Align text left")
        self.actionAlignLeft.setCheckable(True)
        self.actionAlignLeft.setIconText('Align text left')
        self.actionAlignLeft.triggered.connect(lambda: self.editor.setAlignment(QtCore.Qt.AlignLeft))
        # Align right action 
        self.actionAlignRight = QtWidgets.QAction(MainWindow)
        self.actionAlignRight.setIcon(QIcon('images/rightSide.png'))
        self.actionAlignRight.setStatusTip("Align text right")
        self.actionAlignRight.setCheckable(True)
        self.actionAlignRight.setIconText('Align text right')
        self.actionAlignRight.triggered.connect(lambda: self.editor.setAlignment(QtCore.Qt.AlignRight))
        # Align center action
        self.actionAlignCenter = QtWidgets.QAction(MainWindow)
        self.actionAlignCenter.setIcon(QIcon('images/center.png'))
        self.actionAlignCenter.setStatusTip("Align text center")
        self.actionAlignCenter.setCheckable(True)
        self.actionAlignCenter.setIconText('Align text center')
        self.actionAlignCenter.triggered.connect(lambda: self.editor.setAlignment(QtCore.Qt.AlignCenter))
        # Align both sides action
        self.actionAlignWhole = QtWidgets.QAction(MainWindow)
        self.actionAlignWhole.setIcon(QIcon('images/whole.png'))
        self.actionAlignWhole.setStatusTip("Align text whole")
        self.actionAlignWhole.setCheckable(True)
        self.actionAlignWhole.setIconText('Align text whole')
        self.actionAlignWhole.triggered.connect(lambda: self.editor.setAlignment(QtCore.Qt.AlignJustify))
        # Cut or paste toolbar
        self.text_toolbar = QtWidgets.QToolBar('Text Toolbar')
        self.text_toolbar.addAction(self.cutAction)
        self.text_toolbar.addAction(self.copyAction)
        self.text_toolbar.addAction(self.pasteAction)
        self.text_toolbar.addAction(self.undoAction)
        # Text edit toolbar
        self.edit_toolbar = QtWidgets.QToolBar('Edit text')
        self.edit_toolbar.addWidget(self.fonts)
        self.edit_toolbar.addWidget(self.font_size)
        self.edit_toolbar.addAction(self.actionBold)
        self.edit_toolbar.addAction(self.actionItalic)
        self.edit_toolbar.addAction(self.actionUnderline)
        self.edit_toolbar.addAction(self.actionAlignLeft)
        self.edit_toolbar.addAction(self.actionAlignRight)
        self.edit_toolbar.addAction(self.actionAlignCenter)
        self.edit_toolbar.addAction(self.actionAlignWhole)

        self.addToolBar(self.file_toolbar)
        self.addToolBar(self.text_toolbar)
        self.addToolBar(self.edit_toolbar)

        self.vboxLayout.addWidget(self.editor)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuApp.setTitle(_translate("MainWindow", "App"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
