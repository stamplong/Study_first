#!/usr/bin/env python
#_*_ coding:utf-8_*_
import openpyxl
#from openpyxl.styles import Font,Style


import sys

reload(sys)
sys.setdefaultencoding('utf8')

wb = openpyxl.load_workbook('example.xlsx')
sh = wb.get_sheet_names()
print sh[0]
sheet1 = wb.get_sheet_by_name(sh[0])
sh1 = wb.get_active_sheet()
print sh1
c = sheet1['B2']

print c.value
print c.row
print c.column
print c.coordinate
print "*"*20

print sheet1.cell(row=3,column=2).value
tuple(sheet1)
for i in sheet1['A1':'C3']:
    for x in i:
        print x.coordinate,x.value
dic = {'abc':{'def':{'xbd':'enaf'}}}
print dic['abc']['def']['xbd']
#Style_fontobj1 = Style(font=fontobj1)
#c.Style/Stylefontobj1
#wb.save('example.xlsx')

for x in sheet1['A1':'A10']:
    for d in x:
        print d.value
