from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)

pdf.cell(200, 10, txt="All of you must be familiar with that PDFs are", ln=1, align='C')
pdf.cell(200, 10, txt=" In-fact, they are one of the most important", ln=2, align='C')
pdf.cell(200, 10, txt="and widely used digital media. PDF stands for", ln=2, align='C')
pdf.cell(200, 10, txt="Portable Document Format. It uses .pdf extension.", ln=2, align='C')
pdf.cell(200, 10, txt="It is used to present abd exchange documents reliably,", ln=2, align='C')
pdf.cell(200, 10, txt="independent of software, hardware or operating system.", ln=2, align='C')

pdf.output("myPDF2.pdf")

