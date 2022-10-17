from msilib.schema import Directory
import pandas as pd
#Arreglos y listas
excel = 'proyecto.xls' #Excel de mnemonicos
operativas = ["org","equ","fcb","end"] #operativas
Hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"] #Arr para verificacion de hexadecimal
num = ["0","1","2","3","4","5","6","7","8","9"] #Arr para verificacion de hexadecimal
excep = ["clr","jsr","jmp","brclr","brset","bclr","bset"]
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
            a=0 #posicion splitt
            splitt = str(i.lower()).split()
            for j in splitt:
                if len(splitt) != 0 and j[0]!="*" and (a+1) <= len(splitt) and splitt[0]!="*":
                    dfNem=df[df["MNEMONICO"]==str(j.lower())]
                    #if para INH
                    #if (((a+1) == len(splitt) or ((a+1) <= len(splitt) and splitt[a+1][0]=="*" )) and len(dfNem) != 0  ):
                    if ((a+1) == len(splitt)  and len(dfNem) != 0  ):
                        if(i[0] == " " ):
                            break
                        else:
                            auxEtique[splitt[0]] = ["G"]
                            break 
                    elif((a+1) == len(splitt)  and len(dfNem) == 0 and i[0]!="*" and i[0]!="#" and i[0]!="$"):
                            auxEtique[splitt[0]] = ["G"]
                            break
                else:
                    a=a+1
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
                    var[splitt[0]]=splitt[2][1:]  
                    formatoLST(linea,"","",i) 
                    break
                #Construye dicc const
                elif  len(splitt) > 1 and splitt[1]==operativas[1] and j[0:2]=="$1":
                    const[splitt[0]]=splitt[2][1:]
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
                        formatoLST(linea,"","",i)
                        break 
                elif((a+1) == len(splitt)  and len(dfNem) == 0 and i[0]!="*" and i[0]!="#" and i[0]!="$"):
                        formatoLST(linea,"","",i) 
                        break
                elif((a+1) < len(splitt) and splitt[a+1][0]=="*" and len(dfNem) != 0 ):
                    if(i[0] == " " ):
                        inh = dfNem[['INH']]
                        #arregl01.append(j)
                        arregl01.append(getOpCode(inh))
                        formatoLST(linea,getOpCode(inh),"",i)
                        break
                    else:
                        formatoLST(linea,"","",i)
                        break
                    #formatoLST(linea,getOpCode(inh),a,j)
                    #print(f"{j} {getOpCode(inh)} ")
                #ARREGLAR PARA CASO DE COMENTARIOS EN FINAL DE LINEA. HACER FUNCION ISCOMMENT?
                #if IMM
                elif ((a+1) < len(splitt) and splitt[a+1][0:2] == "#$" and conNum2(Hex,splitt[a+1][2:])):
                    imm = dfNem[['IMM']]
                    arregl01.append(getOpCode(imm))
                    arregl01.append(transHex(splitt[a+1][2:],1)) 
                    formatoLST(linea,getOpCode(imm),transHex(splitt[a+1][2:],1),i)
                    break
                #if IMM PERO SIN $
                elif ((a+1) < len(splitt) and splitt[a+1][0] == "#"):
                    if(conNum2(num,splitt[a+1][1:])):
                        imm = dfNem[['IMM']]
                        arregl01.append(getOpCode(imm))
                        arregl01.append(transHex(splitt[a+1][1:],0))
                        formatoLST(linea,getOpCode(imm),transHex(splitt[a+1][1:],0),i)
                        break
                    if(splitt[a+1][0:2] == "#'"):
                        imm = dfNem[['IMM']]
                        arregl01.append(getOpCode(imm))
                        auxSplit = i.split()
                        arregl01.append(transHex(ord(auxSplit[a+1][2:]),0))
                        formatoLST(linea,getOpCode(imm),transHex(ord(auxSplit[a+1][2:]),3),i)
                        break
                    elif(iterador(var.keys(),splitt[a+1][1:]) == 1):
                        imm = dfNem[['IMM']]
                        arregl01.append(getOpCode(imm))
                        arregl01.append(var[splitt[a+1][1:]])
                        formatoLST(linea,getOpCode(imm),var[splitt[a+1][1:]],i)
                        break
                    elif(iterador(const.keys(),splitt[a+1][1:]) == 1):
                        imm = dfNem[['IMM']]
                        arregl01.append(getOpCode(imm))
                        arregl01.append(const[splitt[a+1][1:]])
                        formatoLST(linea,getOpCode(imm),const[splitt[a+1][1:]],i)
                        break
                #if EXT
                elif(((a+1) < len(splitt)) and (splitt[a+1][0] == "$") and (len(splitt[a+1]) == 5) and (conNum(3,operativas,j)== 3) and (conNum2(Hex,splitt[a+1][1:]) == True) ):
                    ext = dfNem[['EXT']]
                    arregl01.append(getOpCode(ext))
                    arregl01.append(splitt[a+1][1:])
                    formatoLST(linea,getOpCode(ext),splitt[a+1][1:],i)
                    break
                #if EXT
                elif((a+1) < len(splitt) and len(dfNem) != 0 and ((len(splitt[a+1]) == 4 and conNum(4,num,splitt[a+1])  == 4)or iterador(const.keys(),splitt[a+1]) == 1 )):
                    if(len(splitt[a+1]) == 4 and conNum(4,num,splitt[a+1])  == 4):
                        ext = dfNem[['EXT']]
                        arregl01.append(getOpCode(ext))
                        arregl01.append(transHex(splitt[a+1],0))
                        formatoLST(linea,getOpCode(ext),transHex(splitt[a+1],0),i)
                        break
                    elif(iterador(const.keys(),splitt[a+1]) == 1):
                        ext = dfNem[['EXT']]
                        arregl01.append(getOpCode(ext))
                        arregl01.append(const[splitt[a+1]])
                        formatoLST(linea,getOpCode(ext),const[splitt[a+1]],i)
                        break
                elif((a+1) < len(splitt) and splitt[a+1][0] == "$" and (conNum2(Hex,splitt[a+1][1:]) == True) and len(splitt[a+1]) == 3 ):
                    dire = dfNem[['DIR']]
                    arregl01.append(getOpCode(dire))
                    arregl01.append(splitt[a+1][1:])
                    formatoLST(linea,getOpCode(dire),splitt[a+1][1:],i)
                    break
                elif((a+1) < len(splitt) and len(dfNem) != 0 and (len(splitt[a+1]) == 2 or iterador(var.keys(),splitt[a+1]) == 1)):
                    if(len(splitt[a+1]) == 2 and conNum(2,num,splitt[a+1])  == 2 ):
                        dire = dfNem[['DIR']]
                        arregl01.append(getOpCode(dire))
                        arregl01.append(transHex(splitt[a+1],3))
                        formatoLST(linea,getOpCode(dire),transHex(splitt[a+1],3),i)
                        break
                    elif(iterador(var.keys(),splitt[a+1]) == 1):
                        dire = dfNem[['DIR']]
                        if(getOpCode(dire) == "**"):
                            ext = dfNem[['EXT']]
                            arregl01.append(getOpCode(ext))
                            arregl01.append(var[splitt[a+1]])
                            formatoLST(linea,getOpCode(ext),var[splitt[a+1]],i)
                            break
                        else:    
                            arregl01.append(getOpCode(dire))
                            arregl01.append(var[splitt[a+1]][2:])
                            formatoLST(linea,getOpCode(dire),var[splitt[a+1]][2:],i)
                            break
                if((a+1) < len(splitt) and splitt[a+1][0] == "$" and (conNum2(Hex,splitt[a+1][1:3]) == True) and len(splitt[a+1]) == 8 ):
                    if((a+2) < len(splitt) and splitt[a+1][3:6] == ",#$" and iterador(etique.keys(),splitt[a+2]) == 1 and (splitt[a] == excep[3] or splitt[a] == excep[4])):
                        dire = dfNem[['DIR']]
                        arregl01.append(getOpCode(dire))
                        arregl01.append(splitt[a+1][1:3] + splitt[a+1][6:8]+"REL")
                        formatoLST(linea,getOpCode(dire),splitt[a+1][1:3]+ splitt[a+1][6:8]+"REL",i)
                        break
                    elif((a+1) < len(splitt) and  splitt[a+1][3:6] == ",#$" and (splitt[a] == excep[5] or splitt[a] == excep[6])):
                        dire = dfNem[['DIR']]
                        arregl01.append(getOpCode(dire))
                        arregl01.append(splitt[a+1][1:3] + splitt[a+1][6:8])
                        formatoLST(linea,getOpCode(dire),splitt[a+1][1:3]+ splitt[a+1][6:8],i)
                        break
                elif((a+1) < len(splitt) and splitt[a+1][0] == "$" and (conNum2(Hex,splitt[a+1][1:3]) == True) and splitt[a+1][3:5] == ",x" ):
                    if(len(splitt[a+1]) == 5 ):
                       indX = dfNem[['IND,X']]
                       arregl01.append(getOpCode(indX))
                       arregl01.append(splitt[a+1][1:3])
                       formatoLST(linea,getOpCode(indX),splitt[a+1][1:3],i)
                       break
                    #sera relativo tambien
                    elif((a+2) < len(splitt) and len(splitt[a+1]) == 10 and splitt[a+1][3:8] == ",x,#$" and iterador(etique.keys(),splitt[a+2]) == 1 and (splitt[a] == excep[3] or splitt[a] == excep[4])):
                        indX = dfNem[['IND,X']]
                        arregl01.append(getOpCode(indX))
                        arregl01.append(splitt[a+1][1:3] + splitt[a+1][8:10]+"REL")
                        formatoLST(linea,getOpCode(indX),splitt[a+1][1:3]+ splitt[a+1][8:10]+"REL",i)
                        break
                    elif((a+1) < len(splitt) and (splitt[a] == excep[5] or splitt[a] == excep[6])):
                        indX = dfNem[['IND,X']]
                        arregl01.append(getOpCode(indX))
                        arregl01.append(splitt[a+1][1:3] + splitt[a+1][8:10])
                        formatoLST(linea,getOpCode(indX),splitt[a+1][1:3]+ splitt[a+1][8:10],i)
                        break
                elif((a+1) < len(splitt) and splitt[a+1][0] == "$" and (conNum2(Hex,splitt[a+1][1:3]) == True) and splitt[a+1][3:5] == ",y" ):
                    if(len(splitt[a+1]) == 5 ):
                        indY = dfNem[['IND,Y']]
                        arregl01.append(getOpCode(indY))
                        arregl01.append(splitt[a+1][1:3])
                        formatoLST(linea,getOpCode(indY),splitt[a+1][1:3],i)
                        break
                    #sera relativo tambien
                    elif((a+2) < len(splitt) and len(splitt[a+1]) == 10 and splitt[a+1][3:8] == ",y,#$" and iterador(etique.keys(),splitt[a+2]) == 1 and (splitt[a] == excep[3] or splitt[a] == excep[4])):
                        indY = dfNem[['IND,Y']]
                        arregl01.append(getOpCode(indY))
                        arregl01.append(splitt[a+1][1:3] + splitt[a+1][8:10]+"REL")
                        formatoLST(linea,getOpCode(indY),splitt[a+1][1:3]+ splitt[a+1][8:10]+"REL",i)
                        break
                    elif((a+1) < len(splitt) and (splitt[a] == excep[5] or splitt[a] == excep[6])):
                        indY = dfNem[['IND,Y']]
                        arregl01.append(getOpCode(indY))
                        arregl01.append(splitt[a+1][1:3] + splitt[a+1][8:10])
                        formatoLST(linea,getOpCode(indY),splitt[a+1][1:3]+ splitt[a+1][8:10],i)
                        print(len(splitt[a+1]))
                        print(splitt[a+1])
                        print(splitt[a+1][7:10])
                        break
                elif((a+1) < len(splitt) and len(dfNem) != 0 and iterador(etique.keys(),splitt[a+1]) == 1):
                    rel = dfNem[['REL']]
                    arregl01.append(getOpCode(rel))
                    formatoLST(linea,getOpCode(rel),"",i)
                    break
                elif(iterador(operativas,splitt[0]) == 1 ):
                    if(splitt[a]==operativas[0]):
                        formatoLST(linea,"","",i)
                        break
                    elif(splitt[a]==operativas[2]):
                        formatoLST(linea,splitt[a+1][1:3],splitt[a+1][5:7],i)
                        break
                    elif(splitt[a]==operativas[3]):
                        formatoLST(linea,"","",i)
                        break
                elif((a+2) < len(splitt)  and iterador(operativas,splitt[a+1]) == 1 ):
                    if(splitt[a+1]==operativas[2]):
                        formatoLST(linea,splitt[a+2][1:3],splitt[a+2][5:7],i)
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
