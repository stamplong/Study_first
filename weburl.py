import urllib2
import requests

def download(url):
    print 'Downloding:',url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:',e.reason
        html = None
    return html
download('http://www.jianshu.com/p/4ce1b066e12a')
