#!/usr/bin/env python

from fuzzy import Soundex

class aramaYap:
    def __init__(self, veritabani, arancak):
        self.veritabani = veritabani
        self.arancaklar = arancak.lower().split(" ")
        self.soundex    = Soundex(4)
        self.sonuclar   = []

    def parset(self, liste):
        ksozluk = {}
        i = 0
        for eleman in liste:
            lis  = []
            dlis = []
            lis.append(eleman)
            dlis.append(eleman.lower().split(" "))
            lis.append(dlis)
            ksozluk[i] = lis
            i+=1
        return ksozluk

    def arama(self):
        veritabani  = self.parset(self.veritabani)
        i = 0
        while i < len(veritabani):
            for kelimem in veritabani[i][1][0]:
                for arancak in self.arancaklar:
                    if self.soundex(kelimem) == self.soundex(arancak):
                        if self.sonuclar.count(veritabani[i][0]) < 1:
                            self.sonuclar.append(veritabani[i][0])
            i+=1
        print self.sonuclar


