import pandas as pd  # libreria pandas para generar data frames

#---------Segundo avance
try:
    excel = '/FinalEPC/proyecto.xls'
    res = 0
    df = pd.read_excel(excel, sheet_name='Hoja1')
    print(df)

    with open("Archiv01.lst","a") as archivo:
        while res != 10:
            print()
except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')
    
#------------------------Terce avance
with open("BURBUJA.asc","r") as archivoASC:
    for i in archivoASC:#lee el archivo y realiza un ciclo
        a=0
        read = archivoASC.readline()
        splitt = read.split()
        #print(splitt)
        for j in splitt:
            if len(splitt) != 0 and j[0]!="*":
                #print(j)
                dfNem=df[df["MNEMONICO"]==str(j.lower())]
                subset = dfNem[['IMM', 'DIR', 'IND,X','IND,Y', 'EXT', 'INH','REL']]
                arr = [tuple(x) for x in subset.values]
                #print(tuples)
                for y in arr:
                    #print(f"{j} {y} {len(splitt)} {a} {a+1} {splitt}")
                    if ((a+1) < len(splitt) and splitt[a+1] == y):
                        print(f"{j} {splitt[a+1]}")
        a=a+1

with open("archiv01.lst","a") as archivo:
    while res != 10:
        archivo.write(f"\n")
        res = 10
#exept Exception as e:
    #print(f'Exception - Ocurrió un error: {e} , {type(e)}, {}')
