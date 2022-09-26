import pandas as pd #libreria pandas para generar data frames
archivo = 'C:/Users/Gus/Escuela/5to semestre/EPC/proyecto.xls'#lectura del archivo axcel

df = pd.read_excel(archivo, sheet_name='Hoja1')#data frame extraido del excel 
print(df)#impime el data frame
#---------Segundo avance
import pandas as pd
try:
    excel = 'C:/Users/Gus/Escuela/5to semestre/EPC/proyecto.xls'
    res = 0
    df = pd.read_excel(excel, sheet_name='Hoja1')
    print(df)

    with open("Archiv01.lst","a") as archivo:
        while res != 10:
            print()
except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')
