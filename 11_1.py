import requests
import webbrowser
import bs4
res = requests.get('http://www.cnblogs.com/kaituorensheng/archive/2013/03/18/2965766.html')
print type(res)
print res.status_code == requests.codes.ok
playfile = open('abc.txt','wb')
for chunk in res.iter_content(10000000):
    playfile.write(chunk)
playfile.close

examplefile = bs4.BeautifulSoup(res.text)
print type(examplefile)
pElems = examplefile.select('p')
print pElems[0].getText()
soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.r a')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
