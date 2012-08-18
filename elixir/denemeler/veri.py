from model import *
from elixir import session

# kurulum yapiliyor
setup_all()

# olusuturuluyor
create_all()

# 1. kayit ekleniyor
Siteler(baslik="Halit Alptekin", site="http://www.halitalptekin.com", aciklama="Halit Alptekin Personal Blog")

# 2.kayit ekleniyor
Siteler(baslik="Google", site="http://www.google.com", aciklama="Arama Motoru")

# tum kayitlar ayni isimli degiskene ataniyor
kayitlar = Siteler.query.all()

# listenin tum elemanlarini yazdirmak icin for dongusu kuruluyor
for kayit in kayitlar:
    print "-" * 20
    print kayit.baslik
    print kayit.site
    print kayit.aciklama
    print "-" * 20

# baska turlu bir filtreleme yapalim ve ilk elemani alalim
sorgu = Siteler.query.filter_by(baslik=u'Halit Alptekin')
kayit = sorgu.first()

# uygun sekilde ekrana basalim
print "%s (%s)" %(kayit.baslik, kayit.site)

# ayni kaydi silelim
kayit.delete()
session.commit()

