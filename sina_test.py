import re

string = "src=\"https:\/\/tva4.sinaimg.cn\/crop.0.8.750.750.50\/8e71b4f4jw8f6zcinp4h1j20ku0lbweu.jpg\""

pattern = re.compile(r'src=(.*?\.jpg).*?')

test = re.findall(pattern,string)
print test
x = test[0].split("\\")
print x
print len(x)

stringL = x[0]+x[1]+x[2]+x[3]+x[4]
print stringL
