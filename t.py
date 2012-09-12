import re
import urllib

urls = [
"http://eepurl.com/pbre9",
"http://eepurl.com/oZDWD",
"http://eepurl.com/oLWeP"
"http://eepurl.com/ozczX",
"http://eepurl.com/ol9Zf",
"http://eepurl.com/n-ZL5",
"http://eepurl.com/nYNDD",
"http://eepurl.com/nLZzz",
"http://eepurl.com/ny-Hz",
"http://eepurl.com/nmrBn",
"http://eepurl.com/m_d5r",
"http://eepurl.com/mXMAr",
"http://eepurl.com/mKD4D",
"http://eepurl.com/mwM7v",
"http://eepurl.com/mjhNz",
"http://eepurl.com/l8eA1",
"http://eepurl.com/lUAtr",
"http://eepurl.com/lHlPz",
"http://eepurl.com/ltr9P",
"http://eepurl.com/lgdNf",
]

with open("dosya.txt", "a") as dosya:

	for url in urls:

		f = urllib.urlopen(url)
		pislink = []

		for i in f:
		    nesne = re.search('<span style="font-size:14px;">(.+)</span>',i)
		    if nesne:
		        pislink.append(nesne.group(1))

		def temizle(link):
			link = link.replace('<a href="','')
			link = link.replace('" target="_blank" style="color: #1173C7;text-decoration: underline;font-weight: bold;">','::')
			link = link.replace('</a>','')

			nesne = re.search('(.+)::(.+)',link)
			title = ""
			if nesne:
				title = nesne.group(2)
				link  = nesne.group(1)

			return title, link

		for i in pislink:
			yazi = str(temizle(i))
			dosya.write(yazi + "\n")