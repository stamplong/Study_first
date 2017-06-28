import sys
import xlrd
import xlwt
N = sys.argv[1]
M = sys.argv[2]
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
print df
for d in range(N,df):
    for f in range (M,sheet1.ncols):
        open_workbook.write(N,M," ")
open_workbook.save('exmaple00.xls')
