__author__ = 'halit'

class sonucAl:
    def __init__(self, soru):
        self.soru = soru
    def cevap(self):
        dosyal = open("new.txt", "r")
        sonuclar = [""]

        for satir in dosyal.readlines():
            sonuc = satir.split(".")
            sonuc = sonuc[1].replace("\n","")
            sonuclar.append(sonuc)
        return sonuclar[int(self.soru)]

