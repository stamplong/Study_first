#_*_coding:UTF-8_*_
# -*- coding:gb2312 -*-
import os
import urllib2
import whois
import urlparse
import bs4
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://www.baidxxxu.com'
url1 = "https://www.pengfu.com/"
url2 = "http://www.jianshu.com/p/e3c971cfe414"

def download(url):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        x = response.read()

        pattern1 = re.compile(r'<h1 class="title">(.*)</h1>')
        pattern2 = re.compile(r'<a href="/u/13fd1e867245">(.*?)</a>')

        fx = re.findall(pattern1,x)
        b = re.findall(pattern2,x)
        sentence = fx[0] + b[0]

        print fx[0]
        print b[0]

        # 打印结果：
        # 标题： xxxxx
        # 作者： yyy

        #finally_file = open('/Users/admin/Study_first/af.txt','w')
        #finally_file.write(sentence)
        #finally_file.close()

    except urllib2.URLError as e:
        print "download Error+++++++",e.reason

html1 = download(url2)
