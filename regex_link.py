import urllib2
import re


url="http://www.javatpoint.com"
print dir(urllib2)
website=urllib2.urlopen(url)

print website
html=website.read()

links = re.findall('"((http|ftp)s?://.*?)"', html)

for i in links:
	print i[0]

