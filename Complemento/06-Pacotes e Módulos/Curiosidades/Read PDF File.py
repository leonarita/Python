import PyPDF2

fileObj = open("code.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(fileObj)
print(f"No. of pages: {pdfReader.numPages}")

pageObj = pdfReader.getPage(8)
print(pageObj.extractText())

fileObj.close()

