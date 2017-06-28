import sys
import xlrd
import xlwt
from xlutils.copy import copy
M = int(sys.argv[1])
N = int(sys.argv[2])
workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1')
for i in range(0,20):
    for x in range(0,20):
        sheet1.write(x,i,i*x)
workbook.save('exmaple00.xls')

open_workbook = xlrd.open_workbook('exmaple00.xls')
sheet1 = open_workbook.sheet_by_index(0)
print sheet1.name
print sheet1.nrows
print sheet1.row_values(1)
df = sheet1.nrows
xf = sheet1.ncols
print df,xf
new_book = copy(open_workbook)
sheet2 = new_book.get_sheet(0)
style0 = xlwt.easyxf('font:color-index red,bold on')

for t in range(0,df):
    sheet2.write(M,t,456,style0)
    sheet2.write(df,t,'#',style0)
    sheet2.write(df+1,t,"?",style0)
new_book.save('exmaple00.xls')
