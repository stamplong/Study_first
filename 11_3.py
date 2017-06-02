import builtwith
import whois
import urllib2
import itertools
x = builtwith.parse('http://www.imooc.com/')
print x
print whois.whois('https://www.zhihu.com/')
url = 'https://www.zhihu.com/'
file1 = urllib2.urlopen(url).read()
print file1
print "*"*50
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()
