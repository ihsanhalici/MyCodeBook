# -*- coding: utf-8 -*-
#!/usr/bin/env python

import DiyanetEyaletlerIlceler
from DiyanetUlkelerSehirler import DiyanetUlkelerSehirler

class DiyanetSehirler:
    def __init__(self):
        self.ulkelerSehirlerDiyanet = DiyanetUlkelerSehirler()
        
    def ilceleriEkle(self, ilceler_comboBox, ulke, sehir):
        ilceler_comboBox.clear()
        
        try:
            if (ulke == "ABD") or (ulke == "KANADA"):
                ilceler = eval("sorted(DiyanetEyaletlerIlceler." + str(ulke) + "." + str(sehir.replace(" ", "_")) + ")")
            else:
                ilceler = eval("sorted(DiyanetEyaletlerIlceler." + str(ulke) + "." + str(sehir) + ")")
            
            for ilce in ilceler:
                ilceler_comboBox.addItem(ilce)
        except:
            pass
        
    def sehirleriEkle(self, sehirler_comboBox, secilenUlke):
        
        secilenUlke = str(secilenUlke.replace(" ", "_").replace("-", "_"))
        
        if len(secilenUlke) != 0:
            for sehir in eval("self.ulkelerSehirlerDiyanet." + secilenUlke):
                sehirler_comboBox.addItem(sehir.replace("_", " "))