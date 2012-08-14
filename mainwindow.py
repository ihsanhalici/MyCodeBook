#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from ana_ekran import Ui_MainWindow
import sys

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.statusBar().showMessage(unicode("Hazir\n")) 

	@QtCore.pyqtSignature("bool")
        def on_pushButton_clicked(self):
	        liste = self.listWidget
	        ekle  = str(self.lineEdit.text())
	        liste.addItem(ekle)		

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_()) 