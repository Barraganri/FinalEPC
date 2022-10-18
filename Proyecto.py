import pandas as pd
#Arreglos y listas
excel = 'proyecto.xls' #Excel de mnemonicos
operativas = ["org","equ","fcb","end"] #operativas
Hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"] #Arr para verificacion de hexadecimal
num = ["0","1","2","3","4","5","6","7","8","9"] #Arr para verificacion de hexadecimal
excep = ["jsr","jmp","brclr","brset","bclr","bset"]
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
        aux = str(hex(int(dato)))[2:]
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
        arrS19.append(aux)
    elif(len(str(oper)) != 0 and  len(mnemonico) == 0 ):
        aux = str(lineas)+" : ("+mnemonico+oper+") :" + lineaCom
        arrS19.append(aux)
    elif(len(str(oper)) == 0 and  len(mnemonico) != 0 ):
        aux = str(lineas) +" : ("+mnemonico+oper+") :" + lineaCom
        arrS19.append(aux)
    else:
        aux = str(lineas)+" : VACIO : " + lineaCom
        arrS19.append(aux)

def etiquetas():
    auxEtique = {}
    with open("BURBUJA.asc") as archivoASC:
        for i in archivoASC:#lee el archivo y realiza un ciclo
            splitt = str(i.lower()).split()
            if len(splitt) != 0 and (1) <= len(splitt) and splitt[0][0]!="*":
                dfNem=df[df["MNEMONICO"]==str(splitt[0].lower())]
                if ((1) <= len(splitt) and len(dfNem) != 0  ):
                    if(i[0] != " " and (1) == len(splitt) and len(dfNem) != 0):
                        auxEtique[splitt[0]] = [""]
                    elif(i[0] != " " and len(dfNem) != 0 and (1) <= len(splitt) and splitt[1][0] == "*"):
                        auxEtique[splitt[0]] = [""]
                    elif(i[0] != " "):
                        print(f"ERROR 009  ")
                elif((1) == len(splitt)  and len(dfNem) == 0 and i[0] != " " and i[0]!="*" and i[0]!="#" and i[0]!="$" and len(dfNem) == 0):
                    auxEtique[splitt[0]] = [""]
    return auxEtique

def iterador(arreglo, dato):
    a = 0
    for x in arreglo:
        if x == dato:
            a = 1
    return a
            

with open("BURBUJA.asc") as archivoASC:
    linea = 1 #contador para lineas
    etique=etiquetas()
    for i in archivoASC:#lee el archivo y realiza un ciclo
        splitt = str(i.lower()).split()
        if(str(len(splitt)) == "0"):
            formatoLST(linea,"","","\n")   
        #if ignora comentarios y lineas vacias
        elif len(splitt) != 0 and splitt[0][0]!="*" and (1) <= len(splitt):
            #Construye dicc var
            if  len(splitt) > 1 and splitt[1]==operativas[1] and splitt[2][0:3]=="$00":
                var[splitt[0]]=splitt[2][1:]  
                formatoLST(linea,"","",i) 
            #Construye dicc const
            elif  len(splitt) > 1 and splitt[1]==operativas[1] and splitt[2][0:2]=="$1":
                const[splitt[0]]=splitt[2][1:]
                formatoLST(linea,"","",i) 
            dfNem=df[df["MNEMONICO"]==str(splitt[0])]
            #if para INH
            #if (((a+1) == len(splitt) or ((a+1) <= len(splitt) and splitt[a+1][0]=="*" )) and len(dfNem) != 0  ):
            if ((1) == len(splitt)  and len(dfNem) != 0  ):
                if(i[0] == " " ):
                    inh = dfNem[['INH']]
                    #arregl01.append(j)
                    arregl01.append(getOpCode(inh))
                    formatoLST(linea,getOpCode(inh),"",i)
                else:
                    formatoLST(linea,"","",i) 
            elif((1) == len(splitt)  and len(dfNem) == 0 and i[0]!="*" and i[0]!="#" and i[0]!="$"):
                    formatoLST(linea,"","",i) 
            elif((1) < len(splitt) and splitt[1][0]=="*" and len(dfNem) != 0 ):
                if(i[0] == " " ):
                    inh = dfNem[['INH']]
                    #arregl01.append(j)
                    arregl01.append(getOpCode(inh))
                    formatoLST(linea,getOpCode(inh),"",i)
                else:
                    formatoLST(linea,"","",i)
                #formatoLST(linea,getOpCode(inh),a,j)
                #print(f"{j} {getOpCode(inh)} ")
            #ARREGLAR PARA CASO DE COMENTARIOS EN FINAL DE LINEA. HACER FUNCION ISCOMMENT?
            #if IMM
            elif ((1) < len(splitt) and splitt[1][0:2] == "#$" and conNum2(Hex,splitt[1][2:])):
                imm = dfNem[['IMM']]
                arregl01.append(getOpCode(imm))
                arregl01.append(transHex(splitt[1][2:],1)) 
                formatoLST(linea,getOpCode(imm),transHex(splitt[1][2:],1),i)
            #if IMM PERO SIN $
            elif ((1) < len(splitt) and splitt[1][0] == "#"):
                if(conNum2(num,splitt[1][1:])):
                    imm = dfNem[['IMM']]
                    arregl01.append(getOpCode(imm))
                    arregl01.append(transHex(splitt[1][1:],0))
                    formatoLST(linea,getOpCode(imm),transHex(splitt[1][1:],0),i)
                elif(splitt[1][0:2] == "#'"):
                    imm = dfNem[['IMM']]
                    arregl01.append(getOpCode(imm))
                    auxSplit = i.split()
                    arregl01.append(transHex(ord(auxSplit[1][2:]),0))
                    formatoLST(linea,getOpCode(imm),transHex(ord(auxSplit[1][2:]),3),i)
                elif(iterador(var.keys(),splitt[1][1:]) == 1):
                    imm = dfNem[['IMM']]
                    arregl01.append(getOpCode(imm))
                    arregl01.append(var[splitt[1][1:]])
                    formatoLST(linea,getOpCode(imm),var[splitt[1][1:]],i)
                elif(iterador(const.keys(),splitt[1][1:]) == 1):
                    imm = dfNem[['IMM']]
                    arregl01.append(getOpCode(imm))
                    arregl01.append(const[splitt[1][1:]])
                    formatoLST(linea,getOpCode(imm),const[splitt[1][1:]],i)
            #if EXT
            elif(((1) < len(splitt)) and (splitt[1][0] == "$") and (len(splitt[1]) == 5) and (conNum(3,operativas,splitt[1])== 3) and (conNum2(Hex,splitt[1][1:]) == True) ):
                ext = dfNem[['EXT']]
                arregl01.append(getOpCode(ext))
                arregl01.append(splitt[1][1:])
                formatoLST(linea,getOpCode(ext),splitt[1][1:],i)
            #if EXT
            elif((1) < len(splitt) and len(dfNem) != 0 and ((len(splitt[1]) == 4 and conNum(4,num,splitt[1])  == 4)or iterador(const.keys(),splitt[1]) == 1 )):
                if(len(splitt[1]) == 4 and conNum(4,num,splitt[1])  == 4):
                    ext = dfNem[['EXT']]
                    arregl01.append(getOpCode(ext))
                    arregl01.append(transHex(splitt[1],0))
                    formatoLST(linea,getOpCode(ext),transHex(splitt[1],0),i)
                elif(iterador(const.keys(),splitt[1]) == 1):
                    ext = dfNem[['EXT']]
                    arregl01.append(getOpCode(ext))
                    arregl01.append(const[splitt[1]])
                    formatoLST(linea,getOpCode(ext),const[splitt[1]],i)
            elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:]) == True) and len(splitt[1]) == 3 ):
                dire = dfNem[['DIR']]
                arregl01.append(getOpCode(dire))
                arregl01.append(splitt[1][1:])
                formatoLST(linea,getOpCode(dire),splitt[1][1:],i)
            elif((1) < len(splitt) and len(dfNem) != 0 and (len(splitt[1]) == 2 or iterador(var.keys(),splitt[1]) == 1)):
                if(len(splitt[1]) == 2 and conNum(2,num,splitt[1])  == 2 ):
                    dire = dfNem[['DIR']]
                    arregl01.append(getOpCode(dire))
                    arregl01.append(transHex(splitt[1],3))
                    formatoLST(linea,getOpCode(dire),transHex(splitt[1],3),i)
                elif(iterador(var.keys(),splitt[1]) == 1):
                    dire = dfNem[['DIR']]
                    if(getOpCode(dire) == "-- "):
                        ext = dfNem[['EXT']]
                        arregl01.append(getOpCode(ext))
                        arregl01.append(var[splitt[1]])
                        formatoLST(linea,getOpCode(ext),var[splitt[1]],i)
                    else:    
                        arregl01.append(getOpCode(dire))
                        arregl01.append(var[splitt[1]][2:])
                        formatoLST(linea,getOpCode(dire),var[splitt[1]][2:],i)
            elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:3]) == True) and len(splitt[1]) == 8 ):
                if((2) < len(splitt) and splitt[1][3:6] == ",#$" and iterador(etique.keys(),splitt[2]) == 1 and (splitt[0] == excep[2] or splitt[0] == excep[3])):
                    dire = dfNem[['DIR']]
                    arregl01.append(getOpCode(dire))
                    arregl01.append(splitt[1][1:3] + splitt[1][6:8]+"REL")
                    formatoLST(linea,getOpCode(dire),splitt[1][1:3]+ splitt[1][6:8]+"REL",i)
                elif((1) < len(splitt) and  splitt[1][3:6] == ",#$" and (splitt[0] == excep[4] or splitt[0] == excep[5])):
                    dire = dfNem[['DIR']]
                    arregl01.append(getOpCode(dire))
                    arregl01.append(splitt[1][1:3] + splitt[1][6:8])
                    formatoLST(linea,getOpCode(dire),splitt[1][1:3]+ splitt[1][6:8],i)
            elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:3]) == True) and splitt[1][3:5] == ",x" ):
                if(len(splitt[1]) == 5 ):
                   indX = dfNem[['IND,X']]
                   arregl01.append(getOpCode(indX))
                   arregl01.append(splitt[1][1:3])
                   formatoLST(linea,getOpCode(indX),splitt[1][1:3],i)
                #sera relativo tambien
                elif((2) < len(splitt) and len(splitt[1]) == 10 and splitt[1][3:8] == ",x,#$" and iterador(etique.keys(),splitt[2]) == 1 and (splitt[0] == excep[2] or splitt[0] == excep[3])):
                    indX = dfNem[['IND,X']]
                    arregl01.append(getOpCode(indX))
                    arregl01.append(splitt[1][1:3] + splitt[1][8:10]+"REL")
                    formatoLST(linea,getOpCode(indX),splitt[1][1:3]+ splitt[1][8:10]+"REL",i)
                elif((1) < len(splitt) and (splitt[0] == excep[4] or splitt[0] == excep[5])):
                    indX = dfNem[['IND,X']]
                    arregl01.append(getOpCode(indX))
                    arregl01.append(splitt[1][1:3] + splitt[1][8:10])
                    formatoLST(linea,getOpCode(indX),splitt[1][1:3]+ splitt[1][8:10],i)
            elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:3]) == True) and splitt[1][3:5] == ",y" ):
                if(len(splitt[1]) == 5 ):
                    indY = dfNem[['IND,Y']]
                    arregl01.append(getOpCode(indY))
                    arregl01.append(splitt[1][1:3])
                    formatoLST(linea,getOpCode(indY),splitt[1][1:3],i)
                #sera relativo tambien
                elif((2) < len(splitt) and len(splitt[1]) == 10 and splitt[1][3:8] == ",y,#$" and iterador(etique.keys(),splitt[2]) == 1 and (splitt[0] == excep[3] or splitt[0] == excep[4])):
                    indY = dfNem[['IND,Y']]
                    arregl01.append(getOpCode(indY))
                    arregl01.append(splitt[1][1:3] + splitt[1][8:10]+"REL")
                    formatoLST(linea,getOpCode(indY),splitt[1][1:3]+ splitt[1][8:10]+"REL",i)
                elif((1) < len(splitt) and (splitt[0] == excep[5] or splitt[0] == excep[6])):
                    indY = dfNem[['IND,Y']]
                    arregl01.append(getOpCode(indY))
                    arregl01.append(splitt[1][1:3] + splitt[1][8:10])
                    formatoLST(linea,getOpCode(indY),splitt[1][1:3]+ splitt[1][8:10],i)
            elif((1) < len(splitt) and len(dfNem) != 0 and iterador(etique.keys(),splitt[1]) == 1):
                rel = dfNem[['REL']]
                if(getOpCode(rel) == "-- " and (splitt[0] == excep[0] or splitt[0] == excep[1])):
                    ext = dfNem[['EXT']]
                    arregl01.append(getOpCode(ext))
                    arregl01.append("")
                    formatoLST(linea,getOpCode(ext),"REL",i)
                else: 
                    arregl01.append(getOpCode(rel))
                    formatoLST(linea,getOpCode(rel),"REL",i)
            elif(iterador(operativas,splitt[0]) == 1 ):
                if(splitt[0]==operativas[0]):
                    formatoLST(linea,"","",i)
                elif(splitt[0]==operativas[2]):
                    formatoLST(linea,splitt[1][1:3],splitt[1][5:7],i)
                elif(splitt[0]==operativas[3]):
                    formatoLST(linea,"","",i)
            elif((2) < len(splitt)  and iterador(operativas,splitt[1]) == 1 ):
                if(splitt[1]==operativas[2]):
                    formatoLST(linea,splitt[2][1:3],splitt[2][5:7],i)
        else:
            formatoLST(linea,"","",i)
        linea=linea + 1
    print(arregl01)
    #print(arrS19)

with open("archiv01.lst","a") as archivo:
    for i in arrS19:
        archivo.write(i)

#exept Exception as e:
    #print(f'Exception - Ocurrió un error: {e} , {type(e)}, {}')
