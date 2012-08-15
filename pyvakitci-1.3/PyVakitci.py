#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hazırlayan : Rahman Yazgan (rahmanyazgan@gmail.com)
# Lisans : GPL v.3
# Sürüm : 1.3

import os, platform, re, sqlite3, sys, threading, urllib

try:
    from PyQt4 import QtCore, QtGui
except:
    print u"PyQt4 modülü ve Phonon yüklü değil.\n\n" + \
    u"Paket yöneticisinden PyQt4 modülünü ve \nPhonon'u yükleyin ve tekrar deneyin.\n\n" + \
    u"Kurulum için komutlar:\n" + \
    u"Ubuntu: sudo apt-get install python-qt4 python-qt4-phonon\n" + \
    u"Pardus: sudo pisi install python-qt python-qt-phonon"
    exit()

# Aşağıdaki try-except bloğundaki QMessageBox'un sorunsuz çalışması
# için uygulama değişkeni burada tanımlandı.

uygulama = QtGui.QApplication(sys.argv)

try:
    from PyQt4.phonon import Phonon
except:
    QtGui.QMessageBox.information(None, u"Modül Hatası",
                                  u"Paket yöneticisinden phonon modülünü yükleyin ve tekrar deneyin.\n\n" + \
                                  u"Kurulum için komutlar:\n" + \
                                  u"Ubuntu: sudo apt-get install python-qt4-phonon\n" + \
                                  u"Pardus: sudo pisi install python-qt-phonon", "Kapat")
    exit()

from moduller.DiyanetUlkelerSehirler import DiyanetUlkelerSehirler
from moduller.DiyanetSehirleriEkle import DiyanetSehirler
from moduller.ZamanUlkelerSehirler import ZamanUlkelerSehirler
from moduller.ZamanSehirleriEkle import ZamanSehirler

# Miladi-Hicri tarih dönüşümü işleminde kullanıldı
from moduller.Calverter import Calverter

from moduller.Ui_PyVakitci import Ui_MainWindow

class PyVakitci(QtGui.QMainWindow, Ui_MainWindow):
    kaynak = ""
    calismaDizini = ""
    veriler = {}
    version = 1.3
    rlock = None
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)        
        
        self.mediaNesnesi = Phonon.MediaObject(self)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.mediaNesnesi, self.audioOutput)
        
        self.volumeSlider.setAudioOutput(self.audioOutput)
        self.volume = None
        
        self.actionCleanlooks.triggered.connect(self.cleanlooksGorunumu)
        self.actionOxygen.triggered.connect(self.oxygenGorunumu)
        self.actionPlastique.triggered.connect(self.plastiqueGorunumu)
        self.actionWindowsXP.triggered.connect(self.windowsXPGorunumu)
        self.actionWindowsVista.triggered.connect(self.windowsVistaGorunumu)
        self.actionCikis.triggered.connect(sys.exit)
        self.actionVakitleriGoster.triggered.connect(self.vakitleriGoster)
        self.actionLisans.triggered.connect(self.lisans)
        self.actionHakkinda.triggered.connect(self.hakkindaDialog)
        self.actionQtHakkinda.triggered.connect(QtGui.QApplication.aboutQt)
        self.audioOutput.mutedChanged.connect(self.sesAyari)
        self.audioOutput.volumeChanged.connect(self.mutedAyari)
        self.her_zaman_ustte_checkBox.stateChanged.connect(self.herZamanUstte)
        self.kaynak_comboBox.currentIndexChanged.connect(self.bolgeselAyarlar)
        self.ezan_oku_checkBox.stateChanged.connect(self.ezanOkuKontrol)
        self.erken_uyari_checkBox.stateChanged.connect(self.erkenUyari)
        self.erken_uyari_lineEdit.setInputMask("99")
        self.vakitleri_guncelle_pushButton.clicked.connect(self.aylikVakitleriKaydet)
        self.vakitleri_goster_pushButton.clicked.connect(self.vakitleriTopluGoster)
        self.bolgesel_ayarlar_kaydet_pushButton.clicked.connect(self.ayarlariKaydet)
        self.ayarlar_kaydet_pushButton.clicked.connect(self.ayarlariKaydet)
        self.ayarlar_varsayilan_pushButton.clicked.connect(self.varsayilanAyarlar)
        self.sabah_toolButton.clicked.connect(self.sesDosyasiEkleSabah)
        self.ogle_toolButton.clicked.connect(self.sesDosyasiEkleOgle) 
        self.ikindi_toolButton.clicked.connect(self.sesDosyasiEkleIkindi)
        self.aksam_toolButton.clicked.connect(self.sesDosyasiEkleAksam)
        self.yatsi_toolButton.clicked.connect(self.sesDosyasiEkleYatsi)
        self.dua_toolButton.clicked.connect(self.sesDosyasiEkleDua)
        self.uyari_toolButton.clicked.connect(self.sesDosyasiEkleUyari)
        self.ses_kaydet_pushButton.clicked.connect(self.ayarlariKaydet)
        self.ses_varsayilan_pushButton.clicked.connect(self.sesVarsayilanAyarlar)
        self.site_01_label.linkActivated.connect(self.siteyeGir)
        self.site_02_label.linkActivated.connect(self.siteyeGir)
        self.site_03_label.linkActivated.connect(self.siteyeGir)
        self.site_04_label.linkActivated.connect(self.siteyeGir)
        self.site_05_label.linkActivated.connect(self.siteyeGir)
        self.site_06_label.linkActivated.connect(self.siteyeGir)
        self.site_07_label.linkActivated.connect(self.siteyeGir)
        self.site_08_label.linkActivated.connect(self.siteyeGir)
        self.site_09_label.linkActivated.connect(self.siteyeGir)
        self.site_10_label.linkActivated.connect(self.siteyeGir)
        self.site_11_label.linkActivated.connect(self.siteyeGir)
        self.site_12_label.linkActivated.connect(self.siteyeGir)
        self.trayIcon.activated.connect(self.iconActivated)

        self.programinKonumu = os.getcwdu().replace(os.sep, "/")
        
        self.ayarDosyasi = QtCore.QDir.homePath() + "/.PyVakitci/ayarlar.ini"
        
        self.ontanimliAyarDosyasi = self.programinKonumu + "/ontanimli_ayarlar.ini"
        
        self.sesDosyalariKonum = self.programinKonumu + "/ses_dosyalari/"        
        self.lisansDosyasi = str(self.programinKonumu + "/GPL_TR.html")
        
        self.hicriTarihDosyasi = self.programinKonumu + "/hicri.txt"
        self.miladiTarihDosyasi = self.programinKonumu + "/miladi.txt"
        
        self.besmeleDosyasi = self.sesDosyalariKonum + "besmele.ogg"
        
        self.simdikiTarih = QtCore.QDate().currentDate().toString("dd MMMM yyyy")
        
        self.mesajGosterildi = False
        self.windowFlag = None
        self.gorunum = "Cleanlooks"
        
        self.ulkelerSehirlerDiyanet = DiyanetUlkelerSehirler()
        self.ulkelerSehirlerZaman = ZamanUlkelerSehirler()
        
        self.sehirAdi = ""
        self.ulkeAdi = ""
        
        PyVakitci.kaynak = self.kaynak_comboBox.currentText()
        PyVakitci.rlock = threading.RLock()        
        
        self.cleanlooksGorunumu()
        self.calismaDizininiHazirla()
        self.bolgeselAyarlar()
        self.ekrandaOrtala()
        self.sesVarsayilanAyarlar()
        self.ayarlariUygula()
        self.hicriTarihiGuncelle()
        self.otomatikGuncellestir()
         
        self.timerSaat = QtCore.QTimer()
        self.connect(self.timerSaat, QtCore.SIGNAL("timeout()"), self.saatiGuncelle)
        self.timerSaat.start(400)

        if self.trayIcon.isVisible():
            pass
        else:
            self.trayIcon.show()
            
    def ekrandaOrtala(self):
        self.move((QtGui.QDesktopWidget().screenGeometry().width() - self.geometry().width()) / 2,
                  (QtGui.QDesktopWidget().screenGeometry().height() - self.geometry().height()) / 2)
        
    def calismaDizininiHazirla(self):
        if QtCore.QDir.exists(QtCore.QDir(QtCore.QDir.homePath() + "/.PyVakitci")) == False:
            QtCore.QDir(QtCore.QDir.homePath()).mkpath(".PyVakitci")
            
        PyVakitci.calismaDizini = QtCore.QDir.homePath() + "/.PyVakitci"
        PyVakitci.veritabaniDosyasi = str(PyVakitci.calismaDizini + "/pyvakitci.db")
    
    def otomatikGuncellestir(self):
        try:
            if self.otomatik_guncellestir_checkBox.isChecked():
                site = urllib.urlopen("http://pyvakitci.googlecode.com/svn/trunk/version.txt")
                version = float(site.read())
                
                print PyVakitci.version, version
                if PyVakitci.version < version:
                    site = urllib.urlopen("http://pyvakitci.googlecode.com/svn/trunk/surum_notlari.txt")
                    surumNotlari = site.read()
                    
                    soru = QtGui.QMessageBox.question(self, u'Güncelleme',
                        u"PyVakitci programının yeni sürümü mevcut.<br><br>" + 
                        "PyVakitci " + str(version) + u" sürüm notları:<br>" + 
                        surumNotlari + "<br><br>" + 
                        u"PyVakitci " + str(version) + u" sürümünü indirmek ister misiniz?",
                        QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    
                    if soru == QtGui.QMessageBox.Yes:
                        url = "http://code.google.com/p/pyvakitci/"
                        QtGui.QDesktopServices().openUrl(QtCore.QUrl(url))
        except:
            pass
        
    # trayIcon a tıklandığında program görünür/görünmez olur.    
    def iconActivated(self, reason):
        if reason in (QtGui.QSystemTrayIcon.Trigger, QtGui.QSystemTrayIcon.DoubleClick):
            if self.isVisible():
                self.setVisible(False) 
            else:
                self.setVisible(True)
                
    def cleanlooksGorunumu(self):        
        self.gorunum = "Cleanlooks"
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(self.gorunum))
        
    def plastiqueGorunumu(self):
        self.gorunum = "Plastique"
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(self.gorunum))
        
    def oxygenGorunumu(self):
        self.gorunum = "Oxygen"
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(self.gorunum))

    def windowsXPGorunumu(self):
        self.gorunum = "WindowsXP"
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(self.gorunum))

    def windowsVistaGorunumu(self):
        self.gorunum = "WindowsVista"
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(self.gorunum))
        
    def otomatikCalistir(self):
        isletimSistemi = platform.system()

        veriler = "#!/usr/bin/env xdg-open\n\n[Desktop Entry]"\
                + "\nEncoding=UTF-8\nVersion=1.0\nType=Application"\
                + "\nTerminal=false\nPath=" + self.programinKonumu\
                + "\nExec=" + self.programinKonumu + "/PyVakitci.py"\
                + "\nIcon=" + self.programinKonumu + "/resimler/cami.png"\
                + "\nName=PyVakitci"
        
        configAutostartDizini = QtCore.QDir.homePath() + "/.config/autostart/"
        xdgAutostartDizini = "/etc/xdg/autostart/"
        kisayolDosyasi = configAutostartDizini + "PyVakitci.desktop"
        
        if self.otomatik_calistir_checkBox.isChecked():
            isletimSistemi = platform.system()
            
            if isletimSistemi == "Linux":
                if QtCore.QDir.exists(QtCore.QDir(configAutostartDizini)) or QtCore.QDir.exists(QtCore.QDir(xdgAutostartDizini)):
                    if QtCore.QDir.exists(QtCore.QDir(configAutostartDizini)):
                        if QtCore.QFile.exists(QtCore.QFile(kisayolDosyasi)) == False:
                            dosya = open(kisayolDosyasi, "wb")
                            dosya.write(veriler)
                            dosya.close()
                    else:
                        QtCore.QDir(QtCore.QDir.homePath() + "/.config/").mkpath("autostart")
                        dosya = open(kisayolDosyasi, "wb")
                        dosya.write(veriler)
                        dosya.close()
                    
                    os.system("chmod +x " + str(kisayolDosyasi))
                else:
                    QtGui.QMessageBox.warning(self, "Hata", u"Kullandığınız dağıtım XDG masaüstü standardını desteklemiyor.\n" + 
                                              u"Paket yöneticisinden xdg yi kurduktan sonra tekrar deneyin.\n" + 
                                              u"Kurulması gerekenler: <b>xdg-user-dirs, xdg-utils</b>", "Kapat")
        else:
            if QtCore.QFile.exists(QtCore.QFile(kisayolDosyasi)):
                QtCore.QFile(kisayolDosyasi).remove()
        
    def besmeleyleBasla(self):
        if self.besmele_ile_basla_checkBox.isChecked():
            self.mediaNesnesi.setCurrentSource(Phonon.MediaSource(self.besmeleDosyasi))
            self.mediaNesnesi.play()
                    
    def herZamanUstte(self):
        if self.her_zaman_ustte_checkBox.isChecked():
            self.windowFlag = self.windowFlags()
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.setVisible(True)
        else:
            self.setWindowFlags(self.windowFlag)
            self.windowFlag = None
            self.setVisible(True)
        
        self.move(self.geometry().x() - 1, self.geometry().y() - 29)        
            
    # Label'daki link tarayıcıda açılır.
    def siteyeGir(self, URL):
        QtGui.QDesktopServices().openUrl(QtCore.QUrl(URL))
    
    def ezanOkuKontrol(self):
        if self.ezan_oku_checkBox.isChecked():
            self.dua_oku_checkBox.setEnabled(True)
        else:
            self.dua_oku_checkBox.setEnabled(False)
            self.dua_oku_checkBox.setChecked(False)
            
    def erkenUyari(self):
        if self.erken_uyari_checkBox.isChecked():
            self.erken_uyari_lineEdit.setEnabled(True)
            self.uyari_sesi_checkBox.setEnabled(True)
        else:
            self.erken_uyari_lineEdit.setEnabled(False)
            self.uyari_sesi_checkBox.setEnabled(False)
            self.uyari_sesi_checkBox.setChecked(False)
            
    def karakterKontrol(self):
        QtGui.QMessageBox.warning(self, "Hata", u"0 ve 99 arasında bir sayı girin.", "Kapat")
    
    def dosyaEkle(self, lineEdit):
        konum = QtGui.QFileDialog.getOpenFileName(self, u"Aç", "", u"Ses Dosyaları (*.mp3 *.ogg *.wma *.wav)")
        
        if len(konum) > 0:
            lineEdit.setText(konum)
    
    def sesDosyasiEkleSabah(self):
        self.dosyaEkle(self.sabah_lineEdit)
        
    def sesDosyasiEkleOgle(self):
        self.dosyaEkle(self.ogle_lineEdit)
        
    def sesDosyasiEkleIkindi(self):
        self.dosyaEkle(self.ikindi_lineEdit)
        
    def sesDosyasiEkleAksam(self):
        self.dosyaEkle(self.aksam_lineEdit)
        
    def sesDosyasiEkleYatsi(self):
        self.dosyaEkle(self.yatsi_lineEdit)
        
    def sesDosyasiEkleDua(self):
        self.dosyaEkle(self.dua_lineEdit)
        
    def sesDosyasiEkleUyari(self):
        self.dosyaEkle(self.uyari_lineEdit)
        
    def sesAyari(self):
        if self.volume == None:
            self.volume = self.audioOutput.volume()
            self.audioOutput.setVolume(0)
        else:
            self.audioOutput.setVolume(self.volume)
            self.volume = None
    
    def mutedAyari(self, volume):
        if volume == 0:
            self.audioOutput.setMuted(True)
        else:
            self.audioOutput.setMuted(False)
                               
    def saatiGuncelle(self):        
        self.saat = QtCore.QTime().currentTime().toString("hh:mm:ss")
        self.saat_label.setText("Saat: " + self.saat)
        
        self.tarih = QtCore.QDate().currentDate().toString("d MMMM yyyy")
        self.miladi_tarih.setText(self.tarih)
        
        if self.simdikiTarih != self.tarih:
            self.miladi_tarih.setText(self.tarih)
            self.simdikiTarih = self.tarih
            self.hicriTarihiGuncelle()
            self.vakitleriAl()
        
    def hicriTarihiGuncelle(self):       
        yil = int(QtCore.QDate().currentDate().toString("yyyy"))
        ay = int(QtCore.QDate().currentDate().toString("M"))
        gun = int(QtCore.QDate().currentDate().toString("d"))
        
        hicriAylar = ["Muharrem", "Safer", "Rebiülevvel", "Rebiülahir",
                      "Cemaziyelevvel", "Cemaziyelahir", "Recep", "Şaban",
                      "Ramazan", "Şevval", "Zilkade", "Zilhicce"]
        
        calverter = Calverter()
        jd = calverter.gregorian_to_jd(yil, ay, gun)
        hicri_tarih = calverter.jd_to_islamic(jd)
        
        hicriTarih = str(hicri_tarih[2]) + " " + str(hicriAylar[hicri_tarih[1] - 1]) + " " + str(hicri_tarih[0])
        
        self.hicri_tarih.setText(QtCore.QString.fromUtf8(hicriTarih))

    def labelTemizlik(self):
        self.ulke_label.clear()
        self.sehir_label.clear()
        Vakitler.saatler = ""
        self.namaz_vakti_label.clear()
        self.imsak_saat_label.clear()
        self.gunes_saat_label.clear()
        self.ogle_saat_label.clear()
        self.ikindi_saat_label.clear()
        self.aksam_saat_label.clear()
        self.yatsi_saat_label.clear()
        self.sonraki_vakit_label.clear()
        self.kalan_sure_label.clear()

    def bolgeselAyarlar(self):
        self.labelTemizlik()
        self.ilceler_comboBox.setEnabled(False)
        
        self.ulkeler_comboBox.currentIndexChanged.connect(self.sehirleriEkle)
            
        if self.kaynak_comboBox.currentText() == "diyanet.gov.tr":
            self.ulkeler_comboBox.clear()
            self.sehirler_comboBox.clear()
            self.vakitleri_aylik_al_checkBox.setEnabled(True)
            self.vakitleri_goster_pushButton.setEnabled(True)
            self.vakitleri_guncelle_pushButton.setEnabled(True)
            
            for ulke in self.ulkelerSehirlerDiyanet.ulkeler:
                self.ulkeler_comboBox.addItem(ulke)
                
            self.ulkeler_comboBox.setCurrentIndex(184)
        
        if self.kaynak_comboBox.currentText() == "zaman.com.tr":
            self.ulkeler_comboBox.clear()
            self.sehirler_comboBox.clear()
            self.vakitleri_aylik_al_checkBox.setChecked(False)
            self.vakitleri_aylik_al_checkBox.setEnabled(False)
            self.vakitleri_goster_pushButton.setEnabled(False)
            self.vakitleri_guncelle_pushButton.setEnabled(False)
            
            for ulke in sorted(self.ulkelerSehirlerZaman.ulkeler.keys()):
                self.ulkeler_comboBox.addItem(ulke)
            
            self.ulkeler_comboBox.setCurrentIndex(114)
            
        PyVakitci.kaynak = self.kaynak_comboBox.currentText()
    
    def ayarlar(self):
        self.gorunum = self.settings.value("Ayarlar/gorunum").toString()
        
        if len(self.gorunum) > 0:
            QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(self.gorunum))
        else:
            self.cleanlooksGorunumu()
        
        self.kaynak_comboBox.setCurrentIndex(self.settings.value("Ayarlar/kaynak").toInt()[0])
        self.ulkeler_comboBox.setCurrentIndex(self.settings.value("Ayarlar/ulke").toInt()[0])
        self.sehirler_comboBox.setCurrentIndex(self.settings.value("Ayarlar/sehir").toInt()[0])
        self.ilceler_comboBox.setCurrentIndex(self.settings.value("Ayarlar/ilce").toInt()[0])            
                    
        otomatikCalistir = self.settings.value("Ayarlar/otomatik_calistir").toInt()[0]
        if otomatikCalistir == 0:
            self.otomatik_calistir_checkBox.setChecked(False)
        if otomatikCalistir == 2:
            self.otomatik_calistir_checkBox.setChecked(True)
            self.otomatikCalistir()
            
        sistemTepsisindeBaslat = self.settings.value("Ayarlar/sistem_tepsisinde_baslat").toInt()[0]
        if sistemTepsisindeBaslat == 0:
            self.sistem_tepsisinde_baslat_checkBox.setChecked(False)
            self.show()
            
        if sistemTepsisindeBaslat == 2:
            self.sistem_tepsisinde_baslat_checkBox.setChecked(True)
        
        otomatikGuncelle = self.settings.value("Ayarlar/otomatik_guncelle").toInt()[0]
        if otomatikGuncelle == 0:
            self.otomatik_guncellestir_checkBox.setChecked(False)
        if otomatikGuncelle == 2:
            self.otomatik_guncellestir_checkBox.setChecked(True)
            
        herZamanUstte = self.settings.value("Ayarlar/her_zaman_ustte").toInt()[0]
        if herZamanUstte == 0:
            self.her_zaman_ustte_checkBox.setChecked(False)
        if herZamanUstte == 2:
            self.her_zaman_ustte_checkBox.setChecked(True)
            
        self.besmeleIleBasla = self.settings.value("Ayarlar/besmele_ile_basla").toInt()[0]
        if self.besmeleIleBasla == 0:
            self.besmele_ile_basla_checkBox.setChecked(False)
        if self.besmeleIleBasla == 2:
            self.besmele_ile_basla_checkBox.setChecked(True)
        
        ezanOku = self.settings.value("Ayarlar/ezan_oku").toInt()[0]
        if ezanOku == 0:
            self.ezan_oku_checkBox.setChecked(False)
        if ezanOku == 2:
            self.ezan_oku_checkBox.setChecked(True)
            
        duaOku = self.settings.value("Ayarlar/dua_oku").toInt()[0]
        if duaOku == 0:
            self.dua_oku_checkBox.setChecked(False)
        if duaOku == 2:
            self.dua_oku_checkBox.setChecked(True)
            
        erkenUyari = self.settings.value("Ayarlar/erken_uyari").toInt()[0]
        
        if erkenUyari == 0:
            self.erken_uyari_checkBox.setChecked(False)
        if erkenUyari == 2:
            self.erken_uyari_checkBox.setChecked(True)
            
        erkenUyariSuresi = self.settings.value("Ayarlar/erken_uyari_suresi").toString()
        self.erken_uyari_lineEdit.setText(erkenUyariSuresi)
        
        uyariSesiCal = self.settings.value("Ayarlar/uyari_sesi_cal").toInt()[0]
        if uyariSesiCal == 0:
            self.uyari_sesi_checkBox.setChecked(False)
        if (erkenUyari == 2) and (uyariSesiCal == 2):
            self.uyari_sesi_checkBox.setChecked(True)
        
        vakitleriAylikAl = self.settings.value("Ayarlar/vakitleri_aylik_al").toInt()[0]
        if vakitleriAylikAl == 0:
            self.vakitleri_aylik_al_checkBox.setChecked(False)
        if vakitleriAylikAl == 2:
            self.vakitleri_aylik_al_checkBox.setChecked(True)
            
            if QtCore.QFile.exists(PyVakitci.veritabaniDosyasi) == False:
                self.aylikVakitleriKaydet()
                
        sesAyari = self.settings.value("Ses_Ayarlari/ses_ayari").toFloat()[0]
        if type(sesAyari) == float:
            self.audioOutput.setVolume(sesAyari)
        
        sesDosyasiSabah = self.settings.value("Ses_Ayarlari/sabah").toString()
        self.sesDosyasiKontrol(self.sabah_lineEdit, sesDosyasiSabah)
        
        sesDosyasiOgle = self.settings.value("Ses_Ayarlari/ogle").toString()
        self.sesDosyasiKontrol(self.ogle_lineEdit, sesDosyasiOgle)
        
        sesDosyasiIkindi = self.settings.value("Ses_Ayarlari/ikindi").toString()
        self.sesDosyasiKontrol(self.ikindi_lineEdit, sesDosyasiIkindi)
        
        sesDosyasiAksam = self.settings.value("Ses_Ayarlari/aksam").toString()
        self.sesDosyasiKontrol(self.aksam_lineEdit, sesDosyasiAksam)
        
        sesDosyasiYatsi = self.settings.value("Ses_Ayarlari/yatsi").toString()
        self.sesDosyasiKontrol(self.yatsi_lineEdit, sesDosyasiYatsi)
        
        sesDosyasiDua = self.settings.value("Ses_Ayarlari/dua").toString()
        self.sesDosyasiKontrol(self.dua_lineEdit, sesDosyasiDua)
        
        sesDosyasiUyari = self.settings.value("Ses_Ayarlari/uyari").toString()
        self.sesDosyasiKontrol(self.uyari_lineEdit, sesDosyasiUyari)
            
    def sesDosyasiKontrol(self, lineEdit, sesDosyasi):
        if len(sesDosyasi) > 0:
            lineEdit.setText(sesDosyasi)
                    
    def varsayilanAyarlar(self):
        self.labelTemizlik()
        
        self.ulkeler_comboBox.setCurrentIndex(-1)
        
        self.settings = QtCore.QSettings(self.ontanimliAyarDosyasi, QtCore.QSettings.IniFormat)
        
        if QtCore.QFile.exists(QtCore.QFile(self.ontanimliAyarDosyasi)):
            if QtCore.QFile.exists(QtCore.QFile(self.ayarDosyasi)):
                QtCore.QFile(self.ayarDosyasi).remove()
            
            self.ayarlar()
                
    def sesVarsayilanAyarlar(self):
        self.sabah_lineEdit.setText(self.sesDosyalariKonum + "sabah_saba.ogg")
        self.ogle_lineEdit.setText(self.sesDosyalariKonum + "ogle_rast.ogg")
        self.ikindi_lineEdit.setText(self.sesDosyalariKonum + "ikindi_hicaz.ogg")
        self.aksam_lineEdit.setText(self.sesDosyalariKonum + "aksam_segah.ogg")
        self.yatsi_lineEdit.setText(self.sesDosyalariKonum + "yatsi_ussak.ogg")
        self.dua_lineEdit.setText(self.sesDosyalariKonum + "ezan_duasi.ogg")
        self.uyari_lineEdit.setText(self.sesDosyalariKonum + "uyari.ogg")

    def ayarlariUygula(self):
        if QtCore.QFile.exists(QtCore.QFile(self.ayarDosyasi)) != False:
            self.settings = QtCore.QSettings(self.ayarDosyasi, QtCore.QSettings.IniFormat)
            
            self.ayarlar()
            
            if self.besmeleIleBasla == 2:
                self.besmeleyleBasla()
            
            self.vakitleriAl()
        else:
            self.sesVarsayilanAyarlar()
            self.varsayilanAyarlar()
    
    def ayarlariKaydet(self):
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        
        self.calismaDizininiHazirla()
        
        self.settings = QtCore.QSettings(self.ayarDosyasi, QtCore.QSettings.IniFormat)
        
        self.settings.setValue("Ayarlar/gorunum", self.gorunum)
        self.settings.setValue("Ayarlar/ulke", self.ulkeler_comboBox.currentIndex())
        self.settings.setValue("Ayarlar/sehir", self.sehirler_comboBox.currentIndex())
        self.settings.setValue("Ayarlar/ilce", self.ilceler_comboBox.currentIndex())
        self.settings.setValue("Ayarlar/kaynak", self.kaynak_comboBox.currentIndex())
        self.settings.setValue("Ayarlar/otomatik_calistir", self.otomatik_calistir_checkBox.checkState())
        self.otomatikCalistir()
        self.settings.setValue("Ayarlar/sistem_tepsisinde_baslat", self.sistem_tepsisinde_baslat_checkBox.checkState())
        self.settings.setValue("Ayarlar/otomatik_guncelle", self.otomatik_calistir_checkBox.checkState())
        self.otomatikGuncellestir()
        self.settings.setValue("Ayarlar/her_zaman_ustte", self.her_zaman_ustte_checkBox.checkState())
        self.settings.setValue("Ayarlar/besmele_ile_basla", self.besmele_ile_basla_checkBox.checkState())
        self.settings.setValue("Ayarlar/ezan_oku", self.ezan_oku_checkBox.checkState())
        self.settings.setValue("Ayarlar/dua_oku", self.dua_oku_checkBox.checkState())
        self.settings.setValue("Ayarlar/erken_uyari", self.erken_uyari_checkBox.checkState())
        self.settings.setValue("Ayarlar/erken_uyari_suresi", self.erken_uyari_lineEdit.text())
        self.settings.setValue("Ayarlar/uyari_sesi_cal", self.uyari_sesi_checkBox.checkState())
        self.settings.setValue("Ayarlar/vakitleri_aylik_al", self.vakitleri_aylik_al_checkBox.checkState())
        self.settings.setValue("Ses_Ayarlari/sabah", self.sabah_lineEdit.text())
        self.settings.setValue("Ses_Ayarlari/ogle", self.ogle_lineEdit.text())
        self.settings.setValue("Ses_Ayarlari/ikindi", self.ikindi_lineEdit.text())
        self.settings.setValue("Ses_Ayarlari/aksam", self.aksam_lineEdit.text())
        self.settings.setValue("Ses_Ayarlari/yatsi", self.yatsi_lineEdit.text())
        self.settings.setValue("Ses_Ayarlari/dua", self.dua_lineEdit.text())
        self.settings.setValue("Ses_Ayarlari/uyari", self.uyari_lineEdit.text())
        self.settings.setValue("Ses_Ayarlari/ses_ayari", self.audioOutput.volume())
        
        PyVakitci.vakitleriAlCheckBox = self.vakitleri_aylik_al_checkBox
        
        self.hicriTarihiGuncelle()
        self.vakitleriAl()
    
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)
        
        QtGui.QMessageBox.information(self, "Bilgilendirme", u"Ayarlar kaydedildi.", "Kapat")
            
    def vakitleriAl(self):
        self.labelTemizlik()
        
        self.ulkeAdi = self.ulke_label.setText(self.ulkeler_comboBox.currentText())
        self.sehirAdi = self.sehir_label.setText(self.sehirler_comboBox.currentText())
        
        if self.ulkeKontrolu():
            PyVakitci.veriler['sehirler'] = self.ilceler_comboBox.currentText()
        else:
            PyVakitci.veriler['sehirler'] = self.sehirler_comboBox.currentText()
                    
        PyVakitci.veriler['ulk'] = self.ulkeler_comboBox.currentText()
        
        if self.vakitleri_aylik_al_checkBox.isChecked():
            PyVakitci.veriler['R1'] = "AYLIK"
        else:
            PyVakitci.veriler['R1'] = "HAFTALIK"
        
        Vakitler.ulke = self.ulkeler_comboBox.currentText()
        Vakitler.sehir = PyVakitci.veriler['sehirler']
        
        PyVakitci.kaynak = self.kaynak_comboBox.currentText()
        
        if self.ulkeler_comboBox.currentIndex() >= 0:
            if self.sehirler_comboBox.currentIndex() >= 0:                
                if PyVakitci.rlock._is_owned() == False:
                    vakitler = Vakitler()
                    vakitler.start()
        
        self.timerLabel = QtCore.QTimer()
        self.connect(self.timerLabel, QtCore.SIGNAL("timeout()"), self.labelGuncelle)
        self.timerLabel.start(500)
        
    def labelGuncelle(self):
        self.saat = QtCore.QTime().currentTime().toString("hh:mm")
        
        if len(Vakitler.saatler) != 0:
            
            if self.kaynak_comboBox.currentText() == "diyanet.gov.tr":
                self.statusbar.showMessage("Kaynak: " + PyVakitci.kaynak)
                
            if self.kaynak_comboBox.currentText() == "zaman.com.tr":
                self.statusbar.showMessage("Kaynak: zaman.com.tr")
            try:
                if "00:00" <= self.saat < Vakitler.imsak:
                    self.labelVeriler(Vakitler.imsak, Vakitler.gunes, Vakitler.ogle, Vakitler.ikindi,
                                      Vakitler.aksam, "<font color='#FF0000'>" + Vakitler.yatsi + "</font>",
                                      u"Şimdi Yatsı Vakti", u"İmsak'a Kalan Süre :", u"yatsı")
    
                if Vakitler.imsak <= self.saat < Vakitler.gunes:
                    self.labelVeriler("<font color='#FF0000'>" + Vakitler.imsak + "</font>", Vakitler.gunes,
                                      Vakitler.ogle, Vakitler.ikindi, Vakitler.aksam, Vakitler.yatsi,
                                      u"Şimdi İmsak Vakti", u"Güneş'e Kalan Süre :", "sabah")
                    
                    self.vakitKontrol(self.sabah_lineEdit.text(), self.imsak_saat_label.text(), "sabah")
                    
                if Vakitler.gunes <= self.saat < Vakitler.ogle:
                    self.labelVeriler(Vakitler.imsak, "<font color='#FF0000'>" + Vakitler.gunes + "</font>",
                                      Vakitler.ogle, Vakitler.ikindi, Vakitler.aksam, Vakitler.yatsi,
                                      u"Şimdi Güneş Vakti", u"Öğle'ye Kalan Süre :", u"güneş")
                    
                if Vakitler.ogle <= self.saat < Vakitler.ikindi:
                    self.labelVeriler(Vakitler.imsak, Vakitler.gunes, "<font color='#FF0000'>" + Vakitler.ogle + "</font>",
                                      Vakitler.ikindi, Vakitler.aksam, Vakitler.yatsi, u"Şimdi Öğle Vakti",
                                      u"İkindi'ye Kalan Süre :", u"öğle")
                    
                    self.vakitKontrol(self.ogle_lineEdit.text(), self.ogle_saat_label.text(), u"öğle")
                    
                if Vakitler.ikindi <= self.saat < Vakitler.aksam:
                    self.labelVeriler(Vakitler.imsak, Vakitler.gunes, Vakitler.ogle,
                                      "<font color='#FF0000'>" + Vakitler.ikindi + "</font>", Vakitler.aksam,
                                      Vakitler.yatsi, u"Şimdi İkindi Vakti", u"Akşam'a Kalan Süre :", "ikindi")
                    
                    self.vakitKontrol(self.ikindi_lineEdit.text(), self.ikindi_saat_label.text(), "ikindi")
                    
                if Vakitler.aksam <= self.saat < Vakitler.yatsi:
                    self.labelVeriler(Vakitler.imsak, Vakitler.gunes, Vakitler.ogle, Vakitler.ikindi,
                                      "<font color='#FF0000'>" + Vakitler.aksam + "</font>", Vakitler.yatsi,
                                      u"Şimdi Akşam Vakti", u"Yatsı'ya Kalan Süre :", u"akşam")
                    
                    self.vakitKontrol(self.aksam_lineEdit.text(), self.aksam_saat_label.text(), u"akşam")
                    
                if Vakitler.yatsi <= self.saat <= "23:59":
                    self.labelVeriler(Vakitler.imsak, Vakitler.gunes, Vakitler.ogle, Vakitler.ikindi,
                                      Vakitler.aksam, "<font color='#FF0000'>" + Vakitler.yatsi + "</font>",
                                      u"Şimdi Yatsı Vakti", u"İmsak'a Kalan Süre :", u"yatsı")
                    
                    self.vakitKontrol(self.yatsi_lineEdit.text(), self.yatsi_saat_label.text(), u"yatsı")
            except ValueError:
                pass
            
        else:
            if (self.vakitleri_aylik_al_checkBox.isChecked()) and (Vakitler.tarihHatasi == True):
                self.timerLabel.stop()
                self.statusbar.clearMessage()
                QtGui.QMessageBox.warning(self, u"Tarih Hatası", u"Sisteminizin tarihi yanlış. Tarihi düzelttikten sonra veya \"Vakitleri aylık olarak " +
                                          u"al.\" seçeneğinin işaretini kaldırdıktan sonra Ayarlar sekmesindeki Kaydet butonuna tıklayın veya programı tekrar çalıştırın.",
                                          "Kapat")

        if (SiteyeBaglan.baglantiVarmi == False) and (Vakitler.baglantiSorunu == True):
            self.timerLabel.stop()
            self.statusbar.clearMessage()

            soru = QtGui.QMessageBox.question(self, u'Bağlantı Hatası',
                                    u"Şehirler seçtiğiniz kaynaktan alınamadı. " +
                                    u"Kullandığınız kaynağı değiştirmek sorunu giderebilir.<br><br>" +
                                    u"Vakitler veritabanında varsa oradan alınsın mı?<br><br>" +
                                    u"Not: Soruya evet cevabını verirseniz \"Vakitleri aylık olarak al.\" seçeneği seçilecek.",
                                    QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if soru == QtGui.QMessageBox.Yes:
                self.vakitleri_aylik_al_checkBox.setChecked(True)
                if Vakitler.baglantiSorunu:
                    Vakitler.baglantiSorunu = False
                    self.settings.setValue("Ayarlar/vakitleri_aylik_al", self.vakitleri_aylik_al_checkBox.checkState())
                    self.vakitleriAl()
        
        if self.vakitleri_aylik_al_checkBox.isChecked():
            if Vakitler.veritabanindakiYerBilgisi == False:
                if self.timerLabel.isActive():
                    self.timerLabel.stop()
    
                soru = QtGui.QMessageBox.question(self, u"Veritabanı Güncel Değil",
                                                  u"Veritabanındaki İlçe/Şehir bilgisiyle programdaki İlçe/Şehir " +
                                                  u"bilgisi uyuşmuyor. Veritabanı programdaki bilgilere göre güncellensin mi?<br><br>" +
                                                  u"Programdaki İlçe/Şehir: " + Vakitler.sehir + "<br>"
                                                  u"Veritanındaki İlçe/Şehir: " + Vakitler.veritabanindakiYer,
                                                  QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
    
                if soru == QtGui.QMessageBox.Yes:
                    self.statusbar.showMessage(u"Vakitler güncelleniyor...")
                    self.aylikVakitleriKaydet()
                    self.vakitleriAl()
                
    def labelVeriler(self, imsak, gunes, ogle, ikindi, aksam, yatsi, namazvakti, sonrakivakit, simdikivakit):
        self.imsak_saat_label.setText(imsak)
        self.gunes_saat_label.setText(gunes)
        self.ogle_saat_label.setText(ogle)
        self.ikindi_saat_label.setText(ikindi)
        self.aksam_saat_label.setText(aksam)
        self.yatsi_saat_label.setText(yatsi)
        self.namaz_vakti_label.setText(namazvakti)
        self.namazvakti = namazvakti
        self.sonraki_vakit_label.setText(sonrakivakit)
        self.kalanSureKontrol(simdikivakit)

    def kalanSureKontrol(self, vakit):
        simdikiZaman = QtCore.QTime().currentTime()
        simdikiSaat = int(simdikiZaman.toString("hh"))
        simdikiDakika = int(simdikiZaman.toString("mm"))
        self.simdikiSaniye = int(simdikiZaman.toString("ss"))
                
        if vakit == "sabah":
            gunes = str(self.gunes_saat_label.text())
            gunesSaat = int(gunes[:gunes.find(":")].replace("<font color='#FF0000'>", ""))
            gunesDakika = int(gunes[gunes.find(":") + 1:].replace("</font>", ""))
            
            self.toplamDakika = (gunesSaat * 60 + gunesDakika) - (simdikiSaat * 60 + simdikiDakika)
            self.kalanSureyiHesapla()
            self.erkenUyariKontrol(self.toplamDakika)
            
        if vakit == u"güneş":
            ogle = str(self.ogle_saat_label.text())
            ogleSaat = int(ogle[:ogle.find(":")].replace("<font color='#FF0000'>", ""))
            ogleDakika = int(ogle[ogle.find(":") + 1:].replace("</font>", ""))
            
            self.toplamDakika = (ogleSaat * 60 + ogleDakika) - (simdikiSaat * 60 + simdikiDakika)
            self.kalanSureyiHesapla()
            self.erkenUyariKontrol(self.toplamDakika)
        
        if vakit == u"öğle":
            ikindi = str(self.ikindi_saat_label.text())
            ikindiSaat = int(ikindi[:ikindi.find(":")].replace("<font color='#FF0000'>", ""))
            ikindiDakika = int(ikindi[ikindi.find(":") + 1:].replace("</font>", ""))
            
            self.toplamDakika = (ikindiSaat * 60 + ikindiDakika) - (simdikiSaat * 60 + simdikiDakika)
            self.kalanSureyiHesapla()
            self.erkenUyariKontrol(self.toplamDakika)
            
        if vakit == "ikindi":
            aksam = str(self.aksam_saat_label.text())
            aksamSaat = int(aksam[:aksam.find(":")].replace("<font color='#FF0000'>", ""))
            aksamDakika = int(aksam[aksam.find(":") + 1:].replace("</font>", ""))
            
            self.toplamDakika = (aksamSaat * 60 + aksamDakika) - (simdikiSaat * 60 + simdikiDakika)
            self.kalanSureyiHesapla()
            self.erkenUyariKontrol(self.toplamDakika)
            
        if vakit == u"akşam":
            yatsi = str(self.yatsi_saat_label.text())
            yatsiSaat = int(yatsi[:yatsi.find(":")].replace("<font color='#FF0000'>", ""))
            yatsiDakika = int(yatsi[yatsi.find(":") + 1:].replace("</font>", ""))
            
            self.toplamDakika = (yatsiSaat * 60 + yatsiDakika) - (simdikiSaat * 60 + simdikiDakika)
            self.kalanSureyiHesapla()
            self.erkenUyariKontrol(self.toplamDakika)

        if vakit == u"yatsı":
            imsak = str(self.imsak_saat_label.text())
            imsakSaat = int(imsak[:imsak.find(":")].replace("<font color='#FF0000'>", ""))
            imsakDakika = int(imsak[imsak.find(":") + 1:].replace("</font>", ""))
            
            if imsakSaat >= simdikiSaat >= 0:
                self.toplamDakika = (imsakSaat * 60 + imsakDakika) - (simdikiSaat * 60 + simdikiDakika)
                self.erkenUyariKontrol(self.toplamDakika)
            else:
                self.toplamDakika = (24 * 60) - (simdikiSaat * 60 + simdikiDakika) + (imsakSaat * 60 + imsakDakika)
                self.erkenUyariKontrol(self.toplamDakika)
                
            self.kalanSureyiHesapla()
            
    def kalanSureyiHesapla(self):
        if self.toplamDakika <= 60 :
            kalanSaat = "00"
        else:
            kalanSaat = "0" + str(self.toplamDakika / 60)
        
        if (self.toplamDakika - (self.toplamDakika / 60) * 60 - 1) >= 10:
            kalanDakika = ":" + str(self.toplamDakika - (self.toplamDakika / 60) * 60 - 1)
        else:
            if (self.toplamDakika - (self.toplamDakika / 60) * 60 - 1) == 60:
                kalanDakika = ":0" + str(0)
            else:
                if (self.toplamDakika - (self.toplamDakika / 60) * 60) == 0:
                    kalanDakika = ":59"
                else:
                    kalanDakika = ":0" + str(self.toplamDakika - (self.toplamDakika / 60) * 60 - 1)
        
        if 60 - self.simdikiSaniye == 60:
            kalanSaniye = ":0" + str(0)
        else:
            if 60 - self.simdikiSaniye >= 10:
                kalanSaniye = ":" + str(60 - self.simdikiSaniye)
            else:
                kalanSaniye = ":0" + str(60 - self.simdikiSaniye)
        
        kalanSure = kalanSaat + kalanDakika + kalanSaniye
        self.kalan_sure_label.setText(kalanSure)
        
    def erkenUyariKontrol(self, toplamDakika):        
        try:
            if toplamDakika == int(self.erken_uyari_lineEdit.text()):
                if self.erken_uyari_checkBox.isChecked():
                    if self.mesajGosterildi == False:
                        self.trayIcon.showMessage(u"Erken Uyarı",
                                                  self.sonraki_vakit_label.text() + " " + str(toplamDakika) + " Dakika",
                                                  self.trayIcon.Information, 15000)
                        self.mesajGosterildi = True
                        
                        if self.uyari_sesi_checkBox.isChecked():
                            self.mediaNesnesi.setCurrentSource(Phonon.MediaSource(self.uyari_lineEdit.text()))
                            
                            try:
                                self.mediaNesnesi.stop()
                            except:
                                pass
                            
                            self.mediaNesnesi.play()
                            
                        self.timerMesaj()
        except:
            pass
            
    def vakitKontrol(self, dosya, labelsaat, simdikivakit):
        try:
            ara = re.search(">(.*):(.*)<", labelsaat)
            saat = ara.group(1) + ":" + ara.group(2)
            
            if saat == self.saat:
                if self.mesajGosterildi == False:
                    self.vakitleriGoster(3000)
                    self.mesajGosterildi = True
                    
                    if self.ezan_oku_checkBox.isChecked():
                        self.ezanOku(dosya)
                    
                    try:
                        self.timerMesaj()
                    except TypeError:
                        pass
        except:
            pass
                
    def timerMesaj(self):
        self.timerMesaj = QtCore.QTimer()
        self.connect(self.timerMesaj, QtCore.SIGNAL("timeout()"), self.mesajGosterimKontrol)
        self.timerMesaj.start(60000)
                
    def mesajGosterimKontrol(self):
        self.mesajGosterildi = False
        self.timerMesaj.stop()
    
    def ezanOku(self, dosya):        
        self.mediaNesnesi.setCurrentSource(Phonon.MediaSource(dosya))
        
        try:
            self.mediaNesnesi.stop()
        except:
            pass
        
        self.mediaNesnesi.play()
        self.mediaNesnesi.finished.connect(self.ezanDuasiniOku)

    def ezanDuasiniOku(self):
        if self.dua_oku_checkBox.isChecked():
            self.mediaNesnesi.setCurrentSource(Phonon.MediaSource(self.dua_lineEdit.text()))
            
            try:
                self.mediaNesnesi.stop()
            except:
                pass
            
            self.mediaNesnesi.play()
            self.mediaNesnesi.finished.connect(self.mediaNesnesi.stop)
            
    def ulkeKontrolu(self):
        secilenUlke = self.ulkeler_comboBox.currentText()
        
        if self.kaynak_comboBox.currentText() == "diyanet.gov.tr":
            if (secilenUlke == "ABD") or (secilenUlke == "KANADA") or (secilenUlke == "TURKIYE"):
                return True
            
    def ilceleriEkle(self):
        self.ilceler_comboBox.clear()
        
        ilceler_comboBox = self.ilceler_comboBox
        secilenUlke = self.ulkeler_comboBox.currentText()
        secilenSehir = self.sehirler_comboBox.currentText()
        
        if self.ulkeKontrolu():
            self.ilceler_comboBox.setEnabled(True)
            self.diyanetSehirler.ilceleriEkle(ilceler_comboBox, secilenUlke, secilenSehir)
        else:
            self.ilceler_comboBox.setEnabled(False)

    def sehirleriEkle(self):
        self.sehirler_comboBox.clear()
        secilenUlke = self.ulkeler_comboBox.currentText()
        sehirler_comboBox = self.sehirler_comboBox
        
        self.sehirler_comboBox.currentIndexChanged.connect(self.ilceleriEkle)
        
        if PyVakitci.kaynak == "diyanet.gov.tr":
            self.diyanetSehirler = DiyanetSehirler()
            self.diyanetSehirler.sehirleriEkle(sehirler_comboBox, secilenUlke)
        
        if PyVakitci.kaynak == "zaman.com.tr":
            zamanSehirler = ZamanSehirler()
            zamanSehirler.sehirleriEkle(sehirler_comboBox, secilenUlke)
        
        self.sehirler_comboBox.setCurrentIndex(-1)
        
        if self.ulkeKontrolu():
            if (secilenUlke == "ABD") or (secilenUlke == "KANADA"):
                self.bolgesel_ayarlar_sehir_label.setText(u"Eyalet:")
                self.bolgesel_ayarlar_ilce_label.setText(u"Şehir:")
            else:
                self.bolgesel_ayarlar_sehir_label.setText(u"Şehir:")
                self.bolgesel_ayarlar_ilce_label.setText(u"İlçe:")
        else:
            self.bolgesel_ayarlar_sehir_label.setText(u"Şehir:")
            self.bolgesel_ayarlar_ilce_label.setText(u"İlçe:")
                        
    def vakitleriGoster(self, gosterimSuresi):
        if gosterimSuresi == False:
            gosterimSuresi = 4000
        
        self.trayIcon.showMessage("", self.ilceler_comboBox.currentText() + u"\n\n" +
                                  self.namazvakti.replace(u"Şimdi ", "") + "\n"
                                  u"\nİmsak:\t" + Vakitler.imsak + 
                                  u"\nGüneş:\t" + Vakitler.gunes + 
                                  u"\nÖğle:\t" + Vakitler.ogle + 
                                  u"\nİkindi:\t" + Vakitler.ikindi + 
                                  u"\nAkşam:\t" + Vakitler.aksam + 
                                  u"\nYatsı:\t" + Vakitler.yatsi,
                                  self.trayIcon.Information, gosterimSuresi)
        
    def vakitleriTopluGoster(self):
        from moduller.Vakitler import AylikVakitler
        AylikVakitler(PyVakitci.veritabaniDosyasi, self.statusbar)
        
        if (self.vakitleri_aylik_al_checkBox.isChecked()) and (Vakitler.tarihHatasi == True):
            self.timerLabel.stop()
            self.statusbar.clearMessage()
            QtGui.QMessageBox.warning(self, u"Tarih Hatası", u"Sisteminizin tarihi yanlış. Tarihi düzelttikten sonra veya \"Vakitleri aylık olarak " +
                                      u"al.\" seçeneğinin işaretini kaldırdıktan sonra Ayarlar sekmesindeki Kaydet butonuna tıklayın veya programı tekrar çalıştırın.",
                                      "Kapat")
        
        if AylikVakitler.veritabaniVarmi == False:
            self.aylikVakitleriKaydet()
            AylikVakitler(PyVakitci.veritabaniDosyasi, self.statusbar)
        
    def aylikVakitleriKaydet(self):
        simdikiSaat = int(QtCore.QTime().currentTime().toString("hh"))
        
        if 1 <= simdikiSaat <= 22:
        
            self.statusbar.showMessage(u"Vakitler güncelleniyor...")
            
            QtGui.QApplication.setOverrideCursor(QtCore.Qt.BusyCursor)
            
            siteyeBaglan = SiteyeBaglan("http://www.diyanet.gov.tr")
            siteyeBaglan.start()
            
            # Siteye SiteyeBaglan sınıfındaki try bloğundaki 
            # kodla 7 sn içinde bağlanılamazsa 
            # except bloğundaki kod devreye girecek.
            
            siteyeBaglan.join(7) # timeout = 7 sn 
            
            if siteyeBaglan.baglantiVarmi:
                vakitler = Vakitler()
                
                ulke = self.ulkeler_comboBox.currentText()
    
                if self.ulkeKontrolu():
                    if ulke == "TURKIYE":
                        vakitler.aylikVakitleriKaydet("İlçe")
                    else:
                        vakitler.aylikVakitleriKaydet("Şehir")
                else:
                    vakitler.aylikVakitleriKaydet("Şehir")
                
            else:
                self.statusbar.clearMessage()
                QtGui.QMessageBox.warning(self, u"Bağlantı Hatası",
                                          u"İnternet bağlantınız olmadığından veya siteye bağlantı kurulamadığından " + 
                                          u"dolayı namaz vakitleri veritabanı güncellenemedi.", "Kapat")
                
            QtGui.QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)

            self.vakitleriAl()
        else:
            QtGui.QMessageBox.information(self, "Bilgilendirme",
                                          u"Saat 1 ve 23 arasında güncelleme yapılabilmektedir.", "Kapat")
            
            self.vakitleri_aylik_al_checkBox.setChecked(False)
            self.vakitleriAl()
        
    def lisans(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.lisansDosyasi))
            
    def hakkindaDialog(self):
        from moduller.Hakkinda import Hakkinda
        dialog = Hakkinda()
        dialog.exec_()
        
    # Program kapatıldığında system tray'da çalışır.
    def closeEvent(self, event):
        event.ignore()
        
        if self.trayIcon.isVisible():
            self.setVisible(False)
        else: 
            self.trayIcon.show()
            self.setVisible(False)

class SiteyeBaglan(threading.Thread):
    baglantiVarmi = False
    
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    
    def run(self):
        try:
            site = urllib.urlopen(self.url)
            SiteyeBaglan.baglantiVarmi = True
        except:
            print self.url + u" sitesine bağlantı yok."
            SiteyeBaglan.baglantiVarmi = False
            
class Vakitler(threading.Thread):
    baglantiSorunu = None
    simdikiTarih = None
    saatler = None
    imsak = None
    gunes = None
    ogle = None
    ikindi = None
    aksam = None
    yatsi = None
    ulke = None
    sehir = None
    tarihHatasi = None
    veritabanindakiYerBilgisi = None
    veritabanindakiYer = None
    
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):        
        PyVakitci.rlock.acquire()
        
        Vakitler.saatler = ""
        Vakitler.imsak = ""
        Vakitler.gunes = ""
        Vakitler.ogle = ""
        Vakitler.ikindi = ""
        Vakitler.aksam = ""
        Vakitler.yatsi = ""
        Vakitler.simdikiTarih = QtCore.QDate().currentDate().toString("dd.MM.yyyy")
        Vakitler.vakitleriAlCheckBox = None
        
        ulke = PyVakitci.veriler['ulk']
        sehir = PyVakitci.veriler['sehirler']
        
        if PyVakitci.veriler["R1"] == "HAFTALIK":
            if PyVakitci.kaynak == "diyanet.gov.tr":
                siteyeBaglan = SiteyeBaglan("http://www.diyanet.gov.tr")
                siteyeBaglan.start()
                siteyeBaglan.join(7)
                
                if siteyeBaglan.baglantiVarmi:
                    try:
                        url = "http://www.diyanet.gov.tr/turkish/namazvakti/vakithes_namazsonuc.asp"
                        veriler = urllib.urlencode(PyVakitci.veriler)
                        
                        site = urllib.urlopen(url, veriler)
                        html = site.read(12000)
                        
                        derle = re.compile("[1-2]*[0-9]\s[0-5][0-9]")
                            
                        Vakitler.saatler = derle.findall(html)
                        
                        Vakitler.imsak = "0" + Vakitler.saatler[0].replace(" ", ":")
                        Vakitler.gunes = "0" + Vakitler.saatler[1].replace(" ", ":")
                        Vakitler.ogle = Vakitler.saatler[2].replace(" ", ":")
                        Vakitler.ikindi = Vakitler.saatler[3].replace(" ", ":")
                        Vakitler.aksam = Vakitler.saatler[4].replace(" ", ":")
                        Vakitler.yatsi = Vakitler.saatler[5].replace(" ", ":")
                    except:
                        pass
                else:
                    siteyeBaglan = SiteyeBaglan("http://www.diyanettakvimi.com")
                    siteyeBaglan.start()
                    siteyeBaglan.join(7)
                    
                    if siteyeBaglan.baglantiVarmi:
                        try:
                            PyVakitci.kaynak = "diyanettakvimi.com"
                            
                            url = str("http://www.diyanettakvimi.com/" + ulke.replace(" ", "-") + \
                                      "/" + sehir.replace(" ", "-") + "-ezan-vakti.html")
                            site = urllib.urlopen(url)
                            html = site.read(8000)
                            
                            metin = 'td align=center class="im3">(.*?)</td><td align=center class="im3">(.*?)</td>' + \
                            '<td align=center class="im3">(.*?)</td><td align=center class="im3">(.*?)</td>' + \
                            '<td align=center class="im3">(.*?)</td><td align=center class="im3">(.*?)</td>'
                            
                            veriler = re.search(metin, html).groups()
                            Vakitler.saatler = veriler
                            
                            Vakitler.imsak = Vakitler.saatler[0]
                            Vakitler.gunes = Vakitler.saatler[1]
                            Vakitler.ogle = Vakitler.saatler[2]
                            Vakitler.ikindi = Vakitler.saatler[3]
                            Vakitler.aksam = Vakitler.saatler[4]
                            Vakitler.yatsi = Vakitler.saatler[5]
                        except:
                            pass
                    else:
                        Vakitler.baglantiSorunu = True
            
            if PyVakitci.kaynak == "zaman.com.tr":
                siteyeBaglan = SiteyeBaglan("http://www.zaman.com.tr")
                siteyeBaglan.start()
                siteyeBaglan.join(7)
                
                if siteyeBaglan.baglantiVarmi:
                    try:
                        urlencode = urllib.urlencode({'country': ZamanUlkelerSehirler.ulkeler[str(ulke)], 
                                                      'city': eval("ZamanUlkelerSehirler." + str(ulke) + "[str(sehir)]"), 
                                                      'type' : 'daily'})
                        site = urllib.urlopen("http://zaman.com.tr/namaz.do", urlencode)
                        veri = site.read(45000)
                        
                        derle = re.compile('<td align="center">(.*?)</td>')                    
                        Vakitler.saatler = derle.findall(veri)
                        
                        Vakitler.imsak = Vakitler.saatler[0]
                        Vakitler.gunes = Vakitler.saatler[1]
                        Vakitler.ogle = Vakitler.saatler[2]
                        Vakitler.ikindi = Vakitler.saatler[3]
                        Vakitler.aksam = Vakitler.saatler[4]
                        Vakitler.yatsi = Vakitler.saatler[5]
                    except:
                        pass
                else:
                    Vakitler.baglantiSorunu = True
        
        if PyVakitci.veriler["R1"] == "AYLIK":
            if QtCore.QFile.exists(PyVakitci.veritabaniDosyasi):
                
                connect = sqlite3.connect(PyVakitci.veritabaniDosyasi)
                cursor = connect.cursor()
                
                try:                    
                    cursor.execute("SELECT " + self.ilceSehirKontrolu() + " FROM namazvakitleri")
                    yerBilgisi = str(cursor.fetchone())
                    
                    yerBilgisi = yerBilgisi[3:yerBilgisi.rfind("'")]
                                    
                    if yerBilgisi == sehir:                                        
                        try:
                            cursor.execute("SELECT Tarih FROM namazvakitleri")
                            
                            veriler = cursor.fetchall()
                            
                            tarihler = []
                            vakitler = []
                            
                            for tarih in veriler:
                                tarihler.append(str(tarih[0]))
                            
                            if tarihler.count(self.simdikiTarih) == 1:
                                cursor.execute("SELECT İmsak, Güneş, Öğle, İkindi, Akşam, Yatsı FROM namazvakitleri WHERE tarih = '" + str(self.simdikiTarih) + "'")
                                veriler = cursor.fetchone()
                                
                                for vakit in veriler:
                                    vakitler.append(str(vakit))
                                
                                Vakitler.saatler = vakitler
                                Vakitler.imsak = vakitler[0]
                                Vakitler.gunes = vakitler[1]
                                Vakitler.ogle = vakitler[2]
                                Vakitler.ikindi = vakitler[3]
                                Vakitler.aksam = vakitler[4]
                                Vakitler.yatsi = vakitler[5]
                                Vakitler.tarihDogrumu = True
                            else:
                                Vakitler.tarihDogrumu = False
                                
                                siteyeBaglan = SiteyeBaglan("http://www.diyanet.gov.tr")
                                siteyeBaglan.start()
                                siteyeBaglan.join(7)
                                
                                if siteyeBaglan.baglantiVarmi:
                                    self.aylikVakitleriKaydet(self.ilceSehirKontrolu())
                            
                            Vakitler.veritabanindakiYerBilgisi = True
                            Vakitler.veritabanindakiYer = yerBilgisi
                            
                        except sqlite3.OperationalError:
                            self.aylikVakitleriKaydet(self.ilceSehirKontrolu())
                            self.run()
                        
                        Vakitler.veritabanindakiYerBilgisi = True
                        Vakitler.veritabanindakiYer = yerBilgisi
                    else:
                        Vakitler.veritabanindakiYerBilgisi = False
                        Vakitler.veritabanindakiYer = yerBilgisi
                except sqlite3.OperationalError:
                    self.aylikVakitleriKaydet(self.ilceSehirKontrolu())
                    self.run()
                        
            else:
                siteyeBaglan = SiteyeBaglan("http://www.diyanet.gov.tr")
                siteyeBaglan.start()
                siteyeBaglan.join(7)
                
                if siteyeBaglan.baglantiVarmi:
                    self.aylikVakitleriKaydet(self.ilceSehirKontrolu())
                    self.run()
                    
        PyVakitci.rlock.release()
        
    def ilceSehirKontrolu(self):
        if PyVakitci.kaynak == "diyanet.gov.tr":
            if Vakitler.ulke == "TURKIYE":
                return "İlçe"
            else:
                return "Şehir"
        else:
            return "Şehir"
        
    def aylikVakitleriKaydet(self, ilceSehir):
        simdikiSaat = int(QtCore.QTime().currentTime().toString("hh"))
        
        if 1 <= simdikiSaat <= 22:
            if QtCore.QFile.exists(PyVakitci.veritabaniDosyasi):
                QtCore.QFile(PyVakitci.veritabaniDosyasi).remove()
            
            connect = sqlite3.connect(PyVakitci.veritabaniDosyasi)
            cursor = connect.cursor()
            
            sqlString = "DROP TABLE namazvakitleri" 
            
            try:
                try:
                    cursor.execute(sqlString)
                except sqlite3.OperationalError:
                    pass
                    #print u"Silmeye çalıştığın namazvakitleri tablosu yok."
                
                sqlString = "CREATE TABLE namazvakitleri (" + str(ilceSehir) + ", Tarih, İmsak, Güneş, Öğle, İkindi, Akşam, Yatsı)"
                cursor.execute(sqlString)
            
            except sqlite3.OperationalError:
                pass
                #print u"namazvakitleri tablosu zaten var."
                        
            url = "http://www.diyanet.gov.tr/turkish/namazvakti/vakithes_namazsonuc.asp"
            
            if Vakitler.ulke and Vakitler.sehir != None:
                veriler = urllib.urlencode({'ulk': Vakitler.ulke , 'sehirler': Vakitler.sehir, 'R1': 'AYLIK'})
                
                site = urllib.urlopen(url, veriler)
                html = site.read()
                
                tarih = re.compile('<td.*?>(.*?)&nbsp;</td>')
                tarih = tarih.findall(html)
                tarihler = []
                
                i = 0
                while i < 233:
                    tarihler.append(tarih[i])
                    i = i + 8
        
                if tarihler.count(Vakitler.simdikiTarih) == 0:
                    Vakitler.tarihHatasi = True
                    QtCore.QFile(PyVakitci.veritabaniDosyasi).remove()
                else:
                    vakit = re.compile('[1-2]*[0-9]\s[0-5][0-9]')
                    saatler = vakit.findall(html)
                            
                    i = 0
                    j = 0
                    while i < 204:            
                        imsak = "0" + saatler[i].replace(" ", ":")
                        gunes = "0" + saatler[i + 1].replace(" ", ":")
                        ogle = saatler[i + 2].replace(" ", ":")
                        ikindi = saatler[i + 3].replace(" ", ":")
                        aksam = saatler[i + 4].replace(" ", ":")
                        yatsi = saatler[i + 5].replace(" ", ":")
                        
                        sqlString = "INSERT INTO namazvakitleri VALUES ('" + \
                                        str(Vakitler.sehir) + "', '" + tarihler[j] + "', '" + \
                                        imsak + "', '" + gunes + "', '" + ogle + "', '" + \
                                        ikindi + "', '" + aksam + "', '" + yatsi + "')"
                        
                        cursor.execute(sqlString)
                        
                        i = i + 7
                        j = j + 1
                        
            connect.commit()
            
        else:
            PyVakitci.vakitleriAlCheckBox.setChecked(False)
            PyVakitci.veriler["R1"] = "HAFTALIK"
            self.run()
            
            
if __name__ == "__main__":
    
    # Uygulamanın tekrar açılmasını önlemeye yarayan yöntemlerden biri.
    import fcntl
    
    dosya = open(QtCore.QDir.tempPath() + "/PyVakitci.pid", "wb")

    try:
        fcntl.lockf(dosya, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        print u"Uygulama zaten çalışıyor."
        sys.exit(0)
     
    # uygulama.setApplicationName("rastgele bir isim") burada Phonon modülünün kusursuz çalışması için gerekli.
    uygulama.setApplicationName("PyVakitci")
    program = PyVakitci()
    
    sys.exit(uygulama.exec_())
