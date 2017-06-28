import xlrd
import xlwt
from datetime import datetime
book = xlwt.Workbook()
ws = book.add_sheet('a test sheet')


style0 = xlwt.easyxf(num_format_str="D-MMM_YY")
style1 = xlwt.easyxf('font:name Times New Roman,color-index red,bold on')

ws.write(0,0,datetime.now(),style0)
ws.write(1,0,10,style1)
ws.write(2,0,10,style1)
ws.write(3,0,xlwt.Formula("A2+A3"))
book.save('abs.xls')
