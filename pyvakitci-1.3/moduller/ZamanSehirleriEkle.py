#!/usr/bin/env python
# -*- coding: utf-8 -*-

from moduller.ZamanUlkelerSehirler import ZamanUlkelerSehirler

class ZamanSehirler:
    def __init__(self):
        self.ulkelerSehirlerZaman = ZamanUlkelerSehirler()
        
    def sehirleriEkle(self, sehirler_comboBox, secilenUlke):
        secilenUlke = str(secilenUlke.replace(" ", "_").replace("-", "_"))
        
        if len(secilenUlke) != 0:
            for sehir in eval("sorted(self.ulkelerSehirlerZaman." + str(secilenUlke) + ")"):
                sehirler_comboBox.addItem(sehir)