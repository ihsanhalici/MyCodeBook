#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys

def dosyalama(yer, uzanti):
	dosyalist = []

	for kok, altdizinler, dosyalar in os.walk(yer):
		for dosya in dosyalar:
			if dosya.endswith(uzanti):
				dosyalist.append(os.path.join(kok,dosya))	
	return dosyalist					


print dosyalama("/home/halit/araci","py")
