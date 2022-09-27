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
    for i in archivoASC:#lee el archivo y realiza un ciclo sobre las lineas del archivo
        a=0
        read = archivoASC.readline()
        splitt = read.split()#separa por un espacio los datos
        #print(splitt)
        for j in splitt:# realiza un ciclo sobre las tuplas del slpit
            #print(j)
            if len(splitt) != 0 : #identifica que no este vacia la tupla
                #print(j)
                dfBus=df[df["MNEMONICO"]==j.lower()]#busca elmnemonico
                subset = dfBus[['IMM', 'DIR', 'IND,X','IND,Y', 'EXT', 'INH','REL']]
                tuples = [tuple(x) for x in subset.values] #realiza una tupla con el mnemonico buscado
                #print(tuples)
                for y in tuples: 
                    #print(f"{j} {y} {len(splitt)} {a} {a+1} {splitt}") #imprime el mnemonico buscado, la tupla obtenida de mnemonicos, tamaño de la tupla del split, 
                    #contador, contador mas 1 y la tupla de split
                    if ((a+1) < len(splitt) and splitt[a+1] == y): #compara que la tupla de mnemonicos sea mas pequeña que el contador y que sea igual el caracter 
                        #despues del mnemonico a la tupla
                        print(f"{j} {splitt[a+1]}")
        a=a+1

with open("archiv01.lst","a") as archivo:
    while res != 10:
        archivo.write(f"\n")
        res = 10
#exept Exception as e:
    #print(f'Exception - Ocurrió un error: {e} , {type(e)}, {}')
