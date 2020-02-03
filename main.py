from parser import parser
from grafica import graph
from fpdf import FPDF
from  print_pdf import print_PDF
from send_email import sendEmail

if __name__ == "__main__":
    # parser returns arguments `pre-processed` for us
    
    # use calc to calculate result of our program
    try:
        year_start, year_end= parser()
        graph(year_start, year_end)
        print_PDF()
        sendEmail()
    except ValueError:
        print("Error de parametros introduce un año entre 1960 y 2015")