import re
import urllib2
import bs4
import sys
# 修改在 argv.py
url = "http://www.youdao.com/w/" + sys.argv[1] + "/#keyfrom=dict2.top"

def download(url):
    requests = urllib2.Request(url)
    reponse = urllib2.urlopen(requests)
    web_reptile_read = reponse.read()


    pattern2 = re.compile(r'<div class="trans-container">(.*?)</div>',re.S)
    dic_text = re.findall(pattern2,web_reptile_read)

    pattern_finally = re.compile(r'<ul>.*?<li>(.*)</li>.*?|<li>(.*)</li>.*?|<li>(.*)</li>.*?|<li>(.*)</li>.*?|</ul>',re.S)
    dic_text_finally = re.findall(pattern_finally,dic_text[0])

    if len(dic_text_finally)==1:
        finally_str = dic_text_finally[0][0].replace("<li>","")
        finally_string = finally_str.replace("</li>","")
        print finally_string
    elif len(dic_text_finally)==2:
        finally_str = dic_text_finally[0][0].replace("<li>","") +"\n" + dic_text_finally[0][1].replace("<li>","")
        finally_string = finally_str.replace("</li>","")
        print finally_string
    elif len(dic_text_finally)==3:
        finally_str = dic_text_finally[0][0].replace("<li>","") + "\n" + dic_text_finally[0][1].replace("<li>","") + "\n" + dic_text_finally[0][2].replace("<li>","")
        finally_string = finally_str.replace("</li>","")
        print finally_string
    elif len(dic_text_finally)==4:
        finally_str = dic_text_finally[0][0].replace("<li>","") + "\n" + dic_text_finally[0][1].replace("<li>","") + "\n" + dic_text_finally[0][2].replace("<li>","") + "\n"+dic_text_finally[0][3].replace("<li>","")
        finally_string = finally_str.replace("</li>","")
        print finally_string

download(url)
