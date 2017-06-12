import urllib
import re
import urllib2

url = "http://www.baidu.com/"
opener = urllib2.build_opener()
postdata = urllib.urlencode({
"username":"longzitan@126.com",
"password":"stamp208A22"
}).encode('utf-8')
rep = urllib.urlopen(url,postdata)
rep.add_header('User_Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:53.0) Gecko/20100101 Firefox/53.0')
file_1 = opener.open(rep)
data = file_1.read()
print(data)
