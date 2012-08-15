#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from tckimlik import Ui_MainWindow
import sys

def tcno_checksum(tcno):
	if len(str(tcno)) == 9:
	    tc    = '%d' % tcno
	    tc10  = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
	    tc10 *= 7
	    tc10 -= int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
	    tc10 %= 10
	    tc11  = int(tc[0]) + int(tc[1]) + int(tc[2]) + int(tc[3]) + int(tc[4])
	    tc11 += int(tc[5]) + int(tc[6]) + int(tc[7]) + int(tc[8]) + int(tc10)
	    tc11 %= 10
	    return '%s%d%d' % (tc, tc10, tc11)
	else:
		return 0    

def akraba_tcno(tcno, adet):
    akraba_liste = ''
    tc   = int(tcno[0:-2])
    t    = tc - 29999 * (1 + int(adet / 2))
    for i in range(adet+1):
        t += 29999
        atc = tcno_checksum(t)
        if atc == tcno:
        	pass
        else:
        	akraba_liste += "'%s'," % atc
    return akraba_liste[0:-1]

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.statusBar().showMessage(unicode("Hazir\n"))

	@QtCore.pyqtSignature("bool")
        def on_pushButton_clicked(self):
        	liste = self.listWidget
        	tcno = int(self.lineEdit.text())

        	if tcno_checksum(tcno):
        		liste.addItem(str(tcno_checksum(tcno)))
        		self.lineEdit.setText(str(tcno_checksum(tcno)))

	@QtCore.pyqtSignature("bool")
        def on_pushButton_2_clicked(self):
        	liste = self.listWidget
        	adet  = int(self.spinBox.value())
        	tcno = str(self.lineEdit.text())
        	i = 1
        	deger = 1

        	while i <= adet:
	        	liste.addItem(akraba_tcno(tcno,adet)[deger:deger+11])
	        	i = i+1
	        	deger = deger+14

	@QtCore.pyqtSignature("bool")
        def on_pushButton_3_clicked(self):
        	 QtGui.QApplication.clipboard().setText(self.listWidget.currentItem().text())	        	

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())        	