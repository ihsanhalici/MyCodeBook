#-*-coding:utf8-*-

import re
import urllib

f = urllib.urlopen("http://www.tcmb.gov.tr/kurlar/today.html")

derli = re.compile("(ABD\sDOLARI\s+)([0-9]\.[0-9]+)")

nesne = derli.search(f.read())

print nesne.group(2)