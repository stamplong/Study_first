import requests
import bs4
import webbrowser
res = requests.get('https://www.pengfu.com/')
playfile = open('124.txt','wb')
for chunk in res.iter_content(1000000)
    playfile.write(chunk)
file1 = bs4.BeautifulSoup(res.text)
x = file1.select('p')
print x[1]
