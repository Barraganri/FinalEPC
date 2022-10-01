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
