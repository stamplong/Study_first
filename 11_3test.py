import builtwith
import whois
import urllib2
import urllib
import itertools
import re
url = "https://www.pengfu.com/"
html_requests = urllib2.Request(url)
reponse = urllib2.urlopen(html_requests)
web_reptile_read = reponse.read()

pattern_1 = re.compile(r'.*<div class="w960 clearfix">.*<div class="w645 fl">(.*)</div>.*</div>.*',re.S)
pattern_values = re.findall(pattern_1,web_reptile_read)
html_text = str(pattern_values[0])


pattern_2 = re.compile(r'<img src="(https://.*?\.jpg)"',re.S)
html_txt_2 = pattern_2.findall(html_text)
print html_txt_2[3]

print len(html_txt_2)
for i in range(0,len(html_txt_2)):
    filename_1 = "%s.jpg"%i
    image_name = "/Users/admin/Study_first/papers/"+ filename_1
    print image_name
    urllib.urlretrieve(html_txt_2[i],filename=image_name)
