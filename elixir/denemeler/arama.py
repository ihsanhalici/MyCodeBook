from veri import *

sorgu = Siteler.query.filter_by(baslik=u'Halit Alptekin')
kayit = sorgu.first()

print "%s (%s)" %(kayit.baslik, kayit.site)
