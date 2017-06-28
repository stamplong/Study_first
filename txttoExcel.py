import os
import xlwt,xlrd
from xlutils.copy import copy
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = os.getcwd()
url_1 = url+'/txttoexcel.txt'
print url_1
txt = open(url_1)
txt_read = txt.readlines()

workbook = xlrd.open_workbook('exmaple001.xls')
sheet2 = workbook.sheet_by_index(0)

new_book = copy(workbook)
sheet1 = new_book.get_sheet(0)
print sheet2.nrows
length = len(txt_read)
print length
last_row = length + sheet2.nrows
print last_row
x = 0
for i in range(sheet2.nrows,last_row):
    sheet1.write(i,0,txt_read[x])
    x+=1

new_book.save('exmaple002.xls')
