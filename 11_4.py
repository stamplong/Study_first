import requests
import urllib2
import re
r = urllib2.urlopen('https://www.pengfu.com/')
s = urllib2.Request('http://www.pengfu.com/')
reponse = urllib2.urlopen(s)
print reponse.read()
pattern = re.compile(r'') 
