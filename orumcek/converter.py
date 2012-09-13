
with open("items1.json","r") as oku:
    yazilar = oku.read()
    yazilar.replace("\u011f","ğ")