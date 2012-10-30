from turkish.deasciifier import Deasciifier
import os

def deascii(text):
	my_ascii_turkish_txt = text
	deasciifier = Deasciifier(my_ascii_turkish_txt.decode("utf-8"))
	my_deasciified_turkish_txt = deasciifier.convert_to_turkish()

	return my_deasciified_turkish_txt.encode("utf-8")

def aramayap(dizin):
	dosyalist = []
	for kok, altdizinler, dosyalar in os.walk(dizin):
		for dosya in dosyalar:
			if "md" in dosya:
				dosyalist.append(os.path.join(kok,dosya))	
	return dosyalist

def donustur(gel):
	liste = aramayap(gel)
	sayac = len(liste)
	i = 0

	while i < sayac:
		metin = ""

		with open(liste[i] ,"r") as dosya:
			metin = dosya.read()

		metin = deascii(metin)

		with open(liste[i] ,"w") as dosya:
			dosya.write(metin)	

		i +=1


donustur("/home/halit/test/")

	

