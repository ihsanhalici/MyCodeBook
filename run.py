#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from toplu_mail2 import Ui_MainWindow
from mail import mail
import sys, re, time

def dogrula(email):
	if len(email) > 7:
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
			return 0
	return 1

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.statusBar().showMessage(unicode("Hazir\n"))

	@QtCore.pyqtSignature("bool")
        def on_pushButton_2_clicked(self):
	        liste = self.listWidget
	        ekle  = str(self.lineEdit_7.text())
	        if(ekle == "" or dogrula(ekle)):
	        	a = QtGui.QMessageBox()
	        	a.setWindowTitle("Bos veya hatali giris")		
	        	a.setText("Yanlis mail girisi yaptiniz!")
	        	a.setIcon(a.Information)
	        	a.exec_()	        	
	        else:
	        	liste.addItem(ekle)
	        	self.lineEdit_7.clear()	


	@QtCore.pyqtSignature("bool")
        def on_pushButton_3_clicked(self):
	        mailler = open("mail.txt")
	        liste = self.listWidget
	        for mail in mailler:
	        	liste.addItem(str(mail).replace("\n",""))
	        
	@QtCore.pyqtSignature("bool")
        def on_pushButton_clicked(self):

        	gmail_user  = str(self.lineEdit_4.text())
        	gmail_pwd   = str(self.lineEdit.text())

        	konu 		= str(self.lineEdit_5.text())
        	metin		= str(self.textEdit.toPlainText())

        	kimden		= str(self.lineEdit_6.text())

        	mserver		= str(self.lineEdit_2.text())
        	mport		= int(self.lineEdit_3.text())

        	i = 0
        	while(i < self.listWidget.count()):
        		gonderilcek = str(self.listWidget.item(i).text())
        		self.statusBar().showMessage(unicode("Gonderiliyor: %i\n")%(i+1))        		
        		try:
        			mail(gonderilcek, kimden, konu, metin, gmail_user, gmail_pwd, mserver, mport)
        		except:
		        	a = QtGui.QMessageBox()
		        	a.setWindowTitle("Hata")		
		        	a.setText("Bilgileri kontrol ediniz!")
		        	a.setIcon(a.Warning)
		        	a.exec_()	        			        				
    			i = i +1
    			self.progressBar.setValue(int(i/self.listWidget.count())*100)
    			time.sleep(1)
    		self.statusBar().showMessage(unicode("Hazir\n")) 
	

app = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())