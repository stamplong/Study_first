import PyPDF2
import os
pdffileobj = open('./papers/Python.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(pdffileobj)
print pdfreader.numPages
pdfpage_num1 = pdfreader.getPage(240)
print pdfpage_num1.extractText()
encripted = pdfreader.isEncrypted
print encripted

for filename in os.listdir('./papers'):
    if filename.endswith('.pdf'):
        print filename
