from elixir import *

# veritabani seciliyor
metadata.bind = "sqlite:///siteler.db"

# sql sorgusu ekrana basiliyor
metadata.bind.echo = False

class Siteler(Entity):

   # baslik kolonu 30 karakter siniriyla
    baslik   = Field(Unicode(30))

    # site kolonu
    site     = Field(Unicode)

    # aciklama kolonu
    aciklama = Field(UnicodeText)

    # geri donus
    def __repr__(self):
        return "<Site '%s' (%s) - %s" %(self.baslik, self.site, self.aciklama)
