import pandas as pd
# Para iniciar colorama
#Arreglos y listas
excel = 'proyecto (1).xls' #Excel de mnemonicos
operativas = ["org","equ","fcb","end"] #operativas
Hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"] #Arr para verificacion de hexadecimal
num = ["0","1","2","3","4","5","6","7","8","9"] #Arr para verificacion de hexadecimal
excep = ["jsr","jmp","brclr","brset","bclr","bset","bcc",'bcs',"beq","bge","bgt","bhi","bhs","ble","blo","bls","blt","bmi","bne","bpl","bra","brn","bsr","bvc","bvs"]
inhe = ["aba","abx","aby","asla","aslb","asld","asra","asrb","cba","clc","cli","clra","clrb","clv","coma","comb","daa","deca","decb","des","dex","dey","fdiv","idiv","inca","incb","ins","inx",
"iny","lsla","lslb","lsld","lsra","lsrb","lsrd","mul","nega","negb","nop","psha","pshb","pshx","pshy","pula","pulb","pulx","puly","rola","rolb","rora","rorb","rti","rts","sba","sec","sei",
"sev","stop","swi","tab","tap","tba","test","tpa","tsta","tstb","tsx","tsy","txs","tys","wai","xgdx","xgdy"]
relativoArre =[] # arreglo para agregar etiquetas y memoria para asignar los diccionarios de las etiquetas
arregl01 = [] #Provisional para pruebas
relDatos = [] #arreglo para los datos que se analisaran de forma relativa
arrS19 = [] #Provisional para pruebas
varYconst = {} #Diccionario de variables
etique = {}
memoria = 0
end = 0
df = pd.read_excel(excel, sheet_name='Hoja1') #Dataframe generado a partir del excel para compraraciones
dfB = pd.read_excel(excel, sheet_name='Hoja2') #Dataframe generado a partir del excel para compraraciones de byts

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
            aux = "0" + aux[0] + aux[1:]
        return aux.upper()
    if(intt == 1):
        aux = dato
        if len(aux) == 1:
            aux = "0" + aux
        elif len(aux) == 3:
            aux = "0" + aux[0] + aux[1:] 
        return aux.upper()
    if(intt == 3):
        aux = str(hex(int(dato)))[2:]
        if len(aux) == 1:
            aux = "0" + aux
        elif len(aux) == 3:
            aux = "0" + aux[0] + aux[1:]
        return aux.upper()

#Estructurar el LST
#linea = linea actual, mnemonico = opcode, oper = operando, lineaCom= linea completa
def formatoLST(lineas,mnemonico,oper,lineaCom):
    aux = ""
    if (len(str(oper)) != 0 and  len(mnemonico) != 0 ):
        aux = f"{str(lineas)} : {transHex(memoria,0)} ({mnemonico}{oper}) : {lineaCom}"
        arrS19.append(aux)
    elif(len(str(oper)) != 0 and  len(mnemonico) == 0 ):
        aux = f"{str(lineas)} : {transHex(memoria,0)} ({mnemonico}{oper}) : {lineaCom}"
        arrS19.append(aux)
    elif(len(str(oper)) == 0 and  len(mnemonico) != 0 ):
        aux = f"{str(lineas)} : {transHex(memoria,0)} ({mnemonico}{oper}) : {lineaCom}"
        arrS19.append(aux)
    else:
        aux = f"{str(lineas)} : VACIO : {lineaCom}"
        arrS19.append(aux)

#funcion para buscar las etiquetas
def etiquetas():
    auxEtique = {}
    with open("EXEMPLO.asc") as archivoASC:
        for i in archivoASC:#lee el archivo y realiza un ciclo
            splitt = str(i.lower()).split()
            if len(splitt) != 0 and (1) <= len(splitt) and splitt[0][0]!="*":
                dfNem=df[df["MNEMONICO"]==str(splitt[0].lower())]
                if ((1) <= len(splitt) and len(dfNem) != 0):
                    if(i[0] != " " and iterador(inhe,splitt[0]) == 1 and (1) == len(splitt)):
                        auxEtique[splitt[0]] = [""]
                    elif(i[0] != " " and iterador(inhe,splitt[0]) == 1 and (1) < len(splitt) and splitt[1][0] == "*"):
                        auxEtique[splitt[0]] = [""]
                elif(i[0] != " " and (1) == len(splitt) and len(dfNem) == 0):
                        auxEtique[splitt[0]] = [""]
                elif(i[0] != " " and len(dfNem) == 0 and (1) < len(splitt) and splitt[1][0] == "*"):
                    auxEtique[splitt[0]] = [""]
    return auxEtique

#funcion auxiliar para iterar 
def iterador(arreglo, dato):
    a = 0
    for x in arreglo:
        if x == dato:
            a = 1
    return a

def negBin(binary):
    listBin = list(binary)
    listAux = []
    for i in listBin:
        if i == '0':
            i = '1'
        else:
            i = '0'
        listAux.append(i)
    listAux = "".join(listAux)
    return listAux

def compa2(bit1,bit2):
    nbit1 = '0b'+negBin(bit1) 
    nbit2 = '0b'+negBin(bit2) 
    resultado = ''
#posible caso para error 8?
    if(int(nbit2,2)+1)<16:
        sumaBit2 = hex(int(nbit2,2)+1)
        nbit1 = hex(int(nbit1,2))
        resultado = nbit1[2:]+sumaBit2[2:]
    else:
        sumaBit1 = hex(int(nbit1,2)+1)
        nbit2 = hex(int(nbit2,2))
        resultado = sumaBit1[2:]+nbit2[2:]
    return resultado

#funcion etiquetas asignan memoria a los diccionarios
def etiqutasDic(lista, dic):
    dicAux = {}
    for i in dic:
        for j in range(len(lista)):  
            if(j < len(lista)-1):
                if i == lista[j]:
                    dicAux[i] = lista[j+1]
    return dicAux
    
#funcion de errores
def analisisErrores(lista, linea, linCom):
    if(lista[0] != "||"):
        Nem=df[df["MNEMONICO"]==str(lista[0])]
        dfByt=dfB[dfB["MNEMONICO"]==str(splitt[0])]
        print("------------------------------------------\n"+linCom)
        if(len(Nem) == 0 and (1) <= len(lista)):
            print(f"ERROR #004 MNEMONICO INEXISTENTE en la linea {linea}")
        if((len(Nem) == 1 or len(Nem) == 0) and (1) < len(lista) and iterador(etique.keys(),lista[1]) == 0  and iterador(excep,lista[0]) == 1 ):
            print(f"ERROR #003 ETIQUETA INEXISTENTE en la linea {linea}")
        if(len(Nem) == 1 and (1) <= len(lista) and iterador(inhe,lista[0]) == 0 ):
            if((1) == len(lista)):
                print(f"ERROR #005 INSTRUCCIÓN CARECE DE OPERANDOS en la linea {linea}")
            elif((1) < len(lista) and lista[1][0] == "*"):
                print(f"ERROR #005 INSTRUCCIÓN CARECE DE OPERANDOS en la linea {linea}")
        if(len(Nem) == 1 and (1) < len(lista) and iterador(inhe,lista[0]) == 1 and lista[1][0] != "*"):
            print(f"ERROR #006 INSTRUCCIÓN NO LLEVA OPERANDOS en la linea {linea}")
        if((len(Nem) == 1 or len(Nem) == 0) and (1) < len(lista) and lista[1][0] == "#" and iterador(varYconst.keys(),lista[1][1:]) == 0 ):
            print(f"ERROR #001 CONSTANTE INEXISTENTE en la linea {linea} ")
        if((len(Nem) == 1 or len(Nem) == 0) and (1) < len(lista) and iterador(varYconst.keys(),lista[1]) == 0 and lista[1][0] != "*"):
            print(f"ERROR #002 VARIABLE INEXISTENTE en la linea {linea}")
        if(len(Nem) == 1 and (1) < len(lista) and lista[1][0] != "*"):
            imme = dfNem[['IMM']]
            immeB = dfByt[['IMM']]
            if(lista[1][0:2] == "#$" and int(len(getOpCode(imme)+lista[1][2:]))/2 != int(getOpCode(immeB))): 
                    print(f"ERROR #007 MAGNITUD DE OPERANDO ERRONEA en la linea {linea}")
            elif(lista[1][0] == "#" and  len(lista[1]) == 1 or len(lista[1]) == 2 or len(lista[1][1:]) > 4 ):
                print(f"ERROR #007 MAGNITUD DE OPERANDO ERRONEA en la linea {linea}")
            elif(splitt[1][0] == "$" and (len(lista[1]) == 1  or len(lista[1][1:]) > 4) ):
                print(f"ERROR #007 MAGNITUD DE OPERANDO ERRONEA en la linea {linea}")
        if((1) == len(lista) and linCom[0] != " " and len(Nem) == 0 ):
            print(f"ERROR #009 INSTRUCCIÓN  CARECE DE AL MENOS UN ESPACIO RELATIVO  AL MARGEN ")
        elif((1) < len(lista) and linCom[0] != " " and len(Nem) != 0 and lista[1][0] != "*" ):
            print(f"ERROR #009 INSTRUCCIÓN  CARECE DE AL MENOS UN ESPACIO RELATIVO  AL MARGEN ")
        
    if(end == 0 and lista[0]=="||"):
        print("-----------------------------------------")
        print(f"ERROR #010 NO SE ENCUENTRA END en la linea {linea}")

with open("EXEMPLO.asc") as archivoASC:
    linea = 1 #contador para lineas
    etique=etiquetas()
    for i in archivoASC:#lee el archivo y realiza un ciclo
        splitt = str(i.lower()).split()  
        #if ignora comentarios y lineas vacias
        if len(splitt) != 0 and splitt[0][0]!="*" and (1) <= len(splitt):
            #Construye dicc var
            if  len(splitt) > 1 and splitt[1]==operativas[1] and splitt[2][0]=="$" and conNum2(Hex,splitt[2][1:]):
                varYconst[splitt[0]]=splitt[2][1:]  
                formatoLST(linea,"","",i) 
            dfNem=df[df["MNEMONICO"]==str(splitt[0])]
            dfByt=dfB[dfB["MNEMONICO"]==str(splitt[0])]
            #if para INH
            if ((1) == len(splitt)  and len(dfNem) != 0 and iterador(inhe,splitt[0]) == 1 and iterador(etique.keys(),splitt[0]) == 0):
                inh = dfNem[['INH']]
                inhB = dfByt[['INH']]
                if(iterador(inhe,splitt[0]) == 1 and i[0] == " " and getOpCode(inh) != "-- "):
                    arregl01.append(getOpCode(inh))
                    formatoLST(linea,getOpCode(inh),"",i)
                    relativoArre.append(transHex(memoria,0))
                    memoria += int(getOpCode(inhB))
                elif(iterador(inhe,splitt[0]) == 0 and i[0] != " "): 
                    analisisErrores(splitt, linea, i)
                    formatoLST(linea,"","",i)
                    relativoArre.append(transHex(memoria,0))
                    memoria += 1
            #if para agregar al lst las etiquetas
            elif((1) <= len(splitt)  and iterador(etique.keys(),splitt[0]) == 1):
                formatoLST(linea,"","",i)
                relativoArre.append(splitt[0])
            elif((1) < len(splitt) and splitt[1][0]=="*" and len(dfNem) != 0 ):
                inh = dfNem[['INH']]
                inhB = dfByt[['INH']]
                if(i[0] == " " and getOpCode(inh) != "-- "):
                    arregl01.append(getOpCode(inh))
                    formatoLST(linea,getOpCode(inh),"",i)
                    relativoArre.append(transHex(memoria,0))
                    memoria += int(getOpCode(inhB))
                elif(iterador(inhe,splitt[0]) == 0 and i[0] != " "): 
                    analisisErrores(splitt, linea, i)
                    formatoLST(linea,"","",i)
                    relativoArre.append(transHex(memoria,0))
                    memoria += 1
            #if para todo lo que no es relativo ni inh
            elif((1) < len(splitt) and len(splitt[1]) > 0 and len(dfNem) != 0 ): 
                if ((1) < len(splitt) and splitt[1][0:2] == "#$" and conNum2(Hex,splitt[1][2:]) ):
                    imm = dfNem[['IMM']]
                    immB = dfByt[['IMM']]
                    if(len(splitt[1]) < 7 and len(splitt[1]) > 2 and int(len(getOpCode(imm)+transHex(splitt[1][2:],1)))/2 == int(getOpCode(immB)) ):
                        arregl01.append(getOpCode(imm))
                        arregl01.append(transHex(splitt[1][2:],1)) 
                        formatoLST(linea,getOpCode(imm),transHex(splitt[1][2:],1),i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    elif(len(splitt[1]) < 5 and len(splitt[1]) > 2 and int(len(getOpCode(imm)+"00"+transHex(splitt[1][2:],1))/2) == int(getOpCode(immB))):
                        arregl01.append(getOpCode(imm))
                        arregl01.append("00"+transHex(splitt[1][2:],1)) 
                        formatoLST(linea,getOpCode(imm),"00"+transHex(splitt[1][2:],1),i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    else:
                        print("1")
                        analisisErrores(splitt, linea, i)
                        formatoLST(linea,"","",i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                #if IMM PERO SIN $
                elif ((1) < len(splitt) and splitt[1][0] == "#" ):
                    if(conNum2(num,splitt[1][1:]) and len(splitt[1]) < 6 and len(splitt[1]) > 1):
                        imm = dfNem[['IMM']]
                        immB = dfByt[['IMM']]
                        arregl01.append(getOpCode(imm))
                        arregl01.append(transHex(splitt[1][1:],0))
                        formatoLST(linea,getOpCode(imm),transHex(splitt[1][1:],0),i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    elif(splitt[1][0:2] == "#'" and len(splitt[1]) < 4 and len(splitt[1]) > 2 ):
                        imm = dfNem[['IMM']]
                        immB = dfByt[['IMM']]
                        arregl01.append(getOpCode(imm))
                        auxSplit = i.split()
                        arregl01.append(transHex(ord(auxSplit[1][2:]),0))
                        formatoLST(linea,getOpCode(imm),transHex(ord(auxSplit[1][2:]),3),i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    elif(iterador(varYconst.keys(),splitt[1][1:]) == 1):
                        imm = dfNem[['IMM']]
                        immB = dfByt[['IMM']]
                        arregl01.append(getOpCode(imm))
                        arregl01.append(varYconst[splitt[1][1:]])
                        formatoLST(linea,getOpCode(imm),varYconst[splitt[1][1:]],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    else:
                        print("2")
                        analisisErrores(splitt, linea, i)
                        formatoLST(linea,"","",i)
                        memoria += 1
                #if EXT
                elif(((1) < len(splitt)) and (splitt[1][0] == "$") and (len(splitt[1]) == 5 or len(splitt[1]) == 4) and (conNum2(Hex,splitt[1][1:]) == True) ):
                    ext = dfNem[['EXT']]
                    extB = dfByt[['EXT']]
                    if(getOpCode(ext) != "-- " and len(getOpCode(ext)+splitt[1][1:])/2 == int(getOpCode(extB))):
                        arregl01.append(getOpCode(ext))
                        arregl01.append(splitt[1][1:])
                        formatoLST(linea,getOpCode(ext),splitt[1][1:],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(extB))
                    elif(getOpCode(ext) != "-- " and len(getOpCode(ext)+"0"+splitt[1][1:])/2 == int(getOpCode(extB))):
                        arregl01.append(getOpCode(ext))
                        arregl01.append("0"+splitt[1][1:])
                        formatoLST(linea,getOpCode(ext),"0"+splitt[1][1:],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(extB))
                    else:
                        print("3")
                        analisisErrores(splitt, linea, i)
                        formatoLST(linea,"","",i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                #if EXT
                elif((1) < len(splitt) and len(dfNem) != 0 and iterador(etique.keys(),splitt[1]) == 0 and (len(splitt[1]) == 4 or len(splitt[1]) == 3 and (conNum2(Hex,splitt[1][1:]) == True))  or iterador(varYconst.keys(),splitt[1]) == 1):
                    if(len(splitt[1]) == 4 and conNum(4,num,splitt[1])  == 4):
                        ext = dfNem[['EXT']]
                        extB = dfByt[['EXT']]
                        if(getOpCode(ext) != "-- " and len(getOpCode(ext)+splitt[1][1:])/2 == getOpCode(extB) ):
                            arregl01.append(getOpCode(ext))
                            arregl01.append(transHex(splitt[1],0))
                            formatoLST(linea,getOpCode(ext),transHex(splitt[1],0),i)
                            relativoArre.append(transHex(memoria,0))
                            memoria += int(getOpCode(extB))
                        elif(getOpCode(ext) != "-- " and len(getOpCode(ext)+"0"+splitt[1])/2 == int(getOpCode(extB))):
                            arregl01.append(getOpCode(ext))
                            arregl01.append("0"+splitt[1])
                            formatoLST(linea,getOpCode(ext),"0"+splitt[1],i)
                            relativoArre.append(transHex(memoria,0))
                            memoria += int(getOpCode(extB))
                        else:
                            analisisErrores(splitt, linea, i)
                            formatoLST(linea,"","",i)
                            relativoArre.append(transHex(memoria,0))
                            memoria += 1
                    elif(iterador(varYconst.keys(),splitt[1]) == 1):
                        ext = dfNem[['EXT']]
                        extB = dfByt[['EXT']]
                        dire = dfNem[['DIR']]
                        direB = dfByt[['DIR']]
                        if(varYconst[splitt[1]][0:2] == "00"  and getOpCode(dire) != "-- " and len(getOpCode(dire)+varYconst[splitt[1]][2:])/2 == int(getOpCode(direB))):
                            arregl01.append(getOpCode(dire))
                            arregl01.append(varYconst[splitt[1]][2:])
                            formatoLST(linea,getOpCode(dire),varYconst[splitt[1]][2:],i)
                            relativoArre.append(transHex(memoria,0))
                            memoria += int(getOpCode(direB))
                        elif(getOpCode(ext) != "-- " and len(getOpCode(ext)+varYconst[splitt[1]])/2 == int(getOpCode(extB))):
                            arregl01.append(getOpCode(ext))
                            arregl01.append(varYconst[splitt[1]])
                            formatoLST(linea,getOpCode(ext),varYconst[splitt[1]],i)
                            relativoArre.append(transHex(memoria,0))
                            memoria += int(getOpCode(extB))
                        else:
                            analisisErrores(splitt, linea, i)
                            formatoLST(linea,"","",i)
                            relativoArre.append(transHex(memoria,0))
                            memoria += 1
                    else:
                        print("4")
                        analisisErrores(splitt, linea, i)
                        formatoLST(linea,"","",i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                #if dir
                elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:]) == True) and len(splitt[1]) == 3 or len(splitt[1]) == 2 ):
                    dire = dfNem[['DIR']]
                    direB = dfNem[['DIR']]
                    if(getOpCode(ext) != "-- " and len(getOpCode(ext)+splitt[1][1:])/2 == getOpCode(extB) ):
                        arregl01.append(getOpCode(dire))
                        arregl01.append(splitt[1][1:])
                        formatoLST(linea,getOpCode(dire),splitt[1][1:],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    elif(getOpCode(ext) != "-- " and len(getOpCode(ext)+"0"+splitt[1])/2 == int(getOpCode(extB))):
                        arregl01.append(getOpCode(ext))
                        arregl01.append("0"+splitt[1])
                        formatoLST(linea,getOpCode(ext),"0"+splitt[1],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(extB))
                    else:
                        print("5")
                        analisisErrores(splitt, linea, i)
                        formatoLST(linea,"","",i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                elif((1) < len(splitt) and len(dfNem) != 0 and (conNum2(Hex,splitt[1][1:]) == True) or iterador(etique.keys(),splitt[1]) == 0 and len(splitt[1]) == 1 or len(splitt[1]) == 2):
                    dire = dfNem[['DIR']]
                    direB = dfByt[['DIR']]
                    print(len(splitt[1]))
                    if(getOpCode(dire) != "-- " and len(getOpCode(dire)+splitt[1][1:])/2 == getOpCode(direB) ):
                        arregl01.append(getOpCode(dire))
                        arregl01.append(transHex(splitt[1],3))
                        formatoLST(linea,getOpCode(dire),transHex(splitt[1],3),i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    elif(getOpCode(dire) != "-- " and len(getOpCode(dire)+"0"+splitt[1])/2 == int(getOpCode(direB))):
                        arregl01.append(getOpCode(dire))
                        arregl01.append("0"+splitt[1])
                        formatoLST(linea,getOpCode(dire),"0"+splitt[1],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    else:
                        print("6")
                        analisisErrores(splitt, linea, i)
                        formatoLST(linea,"","",i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                    #hasta aqui
                elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:3]) == True) and len(splitt[1]) == 8 ):
                    if((2) < len(splitt) and splitt[1][3:6] == ",#$" and iterador(etique.keys(),splitt[2]) == 1 and (splitt[0] == excep[2] or splitt[0] == excep[3])):
                        dire = dfNem[['DIR']]
                        direB = dfNem[['DIR']]
                        arregl01.append(getOpCode(dire))
                        arregl01.append(splitt[1][1:3] + splitt[1][6:8]+"REL")
                        formatoLST(linea,getOpCode(dire),splitt[1][1:3]+ splitt[1][6:8]+"REL",i)
                        rela = f"{splitt[0]}/{splitt[2]}/{len(arrS19)-1}/{transHex(memoria,0)}/{getOpCode(rel)}/{i}/{linea}"
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    elif((1) < len(splitt) and  splitt[1][3:6] == ",#$" and (splitt[0] == excep[4] or splitt[0] == excep[5])):
                        dire = dfNem[['DIR']]
                        direB = dfNem[['DIR']]
                        arregl01.append(getOpCode(dire))
                        arregl01.append(splitt[1][1:3] + splitt[1][6:8])
                        formatoLST(linea,getOpCode(dire),splitt[1][1:3]+ splitt[1][6:8],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    else:
                        print("7")
                        analisisErrores(splitt, linea, i)
                        formatoLST(linea,"","",i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:3]) == True) and splitt[1][3:5] == ",x" and (len(splitt[1]) == 5 or len(splitt[1]) == 10 ) ):
                    if(splitt[1][3:5] == ",x" and len(splitt[1]) == 5 ):
                        indX = dfNem[['IND,X']]
                        indXB = dfByt[['IND,X']]
                        arregl01.append(getOpCode(indX))
                        arregl01.append(splitt[1][1:3])
                        formatoLST(linea,getOpCode(indX),splitt[1][1:3],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indXB))
                    #sera relativo tambien
                    elif((2) < len(splitt) and len(splitt[1]) == 10 and splitt[1][3:8] == ",x,#$" and iterador(etique.keys(),splitt[2]) == 1 and (splitt[0] == excep[2] or splitt[0] == excep[3])):
                        indX = dfNem[['IND,X']]
                        indXB = dfByt[['IND,X']]
                        arregl01.append(getOpCode(indX))
                        arregl01.append(splitt[1][1:3] + splitt[1][8:10]+"REL")
                        formatoLST(linea,getOpCode(indX),splitt[1][1:3]+ splitt[1][8:10]+"REL",i)
                        rela = f"{splitt[0]}/{splitt[2]}/{len(arrS19)-1}/{transHex(memoria,0)}/{getOpCode(rel)}/{i}/{linea}"
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indXB))
                    elif((1) < len(splitt) and (splitt[0] == excep[4] or splitt[0] == excep[5])):
                        indX = dfNem[['IND,X']]
                        indXB = dfByt[['IND,X']]
                        arregl01.append(getOpCode(indX))
                        arregl01.append(splitt[1][1:3] + splitt[1][8:10])
                        formatoLST(linea,getOpCode(indX),splitt[1][1:3]+ splitt[1][8:10],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indXB))
                    else:
                        print("8")
                        analisisErrores(splitt, linea, i)
                        formatoLST(linea,"","",i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:3]) == True) and (len(splitt[1]) == 5 or len(splitt[1]) == 10 ) and splitt[1][3:5] == ",y"):
                    if(splitt[1][3:5] == ",y" and len(splitt[1]) == 5):
                        indY = dfNem[['IND,Y']]
                        indYB = dfByt[['IND,Y']]
                        arregl01.append(getOpCode(indY))
                        arregl01.append(splitt[1][1:3])
                        formatoLST(linea,getOpCode(indY),splitt[1][1:3],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indYB))
                    #sera relativo tambien
                    elif((2) < len(splitt) and len(splitt[1]) == 10 and splitt[1][3:8] == ",y,#$" and iterador(etique.keys(),splitt[2]) == 1 and (splitt[0] == excep[3] or splitt[0] == excep[4])):
                        indY = dfNem[['IND,Y']]
                        indYB = dfByt[['IND,Y']]
                        arregl01.append(getOpCode(indY))
                        arregl01.append(splitt[1][1:3] + splitt[1][8:10]+"REL")
                        formatoLST(linea,getOpCode(indY),splitt[1][1:3]+ splitt[1][8:10]+"REL",i)
                        rela = f"{splitt[0]}/{splitt[2]}/{len(arrS19)-1}/{transHex(memoria,0)}/{getOpCode(rel)}/{i}/{linea}"
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indYB))
                    elif((1) < len(splitt) and (splitt[0] == excep[5] or splitt[0] == excep[6])):
                        indY = dfNem[['IND,Y']]
                        indYB = dfByt[['IND,Y']]
                        arregl01.append(getOpCode(indY))
                        arregl01.append(splitt[1][1:3] + splitt[1][8:10])
                        formatoLST(linea,getOpCode(indY),splitt[1][1:3]+ splitt[1][8:10],i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indYB))
                    else:
                        print("9")
                        analisisErrores(splitt, linea, i)
                        formatoLST(linea,"","",i)
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                elif((1) < len(splitt) and len(dfNem) != 0 and iterador(etique.keys(),splitt[1]) == 1):
                    rel = dfNem[['REL']]
                    relB = dfByt[['REL']]
                    if(getOpCode(rel) == "-- " and (splitt[0] == excep[0] or splitt[0] == excep[1])):
                        ext = dfNem[['EXT']]
                        extB = dfByt[['EXT']]
                        arregl01.append(getOpCode(ext))
                        arregl01.append("")
                        formatoLST(linea,getOpCode(ext),"REL",i)
                        rela = f"{splitt[0]}/{splitt[1]}/{len(arrS19)-1}/{transHex(memoria,0)}/{getOpCode(ext)}/{i}/{linea}"
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(extB))
                    else: 
                        arregl01.append(getOpCode(rel))
                        arregl01.append("")
                        formatoLST(linea,getOpCode(rel),"REL",i)
                        rela = f"{splitt[0]}/{splitt[1]}/{len(arrS19)-1}/{transHex(memoria,0)}/{getOpCode(rel)}/{i}/{linea}"
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(relB))
                else:
                    print("10")
                    analisisErrores(splitt, linea, i)
                    formatoLST(linea,"","",i)
                    relativoArre.append(transHex(memoria,0))
                    memoria += 1
            elif(iterador(operativas,splitt[0]) == 1 ):
                #if para org
                if(splitt[0]==operativas[0]):
                    memoria = int(splitt[1][1:],base=16)
                    formatoLST(linea,"","",i)
                #if para fcb
                elif(splitt[0]==operativas[2]):
                    formatoLST(linea,splitt[1][1:3],splitt[1][5:7],i)
                #if para end
                elif(splitt[0]==operativas[3]):
                    end = 1
                    formatoLST(linea,"","",i)
            #if para reset fcb 
            elif((2) < len(splitt)  and iterador(operativas,splitt[1]) == 1 ):
                if(splitt[1]==operativas[2]):
                    formatoLST(linea,splitt[2][1:3],splitt[2][5:7],i)
            else:
                print("11")
                analisisErrores(splitt, linea, i)
                formatoLST(linea,"","",i)
                relativoArre.append(transHex(memoria,0))
                memoria += 1
        else:
            formatoLST(linea,"","",i)
        linea=linea + 1
    #funcion que agrega a los diccionarios de las etiquetas todas las direcciones de memoria
    etique = etiqutasDic(relativoArre,etique)
    #error 10 end no se encuentra
    analisisErrores(["||"], linea, "")
    #por si lo ocupas
    #funcion para relativos
    for i in relDatos:
        #split del arreglo relDatos que tienen todos los datos que son relativos asi como su informacion
        relSplit = str(i.lower()).split("/")
        if(relSplit[0] == excep[0] or relSplit[0] == excep[1]):
            #agrega al lst el jmp y jsr su direccion relativa
            arrS19[int(relSplit[2])] = f"{str(relSplit[6])} : {relSplit[3]} ({relSplit[4]}{etique[relSplit[1]]}) : {relSplit[5]}"
    
with open("archiv01.lst","a") as archivo:
    for i in arrS19:
        archivo.write(i.upper())

#exept Exception as e:
    #print(f'Exception - Ocurrió un error: {e} , {type(e)}, {}')
