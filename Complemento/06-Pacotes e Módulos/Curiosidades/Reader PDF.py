import PyPDF2

pdfFileObj = open('your_pdf_file.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)

print(pdfReader.numPages)
print(pageObj.extractText())

pdfFileObj.close()