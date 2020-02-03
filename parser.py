import argparse

def parser():   
    analizador = argparse.ArgumentParser(description='Seleccionar dos años para filtrar el DataSet')
    analizador.add_argument("-s","--start",nargs="?",default=1960,help="Año inicial",type=int)
    analizador.add_argument("-e","--end",nargs="?",default=2015,help="Año final",type=int)
    argumento = analizador.parse_args()
    if argumento.start in range(1959,2016) and argumento.end in range(argumento.start+1,2016):
        year_start = argumento.start
        year_end = argumento.end
        return year_start, year_end
    else:
        return('Error')