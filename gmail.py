#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#########################################
#Bu program Muslu YÜKSEKTEPE tarafından hazırlanmıştır.
#Gmail hesabınıza bağlanıp mail göndermenizi sağlar.
#Mechanize modülü kullanılmıştır.
#Modülün varlığı kontrol edilmekte ve kullanmış olduğunuz işletim sistemine göre
#size link verilmektedir.
#2010 www.yazki.com
# musluyuksektepe@gmail.com
#########################################
from PyQt4 import QtCore, QtGui
import sys
import cookielib, sys, os
isletimsistemi = os.name

class kontrol():
    def __init__(self, ui):
        self.ui = ui
    def baglan(self):

        try:
# mechanize kütüphanesi varmı diye kontrol ediyoruz
            import mechanize
        except ImportError:
# kütüphane yoksa hata ver 
            print "Moduller bulunamadi"
# işletim sistemini kontrol et
            if isletimsistemi == 'posix':
# linux ise
                print "sudo apt-get install python-mechanize\n komutu ile bagimliliklari kurun."
            else:
# başka bir işletim sistemi ise
                print "http://wwwsearch.sourceforge.net/mechanize/src/mechanize-0.1.11.zip"
                print "İndirdiğiniz klasoru zipten cikartin"
                print "komut satırında klasore gidin"
                print "setup.py install\n yazarak kurulumu yapin"
# programi kapat  
            sys.exit (1)
        else:
# Tarayıcı oluştur
            br = mechanize.Browser()
# Cookie Jar
            cj = cookielib.LWPCookieJar()
            br.set_cookiejar(cj)
# Tarayıcı ayarları
            br.set_handle_equiv(True)
            br.set_handle_gzip(True)
            br.set_handle_redirect(True)
            br.set_handle_referer(True)
            br.set_handle_robots(False)
# yenile ama askıya alma
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# Kullanıcı ve gidecek mail bilgileri
            kullaniciadiraw= ui.lineEdit.text()
            sifreraw= ui.lineEdit_2.text()
            toraw= ui.lineEdit_3.text()
            subjectraw= ui.lineEdit_4.text()
            bodyraw= ui.plainTextEdit.toPlainText()

# sayfayı html türünde açtırıyoruz
            br.open("https://mail.google.com/mail/h/1a8m94mtpabm4/?zy=a&f=1") # bu siteyi aç
            br.select_form(nr=0)  # kullanılacak form numarası
# girilen kullanıcı bilgilerini eşitliyoruz
            br["Email"]=kullaniciadiraw
            br["Passwd"]=sifreraw
            br.submit() # gönder
            ui.label_6.setText(u"Bağlandı!")

# mail gönderme sayfasına bağlanıyoruz
            br.open("https://mail.google.com/mail/h/5sq3vpo5rgzt/?v=b&pv=tl&cs=b")
            br.select_form(nr=1)
# gidecek mail bilgilerini eşitliyoruz
            br["to"]= toraw
            br["subject"]= subjectraw
            br["body"]= bodyraw
            br.submit()
# mail gönderildiyse bilgi veriyoruz
            ui.label_6.setText(u"Mailiniz gönderildi!")


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 375)
        Dialog.setMinimumSize(QtCore.QSize(360, 375))
        Dialog.setMaximumSize(QtCore.QSize(360, 375))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 18))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 62, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 41, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 41, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 62, 18))
        self.label_5.setObjectName("label_5")
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 70, 321, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 221, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 50, 221, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 90, 271, 26))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 120, 271, 26))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 330, 92, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 340, 181, 20))
        self.label_6.setObjectName("label_6")
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 160, 271, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 340, 62, 18))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        self.kontrol = kontrol(self)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.kontrol.baglan)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Gmail\'den Mail Gönderme", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Kullanıcı Adı: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Şifre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Kime:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Konu:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "İçerik:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Gönder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Durum:", None, QtGui.QApplication.UnicodeUTF8))


app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())