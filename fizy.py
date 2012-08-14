#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib
import simplejson
import threading
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.kayitYeri="kayit"
	self.muzikIsimListesi=[]
	self.muzikIdListesi=[]
	self.indirileceklist=[]
	self.indirIsimliste=[]
	self.seciliOge=""
	self.kontrol2=0
	self.sarki=""
	self.page=0
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle("Fizy.Com'dan Muzik Indir")

	self.txtSearch = QtGui.QLineEdit(self)
	self.txtSearch.setGeometry(QtCore.QRect(20, 20, 171, 27))
        self.txtSearch.setObjectName(_fromUtf8("txtSearch"))
	
	self.btnsearch = QtGui.QPushButton('Search',self)
        self.btnsearch.setGeometry(QtCore.QRect(206, 20, 71, 27))
        self.btnsearch.setObjectName(_fromUtf8("btnsearch"))
	self.btnsearch.clicked.connect(self.btnSearch)	
	
	self.label = QtGui.QLabel('?',self)
        self.label.setGeometry(QtCore.QRect(30, 50, 240, 17))
        self.label.setObjectName(_fromUtf8("label"))
	
	self.btndownload = QtGui.QPushButton('Download',self)
        self.btndownload.setGeometry(QtCore.QRect(120, 360, 97, 27))
        self.btndownload.setObjectName(_fromUtf8("btndownload"))
	self.btndownload.clicked.connect(self.musicDownload)
	
	self.btnMore = QtGui.QPushButton('>>',self)
        self.btnMore.setGeometry(QtCore.QRect(230, 360, 40, 27))
        self.btnMore.setObjectName(_fromUtf8("btnMore"))
	self.btnMore.clicked.connect(self.moreResult)
	
	self.btnkayityeri = QtGui.QPushButton('Kayit Yeri',self)
        self.btnkayityeri.setGeometry(QtCore.QRect(20, 360, 97, 27))
        self.btnkayityeri.setObjectName(_fromUtf8("btnkayityeri"))	
	self.btnkayityeri.clicked.connect(self.kayitYeriAyarla)
	
	self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(20, 70, 251, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 279))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.listWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 251, 281))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
	self.listWidget.currentItemChanged.connect(self.selectedItemChange)
	
        self.show()
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',"inen dosyalar olabilir. Eminmisiniz?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
	if reply == QtGui.QMessageBox.Yes:
         	event.accept()
        else:
            	event.ignore()
    def musicDownload(self):
	seciliId=self.muzikIdListesi[self.listWidget.currentRow()]
	self.musicIndirmeIslemi(seciliId)
    def musicIndirmeIslemi(self,ID):
	#print "Dosya indiriliyor...."
	aramaBilgileri='SID=%s'%ID
	site=urllib.urlopen('http://fizy.com/fizy::getSong',aramaBilgileri)
	j=simplejson.loads(site.read())
	link=j["source"]
	title=u"%s"%j["title"]
	#bidakka dur
	self.indirileceklist.append(link)
	self.indirIsimliste.append(title)
	#thread başlat
	thrDown=AsyncDownload(link,title)
	thrDown.kayitYoluAl(self.kayitYeri)
	thrDown.start()
    def moreResult(self):
	self.page+=1
	self.muzikAra(self.sarki)
    def btnSearch(self):
	self.sarki=unicode(self.txtSearch.text()).encode('utf-8')
	self.page=0
	self.muzikAra(self.sarki)
    def muzikAra(self,sarki):
	if self.page==0:
		self.listWidget.clear()
		del self.muzikIdListesi[0:len(self.muzikIdListesi)]
	aramaBilgileri="query=%s&p=%s"%(sarki,self.page)
	site=urllib.urlopen('http://fizy.com/search',aramaBilgileri)
	j=simplejson.loads(site.read())
	for item in j["results"]:
		if item["type"]=="audio":
			self.muzikIdListesi.append(item["ID"])
			self.listWidget.addItem(item["title"])
    def kayitYeriAyarla(self):
	if self.kayitYeri=="kayit":
		self.kayitYeri = "%s"%QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
		print "Dosyalar %s 'ye indirilecek."%self.kayitYeri
    def selectedItemChange(self):
	try:	
		self.seciliOge=unicode(self.listWidget.currentItem().text()).encode('utf-8')
		self.label.setText(_fromUtf8(self.seciliOge))
	except AttributeError:
		self.label.setText(_fromUtf8("?"))
class AsyncDownload(threading.Thread):
    def __init__(self,liste,indirIsimliste):
	threading.Thread.__init__(self);
	self.indirliste=liste
	self.indirIsimliste=indirIsimliste
	self.kayitYolu=""
    def kayitYoluAl(self,kayitYolu):
	self.kayitYolu=kayitYolu
    def run(self):
	self.indir()
    def indir(self):
	try:
		print u"%s dosyası indiriliyor..."%self.indirIsimliste
		link=self.indirliste
		music=urllib.urlopen(link).read()
		tempStr=u"%s/%s.m4a"%(self.kayitYolu,self.indirIsimliste)
		file=open(tempStr,'w')
		file.write(music)
		file.close()
		print "%s 'ye indirildi :)"%tempStr
	except:
		print "%s dosyası inerken hata!"%self.indirIsimliste
		
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  
