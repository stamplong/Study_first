import xlrd
import xlwt
import re
x = "abc you are sunshine"
d = re.compile(r'.*')
patter = re.findall(d,x)
print patter
