# -*- coding: utf-8 -*-
#!/usr/bin/env python

from PyQt4 import QtGui, QtCore, QtSql
from moduller.Ui_Vakitler import Ui_Dialog

class AylikVakitler(QtGui.QDialog, Ui_Dialog):
    veritabaniVarmi = None
    
    def __init__(self, veritabaniDosyasi, statusBar):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
                
        self.database = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        veritabaniDosyasi = QtCore.QFile(veritabaniDosyasi)
        
        self.vakitleriGoster(veritabaniDosyasi.fileName(), statusBar)
        
    def vakitleriGoster(self, veritabaniDosyasi, statusBar):
        if QtCore.QFile.exists(veritabaniDosyasi):
            if veritabaniDosyasi.size() != 0:
                self.database.setDatabaseName(veritabaniDosyasi)
                
                if self.database.open():
                    model = QtSql.QSqlTableModel(self)
                    model.setTable("namazvakitleri")
                    model.select()
                    
                    veri = model.record(0).value("Tarih").toString()
                    
                    if len(veri) != 0:
                        self.tableView.setModel(model)
                        self.exec_()
                        AylikVakitler.veritabaniVarmi = True
                    else:
                        QtGui.QMessageBox.information(self, u"Bilgilendirme",
                                                      u"Aylık namaz vakitleri veritabanı boş. " + 
                                                      u"\"Kapat\" butonuna bastığınızda veritabanınız güncellenecek.", 
                                                      "Kapat")
                        
                        statusBar.showMessage(u"Vakitler güncelleniyor...")
                        
                        AylikVakitler.veritabaniVarmi = False
        else:
            AylikVakitler.veritabaniVarmi = False
