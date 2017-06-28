import openpyxl

wb = openpyxl.load_workbook('example.xlsx',data_only=True)
sheet2 = wb.get_active_sheet()
sheet = wb.get_sheet_names()
print sheet
sheet1 = wb.get_sheet_by_name(sheet[0])
sheet2['A10']='=SUM(A1:A9)'
print sheet2['A10'].value
wb_len = sheet1.rows()
#wb_columns_len = len(sheet1.columns)
print wb_len
#print wb_columns_len
#暂时 openpyxl 不太好用，colums 和 cows 不能用
