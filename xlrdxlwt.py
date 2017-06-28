import xlrd
import xlwt
import os
file_name = os.getcwd()
file_1 = file_name + '/papers/examples_1.xls'
print file_1


workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1')
style0 = xlwt.easyxf('font:color-index orange,bold on')
for x in range(1,10):

    sheet1.write(x,0,x,style0)
    sheet1.write(0,x,x,style0)
    for f in range(1,10):
        sheet1.write(f,x,f*x)





workbook.save(file_1)
