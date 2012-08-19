from mongoengine import *

connect("mongod", host="localhost", port=27017)

class Siteler(Document):
    baslik = StringField(required=True)
    site   = StringField()

Siteler(baslik="Google",site="http://www.google.com").save()

for site in Siteler.objects:
    print "Site adi:%s Site adresi=%s" %(site.baslik,site.site)

