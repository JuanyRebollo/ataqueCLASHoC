import pyautogui
import time
import csv
import os
def click_escalado(x, y):
    anchoOG=1366
    altoOG=768
    anchoNW,altoNW=pyautogui.size()
    x = int(x * anchoNW / anchoOG)
    y = int(y * altoNW / altoOG)
    pyautogui.click(x, y)
def terminar():
    
        print("ENTRO A TERMINAR")
        terminar1=170
        terminar2=578
        time.sleep(1)
        click_escalado(terminar1,terminar2)
        FINALIZAR1=839
        FINALIZAR2=460
        time.sleep(1)
        click_escalado(FINALIZAR1,FINALIZAR2)
        volver1=710
        volver2=615
        time.sleep(3)
        click_escalado(volver1,volver2)

     
def tropa1(x,y,xlista,j,coord1):
    cant=xlista[j]
    click_escalado(x,y)
    i=cant
    if isinstance(i,str):
        click_escalado(265,385)
    else: 
        if cant > len(coord1):
            cant=len(coord1)    
        for n,m in coord1[:cant]:
            click_escalado(n,m)
            i-=1
        if i>0:
            xlista[j]=i
            tropa1(x,y,xlista)
# def moverPantalla():
    # xInicio=703
    # yInicio=195
    # xFin=692
    # yFin=341
    # pyautogui.moveTo(xInicio, yInicio, duration=1)
    # pyautogui.mouseDown(button="left")
    # pyautogui.moveTo(xFin, yFin, duration=1)
    # pyautogui.mouseUp(button="left")
    # return 3
def lanzarMurcielago(lista,x,y):#!ARREGLAR
    click_escalado(x,y)
    ejeX=265
    ejeY=385
    for j in range(11):
        click_escalado(265,385)
def recuperar():
    listas=[]
    ruta='ejercito.csv'
    cont=0
    if os.path.exists(ruta) or os.path.exists('ejercito.csv'):
        print("EXISTEN EJERCITOS,\n¿ARMAR NUEVO EJERCITO O ATACAR CON YA EXISTENTE?")
        opcion=int( input("[1] atacar con ejercito armado\n[2] atacar con nuevo ejercito\n>>> "))
        if opcion==1:
            with open('ejercito.csv',newline='') as f:
                reader=csv.reader(f,delimiter=';')
                for fila in reader:
                    ejercito=[]
                    for x in fila:
                        if x.isdigit():
                            ejercito.append(int(x))
                        else:
                            ejercito.append(x)
                    listas.append(ejercito)
                    print(f"ejercito {cont+1}",ejercito)
                    cont+=1
                opcion=int( input(f"ELIJA EJERCITO entre [1] a [{cont}]\n>>> "))
                if opcion>0 and opcion < len(listas):    
                    return listas[opcion-1]
                else:
                    print("ERROR... volviendo al principio...")
                    return recuperar()
        elif opcion==2:
            
            listas=[]
            return listas
    else:
        listas=[]
        return listas
        
def guardar(ejercito):
    with open('ejercito.csv','a',newline='') as f:
        writer=csv.writer(f,delimiter=';')
        writer.writerow(ejercito)
def buscar():
    botonA1=176
    botonA2=659
    time.sleep(1)
    click_escalado(botonA1,botonA2)
    botonB1=281
    botonB2=500
    time.sleep(1)
    click_escalado(botonB1,botonB2)
def armarEjercito(xtropas,xhero,xcuart,xhech,lista):
    
    for i in range(xtropas):
        cant=int(input(f"Cantidad de la {i+1}° tropa >>>"))
        cant+=5
        lista.append(cant)
    if xcuart==1:
        lista.append("CUARTEL")
    if xhero>0:
        
        for i in range(xhero):
            heroe="heroe"
            lista.append(heroe)
    if xhech>0:
        for i in range(xhech):
             cant=int(input(f"Cantidad del {i+1}° hechizo >>>"))
             lista.append(cant)
    
def comprobar(lista):
    habil=[]
    cont=[]
    coord1 = [(326, 276),(416, 206),(535, 132),(571, 72),(631, 49),(409, 500),(492, 505),(485, 541),(560, 597),(587, 604),(861, 601),(936, 550),(1082, 443),(1100, 300),(1026, 241),(935, 175),(848, 103),(848, 103),(952, 528),(952, 528),(868, 471),(871, 890),(871, 890),(871, 889)]
    if len(lista)<=11:
        cuadros=[(313,662),(391,666),(478,660),(570,661),(645,661),(725,664),(784,664),(882,668),(962,661),(1042,671),(1119,668)]
        for i in range(len(lista)):
            X,Y=cuadros[i]
            tropa1(X,Y,lista,i,coord1)
            if lista[i]=='heroe':
                habil.append((X,Y))
                cont.append(i)
        time.sleep(5)
        for j in range(len(habil)):
            
            n,m=habil[j]
            pos=cont[j]
            tropa1(n,m,lista,pos,coord1)
        for l in range(len(cont)):
            pos=cont[l]
            x,y=cuadros[pos+1]
        lanzarMurcielago(lista,x,y)
            
if __name__=='__main__':
    ej=recuperar()
    if len(ej)<=0:
        heroes=int(input("""Ingrese cantidad de heroes disponibles para el ataque 
                        [0] Si no hay heroes
                        [4] Como maximo
                        >>> """))
        tropas=int(input("""Ingrese cantidad de tropas distintas
                        >>> """))
        cuartel=int(input("""Cuarteles disponibles?
                        [0] Si no hay cuarteles
                        [1] Si hay disponibles
                        >>>"""))
        hechizos=int(input("""Ingrese cantidad de hechizos distintos
                        >>> """))
        armarEjercito(tropas,heroes,cuartel,hechizos,ej)
        guardar(ej)
        
    for i in range(len(ej)):
        print(f"Cuadro {i+1}",ej[i])
    
    time.sleep(4)
    buscar()
    time.sleep(4)
    coord1 = [(326, 276),(416, 206),(535, 132),(571, 72),(631, 49),(409, 500),(492, 505),(485, 541),(560, 597),(587, 604),(861, 601),(936, 550),(1082, 443),(1100, 300),(1026, 241),(935, 175),(848, 103),(848, 103),(952, 528),(952, 528),(868, 471),(871, 890),(871, 890),(871, 889)]
    coord2=[(639,121),(783,121),(708,100)]
    # try:
    band=True
    while band==True:
        print("ENTRO BUCLE")
        time.sleep(1)
        pyautogui.scroll(-1000)  # cantidad negativa
        pyautogui.scroll(-3000)  
        pyautogui.scroll(-1000) 
        pyautogui.scroll(-1000)  # cantidad negativa
        pyautogui.scroll(-1000)  # cantidad negativa
        pyautogui.scroll(-1000)  # cantidad negativa
        comprobar(ej)
        time.sleep(30)
        terminar()
        time.sleep(6)
        buscar()
        time.sleep(5)
        
        
    