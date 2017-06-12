import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
url = "http://weibo.com/u/5278517747/home?wvr=5&uut=fin&from=reg"
cookies = 'SINAGLOBAL=1118617277445.4795.1496911942852; ULV=1496911943236:1:1:1:1118617277445.4795.1496911942852:; SCF=Auq-RyoAwt-oiYlbg94HEychP4BelPDTr1aYAs6aejo7INo9Ix5Pbq8hjiPWhRj9Z2PsScbgRg3wVLqi-xtx8PQ.; SUHB=08JrIgilMwsCtf; ALF=1528596623; un=446762229@qq.com; wvr=6; TC-Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e; TC-V5-G0=784f6a787212ec9cddcc6f4608a78097; TC-Page-G0=e2379342ceb6c9c8726a496a5565689e; login_sid_t=8ff5843b4d5ea4760778dda4d0cebc84; _s_tentry=-; Apache=1118617277445.4795.1496911942852; SSOLoginState=1496911971; SUB=_2A250PyVADeThGeNM7FoU8SnLzzuIHXVXTRGIrDV8PUNbmtAKLRP1kW808cQ2sR3sX8ECkPOmF5sGn2bk7Q..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWNw0im15xSTWg4lfgOJg3c5JpX5KMhUgL.Fo-ES0nfeKMNShM2dJLoIpRLxK.LB.-L1K.LxK-LB-BL1K5LxK-LB.eLBo._eKBt; UOR=,,login.sina.com.cn'
cookies123 = cookies.split(';')

cookies_right = {}
for line in cookies123:
    key,value=line.split('=',1)
    cookies_right[key]=value
print cookies_right

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:53.0) Gecko/20100101 Firefox/53.0"}
login = requests.session()
login_sina = login.get(url,cookies=cookies_right,headers=header)
text = str(login_sina.text)

print login_sina.text
print "***********"*50

pattern = re.compile(r'src=(.*?\.jpg)',re.S)

img_src = re.findall(pattern,text)
print img_src
