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
#------------------------------------------------ MEGA AVANCE RADICAL o.O
from itertools import count
import pandas as pd
excel = 'proyecto.xls'
directivas = ["org","equ","fcb","end"]
Hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
num = ["0","1","2","3","4","5","6","7","8","9"]
arregl01 = []
arrS19 = []
var = {}
const = {}
res = 0
df = pd.read_excel(excel, sheet_name='Hoja1')

def sacaDato(arreglo):
    arr = ""
    for i in arreglo.values:
        arr = i[0]
    #print(arr)
    return str(arr)

def compar(dato,arr):
    res = False
    for i in arr:
        if i == dato:
            res = True
    return res

def conNum(n,arr,dato):
    count1 = 0
    for i in range(n):
        for j in arr:
            if dato[i] == j:
                count1=count1+1
    return count1

def conNum2(arr,dato):
    count1 = 0
    ret = False
    for i in dato:
        for j in arr:
            if i == str(j):
                count1=count1+1
            if count1 == len(dato):
                ret = True
    return ret

def transHex(dato,intt):
    if(intt == 0):
        aux = str(hex(int(dato)[2:]))
        if len(aux) == 1:
            aux = "0" + aux
        elif len(aux) == 3:
            aux = "0" + aux[0] + " " + aux[1:]
        return aux
    if(intt == 1):
        aux = dato
        if len(aux) == 1:
            aux = "0" + aux
        elif len(aux) == 3:
            aux = "0" + aux[0] + " " + aux[1:] 
        return aux

def formatoS19(lineas,mnemonico,dire,lineaCom):
    aux = ""
    if (len(dire) != 0 and  len(mnemonico) != 0 ):
        aux = str(lineas)+": ("+mnemonico+dire+") " + lineaCom
        arrS19.append(aux)
    else:
        aux = str(lineas)+": " + lineaCom
        arrS19.append(aux)


with open("EJEMPLO.asc") as archivoASC:
    linea = 0
    for i in archivoASC:#lee el archivo y realiza un ciclo
        a=0
        splitt = str(i.lower()).split()
        for j in splitt:
            
            if len(splitt) != 0 and j[0]!="*" and (a+1) <= len(splitt) :
                if  len(splitt) > 1 and splitt[1]==directivas[1] and j[1:3]=="00":
                    var[splitt[0]]=splitt[2]
                elif  len(splitt) > 1 and splitt[1]==directivas[1] and j[1]=="1":
                    const[splitt[0]]=splitt[2]
                dfNem=df[df["MNEMONICO"]==str(j.lower())]
                #subset = dfNem[['IMM', 'DIR', 'IND,X','IND,Y', 'EXT', 'INH','REL']]
                if ((a+1) == len(splitt) and len(dfNem) != 0 ):
                    inh = dfNem[['INH']]
                    #arregl01.append(j)
                    arregl01.append(sacaDato(inh))
                    formatoS19(linea,sacaDato(inh),a,j)
                    #print(f"{j} {sacaDato(inh)} ")
                if ((a+1) < len(splitt) and splitt[a+1][0:2] == "#$" and conNum2(Hex,splitt[a+1][2:])):
                    imm = dfNem[['IMM']]
                    #arregl01.append(j)
                    arregl01.append(sacaDato(imm))
                    arregl01.append(transHex(splitt[a+1][2:],1)) 
                    #print(f"{j} {splitt[a+1]}")
                if ((a+1) < len(splitt) and splitt[a+1][0] == "#" and conNum2(num,splitt[a+1][1:])):
                    print(splitt[a+1])
                    imm = dfNem[['IMM']]
                    #arregl01.append(j)
                    arregl01.append(transHex(splitt[a+1][1:],0))    
                #    aux = splitt[a+1]
                #    print(aux)
                #    #print(f"{j} {splitt[a+1]}")
                if((a+1) < len(splitt) and splitt[a+1][0] == "$" and (compar(j,directivas) != True and len(splitt[a+1]) == 5) and conNum2(Hex,splitt[a+1][1:])):
                    ext = dfNem[['EXT']]
                #    #arregl01.append(j)
                    arregl01.append(sacaDato(ext))
                    arregl01.append(splitt[a+1][1:])
                #    #print(f"{j} {splitt[a+1]}")
                if((a+1) < len(splitt) and len(splitt[a+1]) == 4 and conNum(4,num,splitt[a+1])  == 4 and (compar(j,directivas) != True)):
                    ext = dfNem[['EXT']]
                #    #arregl01.append(j)
                    arregl01.append(sacaDato(ext))
                    arregl01.append(transHex(splitt[a+1],0))
                #    #print(f"{j} {splitt[a+1]}")
                #if((a+1) < len(splitt) and splitt[a+1][0] == "$" and (compar(j,directivas) != True) and len(splitt[a+1]) == 3 ):
                    #dire = dfNem[['DIR']]
                #    #arregl01.append(j)
                    #arregl01.append(sacaDato(dire))
                #    arregl01.append(splitt[a+1][1:])
                #    #print(f"{j} {splitt[a+1]}")
                #if((a+1) < len(splitt) and len(splitt[a+1]) == 2 and conNum(2,num,splitt[a+1])  == 2 and (compar(j,directivas) != True)):
                #    dire = dfNem[['DIR']]
                #    #arregl01.append(j)
                #    arregl01.append(sacaDato(dire))
                #    arregl01.append(Hex(splitt[a+1]))
                #    #print(f"{j} {splitt[a+1]}")
                ##print(splitt)
                #print(len(splitt[a+1]))
                #if((a+1) < len(splitt) and splitt[a+1] == ("#"+str(j))):
                    #print(f"{j} {splitt[a+1]}")
                #if((a+1) < len(splitt) and (splitt[a+1] == (str(j)+",X") or splitt[a+1] == (str(j)+",Y"))):
                    #print(f"{j} {splitt[a+1]}")
                #if((a+1) < len(splitt) and (splitt[a+1] == (str(j)+",X") or splitt[a+1] == (str(j)+",Y"))):
                    #print(f"{j} {splitt[a+1]}")
            else:
                formatoS19(linea,"","",j)
                a=a+1
            #print(j)
        linea+=1
    
    #print(inh)
    #print(var)
    print(linea)
    print(arregl01)
    print(arrS19)


with open("archiv01.lst","a") as archivo:
    while res != 10:
        archivo.write(f"\n")
        res = 10
#exept Exception as e:
    #print(f'Exception - Ocurrió un error: {e} , {type(e)}, {}')
    
    #________________________________________________________________________________
import pandas as pd
#Arreglos y listas
excel = 'proyecto.xls' #Excel de mnemonicos
operativas = ["org","equ","fcb","end"] #operativas
Hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"] #Arr para verificacion de hexadecimal
num = ["0","1","2","3","4","5","6","7","8","9"] #Arr para verificacion de hexadecimal
arregl01 = [] #Provisional para pruebas
arrS19 = [] #Provisional para pruebas
var = {} #Diccionario de variables
const = {} #Dicc de constante
etique = {}
res = 0
df = pd.read_excel(excel, sheet_name='Hoja1') #Dataframe generado a partir del excel para compraraciones

#Obtiene el opcode deseado del renglon del dataframe
def getOpCode(arreglo):
    arr = ""
    for i in arreglo.values:
        arr = i[0]
    #print(arr)
    return str(arr)

#Compara si dato es contenido en arr
def comparDire(dato,arr):
    veri = "a"
    for i in arr:
        if (i == dato and len(i) == len(dato)):
            veri = "b"
        print(f"{i} {j}  {veri} {len(dato)}")
    print(veri)
    return res

#n = tamano esperado, arr = arreglo a comparar, dato = dato comparado
#Verfica tamano y que sea un numero. Puede ser 16 o 8 bits
def conNum(n,arr,dato):
    count1 = 0
    for i in range(n):
        for j in arr:
            if dato[i] == j:
                count1=count1+1
    return count1

#Verificar si hexa o un numero(?)
def conNum2(arr,dato):
    count1 = 0
    ret = False
    for i in dato:
        for j in arr:
            if i == str(j):
                count1=count1+1
            if count1 == len(dato):
                ret = True
    return ret

#Transformar hexadecimal
# dato= dato a transformar
# intt= 0 si es transformacion, 1 si es verificacion
def transHex(dato,intt):
    if(intt == 0):
        aux = str(hex(int(dato)[2:]))
        if len(aux) == 1:
            aux = "0" + aux
        elif len(aux) == 3:
            aux = "0" + aux[0] + " " + aux[1:]
        return aux.upper()
    if(intt == 1):
        aux = dato
        if len(aux) == 1:
            aux = "0" + aux
        elif len(aux) == 3:
            aux = "0" + aux[0] + " " + aux[1:] 
        return aux.upper()
    if(intt == 3):
        aux = str(hex(int(dato)))[2:]
        if len(aux) == 1:
            aux = "0" + aux
        elif len(aux) == 3:
            aux = "0" + aux[0] + " " + aux[1:]
        return aux.upper()

#Estructurar el LST
#linea = linea actual, mnemonico = opcode, oper = operando, lineaCom= linea completa
def formatoLST(lineas,mnemonico,oper,lineaCom):
    aux = ""
    if (len(str(oper)) != 0 and  len(mnemonico) != 0 ):
        aux = str(lineas)+" : ("+mnemonico+oper+") :" + lineaCom
        arrS19.append(aux.upper())
    elif(len(str(oper)) != 0 and  len(mnemonico) == 0 ):
        aux = str(lineas)+" : ("+mnemonico+oper+") :" + lineaCom
        arrS19.append(aux.upper())
    elif(len(str(oper)) == 0 and  len(mnemonico) != 0 ):
        aux = str(lineas)+" : ("+mnemonico+oper+") :" + lineaCom
        arrS19.append(aux.upper())
    else:
        aux = str(lineas)+" : " + lineaCom
        arrS19.append(aux.upper())


with open("EJEMPLO.asc") as archivoASC:
    linea = 1 #contador para lineas
    for i in archivoASC:#lee el archivo y realiza un ciclo
        a=0 #posicion splitt
        splitt = str(i.lower()).split()
        if(str(len(splitt)) == "0"):
            formatoLST(linea,"","","\n")   
        for j in splitt:
            if(str(len(splitt)) == "0"):
                formatoLST(linea,"","","")
                break
            #if ignora comentarios y lineas vacias
            elif len(splitt) != 0 and j[0]!="*" and (a+1) <= len(splitt) and splitt[0]!="*":
                #Construye dicc var
                if  len(splitt) > 1 and splitt[1]==operativas[1] and j[0:3]=="$00":
                    var[splitt[0]]=splitt[2]  
                    formatoLST(linea,"","",i) 
                    break
                #Construye dicc const
                elif  len(splitt) > 1 and splitt[1]==operativas[1] and j[0:2]=="$1":
                    const[splitt[0]]=splitt[2]
                    formatoLST(linea,"","",i)
                    break 
                dfNem=df[df["MNEMONICO"]==str(j.lower())]
                #if para INH
                #if (((a+1) == len(splitt) or ((a+1) <= len(splitt) and splitt[a+1][0]=="*" )) and len(dfNem) != 0  ):
                if ((a+1) == len(splitt)  and len(dfNem) != 0  ):
                    if(i[0] == " " ):
                        inh = dfNem[['INH']]
                        #arregl01.append(j)
                        arregl01.append(getOpCode(inh))
                        formatoLST(linea,getOpCode(inh),"",i)
                        break
                    else:
                        etique[splitt[0]] = ["G"]
                        formatoLST(linea,"","",i)
                        break 
                elif((a+1) == len(splitt)  and len(dfNem) == 0 and i[0]!="*" and i[0]!="#" and i[0]!="$"):
                        etique[splitt[0]] = ["G"]
                        formatoLST(linea,"","",i) 
                        break
                    #formatoLST(linea,getOpCode(inh),a,j)
                    #print(f"{j} {getOpCode(inh)} ")
                #ARREGLAR PARA CASO DE COMENTARIOS EN FINAL DE LINEA. HACER FUNCION ISCOMMENT?
                ##if IMM
                #elif ((a+1) < len(splitt) and splitt[a+1][0:2] == "#$" and conNum2(Hex,splitt[a+1][2:])):
                #    imm = dfNem[['IMM']]
                #    arregl01.append(getOpCode(imm))
                #    arregl01.append(transHex(splitt[a+1][2:],1)) 
                #    formatoLST(linea,getOpCode(imm),transHex(splitt[a+1][2:],1),i)
                #    break
                ##if IMM PERO SIN $
                #elif ((a+1) < len(splitt) and splitt[a+1][0] == "#" and conNum2(num,splitt[a+1][1:])):
                #    imm = dfNem[['IMM']]
                #    arregl01.append(transHex(splitt[a+1][1:],0))
                #    formatoLST(linea,getOpCode(imm),transHex(splitt[a+1][1:],0),i)
                #    break
                ##if EXT
                #elif(((a+1) < len(splitt)) and (splitt[a+1][0] == "$") and (len(splitt[a+1]) == 5) and (conNum(3,operativas,j)== 3) and (conNum2(Hex,splitt[a+1][1:]) == True) ):
                #        ext = dfNem[['EXT']]
                #        arregl01.append(getOpCode(ext))
                #        arregl01.append(splitt[a+1][1:])
                #        formatoLST(linea,getOpCode(ext),splitt[a+1][1:],i)
                #        break
                ##if EXT
                #elif((a+1) < len(splitt) and len(splitt[a+1]) == 4 and conNum(4,num,splitt[a+1])  == 4 ):
                #    ext = dfNem[['EXT']]
                #    arregl01.append(getOpCode(ext))
                #    arregl01.append(transHex(splitt[a+1],0))
                #    formatoLST(linea,getOpCode(ext),transHex(splitt[a+1],0),i)
                #    break
                #elif((a+1) < len(splitt) and splitt[a+1][0] == "$" and (conNum2(Hex,splitt[a+1][1:]) == True) and len(splitt[a+1]) == 3 ):
                #    dire = dfNem[['DIR']]
                #    arregl01.append(getOpCode(dire))
                #    arregl01.append(splitt[a+1][1:])
                #    formatoLST(linea,getOpCode(dire),splitt[a+1][1:],i)
                #    break
                #elif((a+1) < len(splitt) and len(splitt[a+1]) == 2 and conNum(2,num,splitt[a+1])  == 2 ):
                #    dire = dfNem[['DIR']]
                #    print(f"{j} {getOpCode(dire)} {transHex(splitt[a+1],3)}")
                #    arregl01.append(getOpCode(dire))
                #    arregl01.append(transHex(splitt[a+1],3))
                #    formatoLST(linea,getOpCode(dire),transHex(splitt[a+1],3),i)
                #    break
                #elif((a+1) < len(splitt) and splitt[a+1][0] == "$" and (conNum2(Hex,splitt[a+1][1:3]) == True) and splitt[a+1][3:5] == ",x" ):
                #    indX = dfNem[['IND,X']]
                #    arregl01.append(getOpCode(indX))
                #    arregl01.append(splitt[a+1][1:3])
                #    formatoLST(linea,getOpCode(indX),splitt[a+1][1:3],i)
                #    break
                #elif((a+1) < len(splitt) and splitt[a+1][0] == "$" and (conNum2(Hex,splitt[a+1][1:3]) == True) and splitt[a+1][3:5] == ",y" ):
                #    indY = dfNem[['IND,Y']]
                #    arregl01.append(getOpCode(indY))
                #    arregl01.append(splitt[a+1][1:3])
                #    formatoLST(linea,getOpCode(indY),splitt[a+1][1:3],i)
                #    break
                elif((a+1) < len(splitt) and len(dfNem) != 0 and conNum2(etique.keys,splitt[a+1]) == True ):
                    print(f"{splitt[a]} {splitt[a+1]}")
                    rel = dfNem[['REL']]
                    break
            else:
                if (a==0):
                    formatoLST(linea,"","",i)
                a=a+1
        linea=linea + 1
    print(arregl01)
    #print(arrS19)


with open("archiv01.lst","a") as archivo:
    for i in arrS19:
        archivo.write(i)

#exept Exception as e:
    #print(f'Exception - Ocurrió un error: {e} , {type(e)}, {}')
