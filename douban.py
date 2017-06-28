import re
import requests
import sys
import time
import os
reload(sys)
sys.setdefaultencoding('utf8')
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:53.0) Gecko/20100101 Firefox/53.0"}

url_1 ="https://book.douban.com/subject/270"
url_3 ="/?icn=index-editionrecommend"
for i in range(10000,100000):
    if i<10:
        url_2="0000%s"%i
        url = url_1+url_2+url_3
        request = requests.session()
        html = requests.get(url,headers=headers)
        text_html = html.text
        print url
        try:
            search_html = re.compile(r'<div id="mainpic" class="">(.*?)</div>',re.S)
            search_1 = re.findall(search_html,text_html)

            pattern_2 = re.compile(r'<a class="nbg".*?href=".*?" title="(.*?)">.*?<img src="(.*?)" title=".*?" alt=".*?".*?rel=".*?" style="width:.*?">.*?</a>',re.S)
            search_2 = re.findall(pattern_2,search_1[0])
            print search_2[0][1]

            pattern_3 = re.compile(r'<div class="rating_wrap clearbox" rel="v:rating">.*?<div class="rating_logo">(.*?)</div>.*? <strong class="ll rating_num " property="v:average">(.*?)</strong>',re.S)
            pattern_4 = re.compile(r'<span class="stars5 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars4 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars3 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars2 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars1 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>',re.S)
            rating_num = re.findall(pattern_3,text_html)
            starstop = re.findall(pattern_4,text_html)

            print rating_num[0][1]
            print starstop[0][1]
            string_finally = "book:\n" + search_2[0][0] + "\n" +"jpg_address:\n" +search_2[0][1] +"\n" + rating_num[0][0] + rating_num[0][1]+"\n" + starstop[0][0] +starstop[0][1] + starstop[0][2] + starstop[0][3] + starstop[0][4] + starstop[0][5] + starstop[0][6] + starstop[0][7] + starstop[0][8] + starstop[0][9]+"\n***********"+"\n\n\n"

            print string_finally
            src = os.getcwd()+"/papers/books.txt"

            write_to_txt = open(src,'a')
            write_to_txt.write(string_finally)
            write_to_txt.close
        except Exception,e:
            print "continue"


        time.sleep(2)
    elif i>=10 and i<100:
        url_2="000%s"%i
        url = url_1+url_2+url_3
        request = requests.session()
        html = requests.get(url,headers=headers)
        #text_html = html.text
        text_html = html.text
        print url
        try:
            search_html = re.compile(r'<div id="mainpic" class="">(.*?)</div>',re.S)
            search_1 = re.findall(search_html,text_html)

            pattern_2 = re.compile(r'<a class="nbg".*?href=".*?" title="(.*?)">.*?<img src="(.*?)" title=".*?" alt=".*?".*?rel=".*?" style="width:.*?">.*?</a>',re.S)
            search_2 = re.findall(pattern_2,search_1[0])
            print search_2[0][1]

            pattern_3 = re.compile(r'<div class="rating_wrap clearbox" rel="v:rating">.*?<div class="rating_logo">(.*?)</div>.*? <strong class="ll rating_num " property="v:average">(.*?)</strong>',re.S)
            pattern_4 = re.compile(r'<span class="stars5 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars4 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars3 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars2 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars1 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>',re.S)
            rating_num = re.findall(pattern_3,text_html)
            starstop = re.findall(pattern_4,text_html)

            print rating_num[0][1]
            print starstop[0][1]
            string_finally = "book:\n" + search_2[0][0] + "\n" +"jpg_address:\n" +search_2[0][1] +"\n" + rating_num[0][0] + rating_num[0][1]+"\n" + starstop[0][0] +starstop[0][1] + starstop[0][2] + starstop[0][3] + starstop[0][4] + starstop[0][5] + starstop[0][6] + starstop[0][7] + starstop[0][8] + starstop[0][9]+"\n***********"+"\n\n\n"

            print string_finally
            src = os.getcwd()+"/papers/books.txt"

            write_to_txt = open(src,'a')
            write_to_txt.write(string_finally)
            write_to_txt.close
        except Exception,e:
            print "continue"
        time.sleep(3)
    elif i>=100 and i<1000:
        url_2="00%s"%i
        url = url_1+url_2+url_3
        request = requests.session()
        html = requests.get(url,headers=headers)
        #text_html = html.text
        text_html = html.text
        print url
        try:
            search_html = re.compile(r'<div id="mainpic" class="">(.*?)</div>',re.S)
            search_1 = re.findall(search_html,text_html)

            pattern_2 = re.compile(r'<a class="nbg".*?href=".*?" title="(.*?)">.*?<img src="(.*?)" title=".*?" alt=".*?".*?rel=".*?" style="width:.*?">.*?</a>',re.S)
            search_2 = re.findall(pattern_2,search_1[0])
            print search_2[0][1]

            pattern_3 = re.compile(r'<div class="rating_wrap clearbox" rel="v:rating">.*?<div class="rating_logo">(.*?)</div>.*? <strong class="ll rating_num " property="v:average">(.*?)</strong>',re.S)
            pattern_4 = re.compile(r'<span class="stars5 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars4 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars3 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars2 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars1 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>',re.S)
            rating_num = re.findall(pattern_3,text_html)
            starstop = re.findall(pattern_4,text_html)

            print rating_num[0][1]
            print starstop[0][1]
            string_finally = "book:\n" + search_2[0][0] + "\n" +"jpg_address:\n" +search_2[0][1] +"\n" + rating_num[0][0] + rating_num[0][1]+"\n" + starstop[0][0] +starstop[0][1] + starstop[0][2] + starstop[0][3] + starstop[0][4] + starstop[0][5] + starstop[0][6] + starstop[0][7] + starstop[0][8] + starstop[0][9]+"\n***********"+"\n\n\n"

            print string_finally
            src = os.getcwd()+"/papers/books.txt"

            write_to_txt = open(src,'a')
            write_to_txt.write(string_finally)
            write_to_txt.close
        except Exception,e:
            print "continue"
        time.sleep(2)
    elif i>=1000 and i<10000:
        url_2="0%s"%i
        url = url_1+url_2+url_3
        request = requests.session()
        html = requests.get(url,headers=headers)
        #text_html = html.text
        text_html = html.text
        print url
        try:
            search_html = re.compile(r'<div id="mainpic" class="">(.*?)</div>',re.S)
            search_1 = re.findall(search_html,text_html)

            pattern_2 = re.compile(r'<a class="nbg".*?href=".*?" title="(.*?)">.*?<img src="(.*?)" title=".*?" alt=".*?".*?rel=".*?" style="width:.*?">.*?</a>',re.S)
            search_2 = re.findall(pattern_2,search_1[0])
            print search_2[0][1]

            pattern_3 = re.compile(r'<div class="rating_wrap clearbox" rel="v:rating">.*?<div class="rating_logo">(.*?)</div>.*? <strong class="ll rating_num " property="v:average">(.*?)</strong>',re.S)
            pattern_4 = re.compile(r'<span class="stars5 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars4 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars3 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars2 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars1 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>',re.S)
            rating_num = re.findall(pattern_3,text_html)
            starstop = re.findall(pattern_4,text_html)

            print rating_num[0][1]
            print starstop[0][1]
            string_finally = "book:\n" + search_2[0][0] + "\n" +"jpg_address:\n" +search_2[0][1] +"\n" + rating_num[0][0] + rating_num[0][1]+"\n" + starstop[0][0] +starstop[0][1] + starstop[0][2] + starstop[0][3] + starstop[0][4] + starstop[0][5] + starstop[0][6] + starstop[0][7] + starstop[0][8] + starstop[0][9]+"\n***********"+"\n\n\n"

            print string_finally
            src = os.getcwd()+"/papers/books.txt"

            write_to_txt = open(src,'a')
            write_to_txt.write(string_finally)
            write_to_txt.close
        except Exception,e:
            print "continue"
        time.sleep(2.1)
    elif i>=37639 and i<100000:
        url_2="%s"%i
        url = url_1+url_2+url_3
        request = requests.session()
        html = requests.get(url,headers=headers)
        #text_html = html.text
        text_html = html.text
        print url
        try:
            search_html = re.compile(r'<div id="mainpic" class="">(.*?)</div>',re.S)
            search_1 = re.findall(search_html,text_html)

            pattern_2 = re.compile(r'<a class="nbg".*?href=".*?" title="(.*?)">.*?<img src="(.*?)" title=".*?" alt=".*?".*?rel=".*?" style="width:.*?">.*?</a>',re.S)
            search_2 = re.findall(pattern_2,search_1[0])
            print search_2[0][1]

            pattern_3 = re.compile(r'<div class="rating_wrap clearbox" rel="v:rating">.*?<div class="rating_logo">(.*?)</div>.*? <strong class="ll rating_num " property="v:average">(.*?)</strong>',re.S)
            pattern_4 = re.compile(r'<span class="stars5 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars4 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars3 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars2 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>.*?<span class="stars1 starstop" title=".*?">(.*?)</span>.*?<span class="rating_per">(.*?)</span>',re.S)
            rating_num = re.findall(pattern_3,text_html)
            starstop = re.findall(pattern_4,text_html)

            print rating_num[0][1]
            print starstop[0][1]
            string_finally = "book:\n" + search_2[0][0] + "\n" +"jpg_address:\n" +search_2[0][1] +"\n" + rating_num[0][0] + rating_num[0][1]+"\n" + starstop[0][0] +starstop[0][1] + starstop[0][2] + starstop[0][3] + starstop[0][4] + starstop[0][5] + starstop[0][6] + starstop[0][7] + starstop[0][8] + starstop[0][9]+"\n***********"+"\n\n\n"

            print string_finally
            src = os.getcwd()+"/papers/books_one.txt"

            write_to_txt = open(src,'a+')
            write_to_txt.write(string_finally)
            write_to_txt.close
            print src
        except Exception,e:
            print "continue"
        time.sleep(1)
