# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 272)
        Dialog.setMinimumSize(QtCore.QSize(464, 272))
        Dialog.setMaximumSize(QtCore.QSize(464, 272))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 441, 251))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.hakkinda_tab = QtGui.QWidget()
        self.hakkinda_tab.setObjectName("hakkinda_tab")
        self.hakkinda_label = QtGui.QLabel(self.hakkinda_tab)
        self.hakkinda_label.setGeometry(QtCore.QRect(10, 10, 421, 171))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.hakkinda_label.setFont(font)
        self.hakkinda_label.setObjectName("hakkinda_label")
        self.tabWidget.addTab(self.hakkinda_tab, "")
        self.yazar_tab = QtGui.QWidget()
        self.yazar_tab.setObjectName("yazar_tab")
        self.yazar_label = QtGui.QLabel(self.yazar_tab)
        self.yazar_label.setGeometry(QtCore.QRect(10, 10, 391, 171))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.yazar_label.setFont(font)
        self.yazar_label.setObjectName("yazar_label")
        self.tabWidget.addTab(self.yazar_tab, "")
        self.hata_bildirimi_tab = QtGui.QWidget()
        self.hata_bildirimi_tab.setObjectName("hata_bildirimi_tab")
        self.hata_bildirimi_label = QtGui.QLabel(self.hata_bildirimi_tab)
        self.hata_bildirimi_label.setGeometry(QtCore.QRect(10, 10, 391, 171))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.hata_bildirimi_label.setFont(font)
        self.hata_bildirimi_label.setObjectName("hata_bildirimi_label")
        self.tabWidget.addTab(self.hata_bildirimi_tab, "")
        self.destek_tab = QtGui.QWidget()
        self.destek_tab.setObjectName("destek_tab")
        self.destek_label = QtGui.QLabel(self.destek_tab)
        self.destek_label.setGeometry(QtCore.QRect(10, 10, 391, 171))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.destek_label.setFont(font)
        self.destek_label.setObjectName("destek_label")
        self.tabWidget.addTab(self.destek_tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Hakkında", None, QtGui.QApplication.UnicodeUTF8))
        self.hakkinda_label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Diyanet verilerine göre tüm ülke ve şehirler için namaz </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">vakitlerini gösterir. İsteğe bağlı olarak namaz vaktinde </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">ezan ve ezan duasını okur.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\';\"></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Ezan için kullanılan ses dosyaları İsmail COŞAR\'a aittir. </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\';\"></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Proje Sayfası: </span><a href=\"http://code.google.com/p/pyvakitci\"><span style=\" font-family:\'Sans\'; text-decoration: underline; color:#0000ff;\">http://code.google.com/p/pyvakitci</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hakkinda_tab), QtGui.QApplication.translate("Dialog", "Hakkında", None, QtGui.QApplication.UnicodeUTF8))
        self.yazar_label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Rahman YAZGAN</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:rahmanyazgan@gmail.com\"><span style=\" font-family:\'Sans\'; text-decoration: underline; color:#0000ff;\">rahmanyazgan@gmail.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.yazar_tab), QtGui.QApplication.translate("Dialog", "Yazar", None, QtGui.QApplication.UnicodeUTF8))
        self.hata_bildirimi_label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Hataları bildirmek için </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:rahmanyazgan@gmail.com\"><span style=\" font-family:\'Sans\'; text-decoration: underline; color:#0000ff;\">rahmanyazgan@gmail.com</span></a><span style=\" font-family:\'Sans\';\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">adresini kullanınız.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hata_bildirimi_tab), QtGui.QApplication.translate("Dialog", "Hata Bildirimi", None, QtGui.QApplication.UnicodeUTF8))
        self.destek_label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Programa katkıda bulunmak istiyorsanız </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:rahmanyazgan@gmail.com\"><span style=\" font-family:\'Sans\'; text-decoration: underline; color:#0000ff;\">rahmanyazgan@gmail.com</span></a><span style=\" font-family:\'Sans\';\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">adresinden bana ulaşabilirsiniz.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.destek_tab), QtGui.QApplication.translate("Dialog", "Destek", None, QtGui.QApplication.UnicodeUTF8))

