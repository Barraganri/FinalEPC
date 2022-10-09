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
def compar(dato,arr):
    res = False
    for i in arr:
        if i == dato:
            res = True
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
        return aux
    if(intt == 1):
        aux = dato
        if len(aux) == 1:
            aux = "0" + aux
        elif len(aux) == 3:
            aux = "0" + aux[0] + " " + aux[1:] 
        return aux

#Estructurar el LST
#linea = linea actual, mnemonico = opcode, oper = operando, lineaCom= linea completa
def formatoLST(lineas,mnemonico,oper,lineaCom):
    aux = ""
    if (len(oper) != 0 and  len(mnemonico) != 0 ):
        aux = str(lineas)+": ("+mnemonico+oper+") " + lineaCom
        arrS19.append(aux)
    else:
        aux = str(lineas)+": " + lineaCom
        arrS19.append(aux)


with open("EJEMPLO.asc") as archivoASC:
    linea = 0 #contador para lineas
    for i in archivoASC:#lee el archivo y realiza un ciclo
        a=0 #posicion splitt
        splitt = str(i.lower()).split()
        for j in splitt:
            #if ignora comentarios y lineas vacias
            if len(splitt) != 0 and j[0]!="*" and (a+1) <= len(splitt) :
                #Construye dicc var
                if  len(splitt) > 1 and splitt[1]==operativas[1] and j[1:3]=="00":
                    var[splitt[0]]=splitt[2]
                    break
                #Construye dicc const
                elif  len(splitt) > 1 and splitt[1]==operativas[1] and j[1]=="1":
                    const[splitt[0]]=splitt[2]
                    break
                dfNem=df[df["MNEMONICO"]==str(j.lower())]
                #if para INH
                if ((a+1) == len(splitt) and len(dfNem) != 0 ):
                    inh = dfNem[['INH']]
                    #arregl01.append(j)
                    arregl01.append(getOpCode(inh))
                    formatoLST(linea,getOpCode(inh),a,j)
                    #print(f"{j} {getOpCode(inh)} ")
                #ARREGLAR PARA CASO DE COMENTARIOS EN FINAL DE LINEA. HACER FUNCION ISCOMMENT?
                #if IMM
                if ((a+1) < len(splitt) and splitt[a+1][0:2] == "#$" and conNum2(Hex,splitt[a+1][2:])):
                    imm = dfNem[['IMM']]
                    #arregl01.append(j)
                    arregl01.append(getOpCode(imm))
                    arregl01.append(transHex(splitt[a+1][2:],1)) 
                    #print(f"{j} {splitt[a+1]}")
                #if IMM PERO SIN $
                if ((a+1) < len(splitt) and splitt[a+1][0] == "#" and conNum2(num,splitt[a+1][1:])):
                    print(splitt[a+1])
                    imm = dfNem[['IMM']]
                    #arregl01.append(j)
                    arregl01.append(transHex(splitt[a+1][1:],0))    
                #    aux = splitt[a+1]
                #    print(aux)
                #    #print(f"{j} {splitt[a+1]}")
                #if EXT
                if((a+1) < len(splitt) and splitt[a+1][0] == "$" and (compar(j,operativas) != True and len(splitt[a+1]) == 5) and conNum2(Hex,splitt[a+1][1:])):
                    ext = dfNem[['EXT']]
                #    #arregl01.append(j)
                    arregl01.append(getOpCode(ext))
                    arregl01.append(splitt[a+1][1:])
                #    #print(f"{j} {splitt[a+1]}")
                #if EXT
                if((a+1) < len(splitt) and len(splitt[a+1]) == 4 and conNum(4,num,splitt[a+1])  == 4 and (compar(j,operativas) != True)):
                    ext = dfNem[['EXT']]
                #    #arregl01.append(j)
                    arregl01.append(getOpCode(ext))
                    arregl01.append(transHex(splitt[a+1],0))
                #    #print(f"{j} {splitt[a+1]}")
                #if((a+1) < len(splitt) and splitt[a+1][0] == "$" and (compar(j,operativas) != True) and len(splitt[a+1]) == 3 ):
                    #oper = dfNem[['DIR']]
                #    #arregl01.append(j)
                    #arregl01.append(getOpCode(oper))
                #    arregl01.append(splitt[a+1][1:])
                #    #print(f"{j} {splitt[a+1]}")
                #if((a+1) < len(splitt) and len(splitt[a+1]) == 2 and conNum(2,num,splitt[a+1])  == 2 and (compar(j,operativas) != True)):
                #    oper = dfNem[['DIR']]
                #    #arregl01.append(j)
                #    arregl01.append(getOpCode(oper))
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
                formatoLST(linea,"","",j)
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
