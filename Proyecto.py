import pandas as pd
from markdown import markdown
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
listRel = [] #lista donde se enuncia los casos relativos por resolver
tablaObj = [] #lista de listas donde cada renglon es linea,bit,hex,mn o oper
relativoArre =[] # arreglo para agregar etiquetas y memoria para asignar los diccionarios de las etiquetas
arregl01 = [] #Provisional para pruebas
arrS19 = []
relDatos = [] #arreglo para los datos que se analisaran de forma relativa
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

#Funcion para imprimir la tabla de opcode
def imprimirTabla(tablaObj):
    with open("tabla.lst","a") as archivo:
        for i in tablaObj:
                archivo.write(str(i[0])+"\t"+str(i[1])+"\t"+str(i[2])+"\t"+str(i[3]+"\n"))
    return

#Funcion para buscar un renglon de acuerdo a la memoria dada
def buscarMem(memoria):
        renglon = 1
        for i in tablaObj:
                if(i[1]==memoria):
                        return renglon
                renglon+=1
        return 0

#funcion auxiliar para iterar 
def iterador(arreglo, dato):
    a = 0
    for x in arreglo:
        if x == dato:
            a = 1
    return a

#funcion para obtener el complemento a 1 de un bit de '0000'
def negBin(binary):
    listBin = list(binary)
    listAux = []
    for i in listBin:
        if i == '0':
            i = '1'
        elif i == '1':
            i = '0'
        listAux.append(i)
    listAux = "".join(listAux)
    return listAux

#Se asegura que los bits en binario sean 4 digitos
def transBin(bit):
    if len(bit) < 4:
        ceros = 4-len(bit)
        for i in range(ceros):
            bit = '0'+ bit
        return bit
# Se asegura que los bits sean de 2 digitos
def transBit(bit):
    if len(bit) < 2:
        ceros = 2-len(bit)
        for i in range(ceros):
            bit = '0'+ bit
        return bit
    else: return bit

#Comparacion a 2 usada en bits al momento de hacer saltos de memoria
def compa2(bit1,bit2):
    bit1 = transBin(bit1)
    bit2 = transBin(bit2)
    nbit1 = negBin(bit1) 
    nbit2 = negBin(bit2) 
    resultado = ''
    if(int(nbit2,2)+1)<16:
        sumaBit2 = hex(int(nbit2,2)+1)
        nbit1 = hex(int(nbit1,2))
        resultado = nbit1[2:]+sumaBit2[2:]
    else:
        sumaBit1 = hex(int(nbit1,2)+1)
        nbit2 = hex(int(nbit2,2))
        resultado = sumaBit1[2:]+nbit2[2:]
    return resultado.upper()

#funcion etiquetas asignan memoria a los diccionarios
def etiqutasDic(lista, dic):
    dicAux = {}
    for i in dic:
        for j in range(len(lista)):  
            if(j < len(lista)-1):
                if i == lista[j]:
                    dicAux[i] = lista[j+1]
    return dicAux

#Agrega una linea a la tabla donde de almacena todo el opcode
def addLine(linea,memo,mn,oper):
        mem = memo
        #parte que se encarga de registrar los errores en un bit
        if mn == "--":
            newLine = [linea,mem,"00","00"]
            mem = mem + 1
            tablaObj.append(newLine)
            return
        #divide el mnemonico y operando en bits de 2 digitos
        listMn = divBits(mn)
        listOper = divBits(oper)
        #itera sobre los bits del mnemonicos y agrega una linea por cada bit
        for i in range(len(listMn)):
                newLine = [linea,mem,listMn[i],"mn"]
                mem = mem + 1
                tablaObj.append(newLine)
        #caso para relativos. Se deja un espacio de operando vacio para ser llenado despues
        if mn == "21" or mn == "22" or mn == "23" or mn == "24" or mn == "25" or mn == "26" or mn == "27" or mn == "28" or mn == "29" or mn == "2A" or mn == "2B" or mn == "2C" or mn == "2D" or mn == "2E" or mn == "2F" or mn == "8D":
                newLine = [linea,mem,"","o"] 
                tablaObj.append(newLine)
                listRel.append(int(mem)) 
                mem = mem + 1
        #caso para jmp y jsr donde se hace lo mismo pero se dejan dos espacios
        elif mn == "BD" or mn == "7E":
                newLine = [linea,mem,"","o"]
                tablaObj.append(newLine)
                mem = mem + 1
                newLine = [linea,mem,"","o"]
                tablaObj.append(newLine)
                mem = mem + 1
        #Se hahcen las lineas para los operandos
        else:                 
                for i in range(len(listOper)):
                        newLine = [linea,mem,listOper[i],'o']
                        mem = mem + 1
                        tablaObj.append(newLine)
                #Caso para brset y brclr
                if mn == "13" or mn == "1F" or mn == "181F" or mn == "12" or mn == "1E" or mn == "181E":
                        newLine = [linea,mem,"","o"] 
                        tablaObj.append(newLine)
                        listRel.append([int(mem)])
                        mem = mem + 1
#Divide en string en pares de digitos y lo regresa en una lista
def divBits(string):
    listBits = []     
    pos1=0
    pos2=1
    for i in range(int(len(string)/2)):
        byte = str(string[pos1]+string[pos2])
        listBits.append(byte)
        pos1 = pos1+2
        pos2 = pos2+2
        #cambiarlo a else para generar un error en caso de que mnemonico o operando no tenga numero par de caracteres
    return listBits
#Resuelve los relativos a partir de la comparacion de datos en relDatos y los diccionarios de las etiquetas
def solveRel():
    for i in relDatos:
        renglonTabla = buscarMem(i[2])
        if renglonTabla == 0:
            print("memoria no encontrada en tabla")
        #Caso para jmp y jsr donde solo se pone la memoria
        if i[3]=="BD" or i[3]=="7E" :
            listOp = divBits(etique[i[1]])
            tablaObj[renglonTabla][2] = listOp[0]
            tablaObj[renglonTabla+1][2] = listOp[1]
        #Caso para los demas relativos
        else:
            memrel = i[2]+1
            memetiq = int(etique[i[1]],16)
            resta =  memrel - memetiq
            #Se discierne si el salto es muy lejano o no
            if resta <= -127 or resta>=128:
                linea = tablaObj[buscarMem(i[2])][0]
                analisisErrores(["8"],linea,"")
            #Caso donde la resta es negativa y se hace el complemento a 2
            else:
                if resta < 0:
                    #dividiendo los caracteres del resultado
                    resta = abs(resta)
                    strResta = str(resta)
                    aux1 = ""
                    aux2 = ""
                    #division de los digitos de la resta para hacer el complemento a 2
                    if len(strResta) == 1:
                        aux1 = '0'
                        aux2 = strResta
                    elif len(strResta) == 2:
                        aux1 = strResta[0]
                        aux2 = strResta[1]
                    elif len(strResta) == 3:
                        aux1 = strResta[0:2]
                        aux2 = strResta[2]
                    aux1 = bin(int(aux1))[2:]
                    aux2 = bin(int(aux2))[2:] 
                    comp2 = compa2(aux1,aux2)
                    if len(str(comp2))%2 != 0:
                        comp2 = '0'+comp2
                    #if para asegurarse que se escriba en el espacio correcto en el caso de las excepciones
                    if i[3]=="12" or i[3]=="13" or i[3]=="1E" or i[3]=="1F" or i[3]=="181E" or i[3]=="181F" : 
                        tablaObj[renglonTabla+2][2] = compa2(aux1,aux2)
                    else:
                        tablaObj[renglonTabla][2] = compa2(aux1,aux2)
                #Caso de resta positiva
                else:
                    hexResta = hex(resta)
                    if len(hexResta)%2 != 0:
                        hexResta = hexResta[0:2]+'0'+hexResta[2:]
                    if i[3]=="12" or i[3]=="13" or i[3]=="1E" or i[3]=="1F" or i[3]=="181E" or i[3]=="181F": 
                        tablaObj[renglonTabla+2][2] = hexResta[2:]
                    else:
                        tablaObj[renglonTabla][2] = hexResta[2:]

#ImprimirLST
def genLST():
    print('generando LST')
    ascArr = []
    #Se genera un arreglo con todo el archivo inicial para no lidear con errores
    with open("EXEMPLO.asc") as ASC:
        for i in ASC:
            ascArr.append(i)
    with open("LST.html", "a") as file:
        linea = 1
        renglonTabla = 0
        #Se itera sobre el arreglo anterior
        for i in ascArr:
            if linea == len(ascArr)-1:
                break
            mem = ''
            mn = ''
            op = ''
            #Se generan dos diferentes strins, una de mnemonicos y otra de operandos
            #El numero maximo de bits por renglon es 5, por eso el for llega hasta 5
            #Solo se registran los mnemonicos y operandos si la linea en la TablaObj coincide con la linea de la iteracion actual
            for j in range(5):
                if tablaObj[renglonTabla][0] == linea:
                    if tablaObj[renglonTabla][3] == 'mn':
                        mn = mn+tablaObj[renglonTabla][2].upper()
                        if j == 0:
                            mem = hex(tablaObj[renglonTabla][1])[2:]
                        if renglonTabla == len(tablaObj)-1:
                            break
                        renglonTabla += 1
                    elif tablaObj[renglonTabla][3] == 'o':
                        op = op+tablaObj[renglonTabla][2].upper()
                        if renglonTabla == len(tablaObj)-1:
                            break
                        renglonTabla += 1
            #Caso cuando el renglon si contiene opcode
            if mn != "":
                html = markdown(f"<font color='black'>{linea} : {mem.upper()} </font><font color = 'blue'>{mn}</font><font color = 'red'>{op.upper()}</font><font color = 'black'> :         {i}</font>")
                file.write(html)
            #Caso sin opcode
            else:
                html = markdown(f"<font color='black'>{linea} : VACIO :       {i}</font>")
                file.write(html)
            linea = linea + 1

#funcion de checksum para seguir el formato de los dos ultimos digitos de acuerdo a las instrucciones de motorola
def checksum(suma,memoria,contador):
    mem1 = memoria[:2]
    mem2 = memoria[2:]
    suma += (int(mem1,16)+(int(mem2,16)))
    suma += (contador+3)
    suma = hex(suma)[2:]
    suma = suma[-2:]
    sum1 = negBin(bin(int(suma[0],16))[2:])
    sum2 = negBin(bin(int(suma[1],16))[2:])
    suma = hex(int(sum1,2))[2:]+hex(int(sum2,2))[2:]
    return suma
    
#Imprimir S19   
def genS19():
    with open("S19.html","a") as S19:
        mem = tablaObj[0][1]
        renglon = 0
        renglonMax = len(tablaObj)
        contadorbits = 0 #contador de bits para el checksum
        lineaS19='' #linea que se va a escribir en el doc
        suma = 0 #suma para el checksum
        chsum = '' #linea que va a tener los digitos del checksum
        #Se itera sobre la tabla
        while(renglon < renglonMax-1):
            if(renglon == 0 or tablaObj[renglon][1]==tablaObj[renglon-1][1]+1): #Si las memorias son consecutivas
                #Se van a tener 32 bits de operaciones por cada renglon
                if(contadorbits == 32):
                    chsum = checksum(suma,hex(mem)[2:],contadorbits)
                    lineaS19 = f"<font color='black'>S123{hex(mem)[2:].upper()}</font>{lineaS19}<font color='black'>{chsum}</font>"
                    S19.write(markdown(lineaS19))
                    lineaS19=''
                    suma = 0
                    contadorbits = 0
                    mem = tablaObj[renglon][1]
                #Si las memorias son consecutivas y se encuentra un mnemonico
                if(tablaObj[renglon][3]=='mn'):
                    lineaS19 = lineaS19 + f"<font color='red'>{tablaObj[renglon][2].upper()}</font>"
                    suma += int(tablaObj[renglon][2],16)
                    if(renglon != renglonMax-1):
                        renglon += 1
                    contadorbits += 1
                    continue
                #Si las memorias son consecutivas y se encuentra un operando
                if(tablaObj[renglon][3]=='o'):
                    lineaS19 = lineaS19 + f"<font color='blue'>{tablaObj[renglon][2].upper()}</font>"
                    suma += int(tablaObj[renglon][2],16)
                    if(renglon != renglonMax-1):
                        renglon += 1
                    contadorbits += 1
                    continue
            #Si las memorias no son consecutivas
            else:
                #Si se tiene un conjunto de operaciones remanentes de diferente memoria
                if(contadorbits != 0):
                    chsum = checksum(suma,hex(mem)[2:],contadorbits)                   
                    lineaS19 = f"<font color='black'>S1{transBit(hex(contadorbits+3)[2:].upper())}{hex(mem)[2:].upper()}</font>{lineaS19}<font color='black'>{chsum}</font>"
                    S19.write(markdown(lineaS19))
                    lineaS19=''
                    suma = 0
                    contadorbits = 0
                    mem = tablaObj[renglon][1]
                #Si no es consecutivo y se encuentra un mn
                if(tablaObj[renglon][3]=='mn'):
                    lineaS19 = lineaS19 + f"<font color='red'>{tablaObj[renglon][2].upper()}</font>"
                    suma += int(tablaObj[renglon][2],16)
                    if(renglon != renglonMax-1):
                        renglon += 1
                    contadorbits += 1
                    continue
                #Si no es consecutivo y se encuentra un op
                if(tablaObj[renglon][3]=='o'):
                    lineaS19 = lineaS19 + f"<font color='blue'>{tablaObj[renglon][2].upper()}</font>"
                    suma += int(tablaObj[renglon][2],16)
                    if(renglon != renglonMax-1):
                        renglon += 1
                    contadorbits += 1
                    continue
        #Se deshace de los remanentes
        if(contadorbits != 0 and renglon == renglonMax):
                    chsum = checksum(suma,hex(mem)[2:],contadorbits)
                    lineaS19 = f"<font color='black'>S1{transBit(hex(contadorbits+3)[2:].upper())}{hex(mem)[2:].upper()}</font>{lineaS19}<font color='black'>{chsum}</font>"
                    S19.write(markdown(lineaS19))
                    lineaS19=''
                    suma = 0
                    contadorbits = 0
        #Ultima linea del formato segun las instrucciones
        S19.write(markdown(f"<font color='black'>S9030000FC</font>"))
        
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

#Codigo principal donde se discierne entre los modos de direccionamiento
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
                    addLine(linea,memoria,getOpCode(inh),"")
                    relativoArre.append(transHex(memoria,0))
                    memoria += int(getOpCode(inhB))
                elif(iterador(inhe,splitt[0]) == 0 and i[0] != " "): 
                    analisisErrores(splitt, linea, i)
                    addLine(linea,memoria,"--","--")
                    relativoArre.append(transHex(memoria,0))
                    memoria += 1
            #if para agregar al lst las etiquetas
            elif((1) <= len(splitt)  and iterador(etique.keys(),splitt[0]) == 1):
                relativoArre.append(splitt[0])
            #IF INH
            elif((1) < len(splitt) and splitt[1][0]=="*" and len(dfNem) != 0 ):
                inh = dfNem[['INH']]
                inhB = dfByt[['INH']]
                if(i[0] == " " and getOpCode(inh) != "-- "):
                    addLine(linea,memoria,getOpCode(inh),"")
                    relativoArre.append(transHex(memoria,0))
                    memoria += int(getOpCode(inhB))
                elif(iterador(inhe,splitt[0]) == 0 and i[0] != " "): 
                    analisisErrores(splitt, linea, i)
                    addLine(linea,memoria,"00","")
                    relativoArre.append(transHex(memoria,0))
                    memoria += 1
            #if para todo lo que no es relativo ni inh
            elif((1) < len(splitt) and len(splitt[1]) > 0 and len(dfNem) != 0 ): 
                #IF IMM
                if ((1) < len(splitt) and splitt[1][0:2] == "#$" and conNum2(Hex,splitt[1][2:]) ):
                    imm = dfNem[['IMM']]
                    immB = dfByt[['IMM']]
                    if(len(splitt[1]) < 7 and len(splitt[1]) > 2 and int(len(getOpCode(imm)+transHex(splitt[1][2:],1)))/2 == int(getOpCode(immB)) ):
                        addLine(linea,memoria,getOpCode(imm),transHex(splitt[1][2:],1))
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    elif(len(splitt[1]) < 5 and len(splitt[1]) > 2 and int(len(getOpCode(imm)+"00"+transHex(splitt[1][2:],1))/2) == int(getOpCode(immB))):
                        addLine(linea,memoria,getOpCode(imm),"00"+transHex(splitt[1][2:],1))
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    else:
                        print("1")
                        analisisErrores(splitt, linea, i)
                        addLine(linea,memoria,"00","")
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                #if IMM PERO SIN $
                elif ((1) < len(splitt) and splitt[1][0] == "#" ):
                    if(conNum2(num,splitt[1][1:]) and len(splitt[1]) < 6 and len(splitt[1]) > 1):
                        imm = dfNem[['IMM']]
                        immB = dfByt[['IMM']]
                        addLine(linea,memoria,getOpCode(imm),transHex(splitt[1][1:],0))
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    #IF IMM #'
                    elif(splitt[1][0:2] == "#'" and len(splitt[1]) < 4 and len(splitt[1]) > 2 ):
                        imm = dfNem[['IMM']]
                        immB = dfByt[['IMM']]
                        arregl01.append(getOpCode(imm))
                        auxSplit = i.split()
                        addLine(linea,memoria,getOpCode(imm),transHex(ord(auxSplit[1][2:]),3))
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    #IF IMM VAR Y CONST
                    elif(iterador(varYconst.keys(),splitt[1][1:]) == 1):
                        imm = dfNem[['IMM']]
                        immB = dfByt[['IMM']]
                        addLine(linea,memoria,getOpCode(imm),varYconst[splitt[1][1:]])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(immB))
                    else:
                        print("2")
                        analisisErrores(splitt, linea, i)
                        addLine(linea,memoria,"00","")
                        memoria += 1
                #if EXT $
                elif(((1) < len(splitt)) and (splitt[1][0] == "$") and (len(splitt[1]) == 5 or len(splitt[1]) == 4) and (conNum2(Hex,splitt[1][1:]) == True) ):
                    ext = dfNem[['EXT']]
                    extB = dfByt[['EXT']]
                    if(getOpCode(ext) != "-- " and len(getOpCode(ext)+splitt[1][1:])/2 == int(getOpCode(extB))):
                        addLine(linea,memoria,getOpCode(ext),splitt[1][1:])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(extB))
                    elif(getOpCode(ext) != "-- " and len(getOpCode(ext)+"0"+splitt[1][1:])/2 == int(getOpCode(extB))):
                        addLine(linea,memoria,getOpCode(ext),"0"+splitt[1][1:])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(extB))
                    else:
                        print("3")
                        analisisErrores(splitt, linea, i)
                        addLine(linea,memoria,"00","")
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                #if EXT variables
                elif((1) < len(splitt) and len(dfNem) != 0 and iterador(etique.keys(),splitt[1]) == 0 and (len(splitt[1]) == 4 or len(splitt[1]) == 3 and (conNum2(Hex,splitt[1][1:]) == True))  or iterador(varYconst.keys(),splitt[1]) == 1):
                    if(len(splitt[1]) == 4 and conNum(4,num,splitt[1])  == 4):
                        ext = dfNem[['EXT']]
                        extB = dfByt[['EXT']]
                        if(getOpCode(ext) != "-- " and len(getOpCode(ext)+splitt[1][1:])/2 == getOpCode(extB) ):
                            addLine(linea,memoria,getOpCode(ext),transHex(splitt[1],0))
                            relativoArre.append(transHex(memoria,0))
                            memoria += int(getOpCode(extB))
                        elif(getOpCode(ext) != "-- " and len(getOpCode(ext)+"0"+splitt[1])/2 == int(getOpCode(extB))):
                            addLine(linea,memoria,getOpCode(ext),"0"+splitt[1])
                            relativoArre.append(transHex(memoria,0))
                            memoria += int(getOpCode(extB))
                        else:
                            analisisErrores(splitt, linea, i)
                            addLine(linea,memoria,"00","")
                            relativoArre.append(transHex(memoria,0))
                            memoria += 1
                    #IF PARA DETERMINAR SI ES EXT O DIR
                    elif(iterador(varYconst.keys(),splitt[1]) == 1):
                        ext = dfNem[['EXT']]
                        extB = dfByt[['EXT']]
                        dire = dfNem[['DIR']]
                        direB = dfByt[['DIR']]
                        #CASO DIRECTO
                        if(varYconst[splitt[1]][0:2] == "00"  and getOpCode(dire) != "-- " and len(getOpCode(dire)+varYconst[splitt[1]][2:])/2 == int(getOpCode(direB))):
                            addLine(linea,memoria,getOpCode(dire),varYconst[splitt[1]][2:])
                            relativoArre.append(transHex(memoria,0))
                            memoria += int(getOpCode(direB))
                        #CASO EXT
                        elif(getOpCode(ext) != "-- " and len(getOpCode(ext)+varYconst[splitt[1]])/2 == int(getOpCode(extB))):
                            addLine(linea,memoria,getOpCode(ext),varYconst[splitt[1]])
                            relativoArre.append(transHex(memoria,0))
                            memoria += int(getOpCode(extB))
                        else:
                            analisisErrores(splitt, linea, i)
                            addLine(linea,memoria,"00","")
                            relativoArre.append(transHex(memoria,0))
                            memoria += 1
                    else:
                        print("4")
                        analisisErrores(splitt, linea, i)
                        addLine(linea,memoria,"00","")
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                #if dir
                elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:]) == True) and len(splitt[1]) == 3 or len(splitt[1]) == 2 ):
                    dire = dfNem[['DIR']]
                    direB = dfNem[['DIR']]
                    if(getOpCode(ext) != "-- " and len(getOpCode(ext)+splitt[1][1:])/2 == getOpCode(extB) ):
                        addLine(linea,memoria,getOpCode(dire),splitt[1][1:])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    elif(getOpCode(ext) != "-- " and len(getOpCode(ext)+"0"+splitt[1])/2 == int(getOpCode(extB))):
                        addLine(linea,memoria,getOpCode(ext),"0"+splitt[1])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(extB))
                    else:
                        print("5")
                        analisisErrores(splitt, linea, i)
                        addLine(linea,memoria,"00","")
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                elif((1) < len(splitt) and len(dfNem) != 0 and (conNum2(Hex,splitt[1][1:]) == True) or iterador(etique.keys(),splitt[1]) == 0 and len(splitt[1]) == 1 or len(splitt[1]) == 2):
                    dire = dfNem[['DIR']]
                    direB = dfByt[['DIR']]
                    print(len(splitt[1]))
                    if(getOpCode(dire) != "-- " and len(getOpCode(dire)+splitt[1][1:])/2 == getOpCode(direB) ):
                        addLine(linea,memoria,getOpCode(dire),transHex(splitt[1],3))
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    elif(getOpCode(dire) != "-- " and len(getOpCode(dire)+"0"+splitt[1])/2 == int(getOpCode(direB))):
                        addLine(linea,memoria,getOpCode(dire),"0"+splitt[1])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    else:
                        print("6")
                        analisisErrores(splitt, linea, i)
                        addLine(linea,memoria,"00","")
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                    #hasta aqui
                    #MAS IF DIR
                elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:3]) == True) and len(splitt[1]) == 8 ):
                    if((2) < len(splitt) and splitt[1][3:6] == ",#$" and iterador(etique.keys(),splitt[2]) == 1 and (splitt[0] == excep[2] or splitt[0] == excep[3])):
                        dire = dfNem[['DIR']]
                        direB = dfNem[['DIR']]
                        addLine(linea,memoria,getOpCode(dire),splitt[1][1:3]+splitt[1][6:8])
                        rela = [splitt[0],splitt[2],memoria,getOpCode(dire)]
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    elif((1) < len(splitt) and  splitt[1][3:6] == ",#$" and (splitt[0] == excep[4] or splitt[0] == excep[5])):
                        dire = dfNem[['DIR']]
                        direB = dfNem[['DIR']]
                        addLine(linea,memoria,getOpCode(dire),splitt[1][1:3]+splitt[1][6:8])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(direB))
                    else:
                        print("7")
                        analisisErrores(splitt, linea, i)
                        addLine(linea,memoria,"00","")
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                #IF IND X
                elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:3]) == True) and splitt[1][3:5] == ",x" and (len(splitt[1]) == 5 or len(splitt[1]) == 10 ) ):
                    if(splitt[1][3:5] == ",x" and len(splitt[1]) == 5 ):
                        indX = dfNem[['IND,X']]
                        indXB = dfByt[['IND,X']]
                        addLine(linea,memoria,getOpCode(indX),splitt[1][1:3])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indXB))
                    #CASO PARA EXCEPCIONES
                    elif((2) < len(splitt) and len(splitt[1]) == 10 and splitt[1][3:8] == ",x,#$" and iterador(etique.keys(),splitt[2]) == 1 and (splitt[0] == excep[2] or splitt[0] == excep[3])):
                        indX = dfNem[['IND,X']]
                        indXB = dfByt[['IND,X']]
                        addLine(linea,memoria,getOpCode(indX),splitt[1][1:3]+splitt[1][8:10])
                        rela = [splitt[0],splitt[2],memoria,getOpCode(indX)]
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indXB))
                    elif((1) < len(splitt) and (splitt[0] == excep[4] or splitt[0] == excep[5])):
                        indX = dfNem[['IND,X']]
                        indXB = dfByt[['IND,X']]
                        addLine(linea,memoria,getOpCode(indX),splitt[1][1:3]+splitt[1][8:10])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indXB))
                    else:
                        print("8")
                        analisisErrores(splitt, linea, i)
                        addLine(linea,memoria,"00","")
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                #IF IND Y
                elif((1) < len(splitt) and splitt[1][0] == "$" and (conNum2(Hex,splitt[1][1:3]) == True) and (len(splitt[1]) == 5 or len(splitt[1]) == 10 ) and splitt[1][3:5] == ",y"):
                    if(splitt[1][3:5] == ",y" and len(splitt[1]) == 5):
                        indY = dfNem[['IND,Y']]
                        indYB = dfByt[['IND,Y']]
                        addLine(linea,memoria,getOpCode(indY),splitt[1][1:3])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indYB))
                    #CASO EXCEPCIONES
                    elif((2) < len(splitt) and len(splitt[1]) == 10 and splitt[1][3:8] == ",y,#$" and iterador(etique.keys(),splitt[2]) == 1 and (splitt[0] == excep[3] or splitt[0] == excep[4])):
                        indY = dfNem[['IND,Y']]
                        indYB = dfByt[['IND,Y']]
                        addLine(linea,memoria,getOpCode(indY),splitt[1][1:3]+ splitt[1][8:10])
                        rela = [splitt[0],splitt[2],memoria,getOpCode(indY)]
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indYB))
                    elif((1) < len(splitt) and (splitt[0] == excep[5] or splitt[0] == excep[6])):
                        indY = dfNem[['IND,Y']]
                        indYB = dfByt[['IND,Y']]
                        addLine(linea,memoria,getOpCode(indY),splitt[1][1:3]+ splitt[1][8:10])
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(indYB))
                    else:
                        print("9")
                        analisisErrores(splitt, linea, i)
                        addLine(linea,memoria,"00","")
                        relativoArre.append(transHex(memoria,0))
                        memoria += 1
                #CASO RELATIVO
                elif((1) < len(splitt) and len(dfNem) != 0 and iterador(etique.keys(),splitt[1]) == 1):
                    rel = dfNem[['REL']]
                    relB = dfByt[['REL']]
                    #CASO PARA JMP JSR
                    if(getOpCode(rel) == "-- " and (splitt[0] == excep[0] or splitt[0] == excep[1])):
                        ext = dfNem[['EXT']]
                        extB = dfByt[['EXT']]
                        addLine(linea,memoria,getOpCode(ext),"")
                        rela = [splitt[0],splitt[1],memoria,getOpCode(ext)]
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(extB))
                    else: 
                        addLine(linea,memoria,getOpCode(rel),"")
                        rela = [splitt[0],splitt[1],memoria,getOpCode(rel)]
                        relDatos.append(rela)
                        relativoArre.append(transHex(memoria,0))
                        memoria += int(getOpCode(relB))
                else:
                    print("10")
                    analisisErrores(splitt, linea, i)
                    addLine(linea,memoria,"00","")
                    relativoArre.append(transHex(memoria,0))
                    memoria += 1
            #IF PARA OPERATIVAS
            elif(iterador(operativas,splitt[0]) == 1 ):
                #if para org
                if(splitt[0]==operativas[0]):
                    memoria = int(splitt[1][1:],base=16)
                #if para fcb
                elif(splitt[0]==operativas[2]):
                    addLine(linea,memoria,splitt[1][1:3],splitt[1][5:7])
                #if para end
                elif(splitt[0]==operativas[3]):
                    end = 1
            #if para reset fcb 
            elif((2) < len(splitt)  and iterador(operativas,splitt[1]) == 1 ):
                if(splitt[1]==operativas[2]):
                    addLine(linea,memoria,splitt[2][1:3],splitt[2][5:7])
            else:
                print("11")
                analisisErrores(splitt, linea, i)
                addLine(linea,memoria,"00","")
                relativoArre.append(transHex(memoria,0))
                memoria += 1
        linea=linea + 1
    #funcion que agrega a los diccionarios de las etiquetas todas las direcciones de memoria
    etique = etiqutasDic(relativoArre,etique)
    #error 10 end no se encuentra
    analisisErrores(["||"], linea, "")
    #Resolucion de relativos
    solveRel()
    #Generar S19
    genS19()
    print("S19 creado")
    #Generar LST
    genLST()
    print('LST creado')

#imprimirTabla(relDatos)
#imprimirTabla(tablaObj)

