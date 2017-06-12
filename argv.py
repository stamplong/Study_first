import re
import urllib2
import sys
import os
x = sys.argv[1]
print x
url = "http://www.youdao.com/w/" + sys.argv[1] + "/#keyfrom=dict2.top"
os.system('say %s'%x)
def download(url):
    requests = urllib2.Request(url)
    reponse = urllib2.urlopen(requests)
    web_reptile_read = reponse.read()


    pattern2 = re.compile(r'<div class="trans-container">(.*?)</div>',re.S)
    dic_text = re.findall(pattern2,web_reptile_read)
    dic_text_str = dic_text[0]
    print dic_text_str.count("</li>")
    #pattern_finally = re.compile(r'<ul>.*?<li>(.*)</li>.*?|<li>(.*)</li>.*?|<li>(.*)</li>.*?|<li>(.*)</li>.*?</ul>',re.S|re.I)
    #dic_text_finally = re.findall(pattern_finally,dic_text[0])
    if dic_text_str.count("</li>")==1:
        print dic_text_str.count("</li>")
        pattern_finally = re.compile(r'ul>.*?<li>(.*)</li>.*?</ul>',re.S)
        dic_text_finally = re.findall(pattern_finally,dic_text_str)
        print dic_text_finally[0][0]


    elif dic_text_str.count("</li>")==2:
        print dic_text_str.count("</li>")
        pattern_finally = re.compile(r'ul>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?</ul>',re.S)
        dic_text_finally = re.findall(pattern_finally,dic_text_str)
        dic = dic_text_finally[0][0] + "\n" + dic_text_finally[0][1]
        print dic

    elif dic_text_str.count("</li>")==3:
        print dic_text_str.count("</li>")
        pattern_finally = re.compile(r'ul>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?</ul>',re.S)
        dic_text_finally = re.findall(pattern_finally,dic_text_str)
        dic = dic_text_finally[0][0] + "\n" + dic_text_finally[0][1] + "\n" + dic_text_finally[0][2]
        print dic

    elif dic_text_str.count("</li>")==4:
        print dic_text_str.count("</li>")
        pattern_finally = re.compile(r'ul>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?</ul>',re.S)
        dic_text_finally = re.findall(pattern_finally,dic_text_str)
        dic = dic_text_finally[0][0] + "\n" + dic_text_finally[0][1] + "\n" + dic_text_finally[0][2]+"\n"+dic_text_finally[0][3]
        print dic

    elif dic_text_str.count("</li>")==5:
        print dic_text_str.count("</li>")
        pattern_finally = re.compile(r'ul>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?<li>(.*)</li>.*?</ul>',re.S)
        dic_text_finally = re.findall(pattern_finally,dic_text_str)
        dic = dic_text_finally[0][0] + "\n" + dic_text_finally[0][1] + "\n" + dic_text_finally[0][2]+"\n"+dic_text_finally[0][3]+"\n"+dic_text_finally[0][4]
        print dic






download(url)
