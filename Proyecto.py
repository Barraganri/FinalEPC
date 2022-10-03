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
