import xlrd,xlwt
import os
txt_url = os.getcwd()
txt_url_1 = txt_url+'/Exceltotxt.txt'
f = open(txt_url_1,'rb+')

workbook = xlrd.open_workbook('exmaple002.xls')
sheet1 = workbook.sheet_by_index(0)
print sheet1.cell(1,2).value
for x in range(0,sheet1.nrows):
    for l in range(0,sheet1.ncols):
        wt = sheet1.cell(x,l).value
        w = str(wt)
        f.write(w)
f.close()
