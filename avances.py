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
    
#------------------------Terce avance
import pandas as pd
#tr:
excel = 'C:/Users/Gus/Escuela/5to semestre/EPC/proyecto.xls'
res = 0
df = pd.read_excel(excel, sheet_name='Hoja1')
#print(df)
#a = "fdhfg"
#hombres=df[df["MNEMONICO"]=="aba"]
#subset = hombres[['IMM', 'DIR', 'IND,X','IND,Y', 'EXT', 'INH','REL']]
#tuples = [tuple(x) for x in subset.values]
#print(tuples)
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
#------------------------------ 4to avance
import pandas as pd
#tr:
excel = 'proyecto.xls'
res = 0
df = pd.read_excel(excel, sheet_name='Hoja1')
#print(df)
#a = "fdhfg"
#hombres=df[df["MNEMONICO"]=="aba"]
#subset = hombres[['IMM', 'DIR', 'IND,X','IND,Y', 'EXT', 'INH','REL']]
#tuples = [tuple(x) for x in subset.values]
#print(tuples)
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
    
#-----------------------------Avance 5
import pandas as pd
excel = 'proyecto.xls'
dirEn = ["ORG","EQU","FCB","END"]
arregl01 = []
res = 0
df = pd.read_excel(excel, sheet_name='Hoja1')
with open("BURBUJA.asc") as archivoASC:
    for i in archivoASC:#lee el archivo y realiza un ciclo
        a=0
        splitt = i.split()
        print(i)
        #print(splitt)
        #print(splitt)
        for j in splitt:
            if len(splitt) != 0 and j[0]!="*" :
                #print(j)
                dfNem=df[df["MNEMONICO"]==str(j.lower())]
                subset = dfNem[['IMM', 'DIR', 'IND,X','IND,Y', 'EXT', 'INH','REL']]
                arr = [tuple(x) for x in subset.values]
                #print(arr)
                for y in arr:
                    #print(f"{j} {y} {len(splitt)} {a} {a+1} {splitt}")
                    #if ((a+1) < len(splitt) and splitt[a+1] == y):
                    if ((a+1) < len(splitt)):
                        #print(f"{j} {splitt[a+1]}")
                        arregl01.append(splitt[a+1])
            else:
                if j[0]=="*" and a>0:
                    break
            #print(j)
        a=a+1
    #print(arregl01)

with open("archiv01.lst","a") as archivo:
    while res != 10:
        archivo.write(f"\n")
        res = 10
#exept Exception as e:
    #print(f'Exception - Ocurrió un error: {e} , {type(e)}, {}')
    
# ------------------------------------------------- Avance 6

import pandas as pd
excel = 'proyecto.xls'
dirEn = ["org","equ","fcb","end"]
arregl01 = []
var = {}
const = {}
res = 0
df = pd.read_excel(excel, sheet_name='Hoja1')
with open("BURBUJA.asc") as archivoASC:
    for i in archivoASC:#lee el archivo y realiza un ciclo
        a=0
        splitt = str(i.lower()).split()
        #print(i)
        #print(splitt)
        #print(splitt)
        for j in splitt:
            if len(splitt) != 0 and j[0]!="*" :
                if  len(splitt) > 1 and splitt[1]==dirEn[1] and j[1:3]=="00":
                    var[splitt[0]]=splitt[2]
                if  len(splitt) > 1 and splitt[1]==dirEn[1] and j[1]=="1":
                    const[splitt[0]]=splitt[2]
                dfNem=df[df["MNEMONICO"]==str(j.lower())]
                subset = dfNem[['IMM', 'DIR', 'IND,X','IND,Y', 'EXT', 'INH','REL']]
                for y in subset.values:
                    #print(f"{j} {y} {len(splitt)} {a} {a+1} {splitt}")
                    for z in y:
                        #print(f"{splitt[a+1]} {str(z)},X")
                        if ((a+1) < len(splitt) and splitt[a+1] == z):
                            print(f"{j} {splitt[a+1]}")
                            arregl01.append(splitt[a+1])
                        if((a+1) < len(splitt) and splitt[a+1] == ("#"+str(z))):
                            print(f"{j} {splitt[a+1]}")
                        if((a+1) < len(splitt) and (splitt[a+1] == (str(z)+",X") or splitt[a+1] == (str(z)+",Y"))):
                            print(f"{j} {splitt[a+1]}")
                        if((a+1) < len(splitt) and (splitt[a+1] == (str(z)+",X") or splitt[a+1] == (str(z)+",Y"))):
                            print(f"{j} {splitt[a+1]}")
            else:
                if j[0]=="*" and a>0:
                    break
            #print(j)
        a=a+1
    print(var)
    print(const)

with open("archiv01.lst","a") as archivo:
    while res != 10:
        archivo.write(f"\n")
        res = 10
#exept Exception as e:
    #print(f'Exception - Ocurrió un error: {e} , {type(e)}, {}')
