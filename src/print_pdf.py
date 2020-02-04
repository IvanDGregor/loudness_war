from fpdf import FPDF

def print_PDF():
    pdf = FPDF('L', 'mm','A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 40)
    pdf.cell(15, 10, 'Report')
    pdf.set_font('Arial', 'B', 30)
    pdf.cell(1, 45, 'Loudness')
    pdf.image('../output/grafica_1.png', 30,40, h=150)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 30)
    pdf.cell(40, 10, 'Tempo')
    pdf.image('../output/grafica_2.png', 35,20, h=150)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 30)
    pdf.cell(40, 10, 'Energy')
    pdf.image('../output/grafica_3.png', 35,20, h=150)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 30)
    pdf.cell(40, 10, 'Danceability')
    pdf.image('../output/grafica_4.png', 35,20, h=150)
    return pdf.output('../output/report.pdf', 'F')