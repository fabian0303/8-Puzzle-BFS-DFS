#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Autor: Fabian Oyarce Valenzuela
Modulo: Inteligencia Artificial 2019-2
Universidad de Talca
Version: 1.0
Python: 3.7.3

"""


from random import randint
from copy import copy, deepcopy
import time

CANT_MOV_DESORDEN=5
ESTADO_FINAL=[[1,2,3],[8,0,4],[7,6,5]]

class Nodo:
    def __init__(self, tablero,fila,columna):
        self.tablero = deepcopy(tablero)
        self.fila = fila
        self.columna = columna


def nuevoNodo(tablero, fila, columna):
    return Nodo(tablero, fila, columna)

def desordenarTablero(T):
    i=0
    while i < CANT_MOV_DESORDEN:
        azar = randint(1,4)
        if azar==1:
            T=movIzquerda(T)
        elif azar==2:
            T=movDerecha(T)
        elif azar==3:
            T=movArriba(T)
        elif azar==4:
            T=movAbajo(T)
        i+=1
    return T

def imprimeTablero(T):
    print()
    i=0
    while i<3:
        j=0
        while j<3:
            print (T[i][j],end=' ')
            j+=1
        print ()
        i+=1

def comparaTablero(T,TF):
    i=0
    while i<3:
        j=0
        while j<3:
            if T[i][j]!=TF[i][j]:
                return False
            j+=1
        i+=1
    print ()
    return True

def movIzquerda(T):
    fila = T.fila
    columna = T.columna
    tablero = T.tablero
    if columna-1>=0:
        temp = tablero[fila][columna-1]
        tablero[fila][columna-1] = 0
        tablero[fila][columna] = temp
        T.columna = columna -1
        return T
    return T

def movDerecha(T):
    fila = T.fila
    columna = T.columna
    tablero = T.tablero
    if columna+1<=2:
        temp = tablero[fila][columna+1]
        tablero[fila][columna+1] = 0
        tablero[fila][columna] = temp
        T.columna = columna + 1
        return T
    return T

def movArriba(T):
    fila = T.fila
    columna = T.columna
    tablero = T.tablero
    if fila-1>=0:
        temp = tablero[fila-1][columna]
        tablero[fila-1][columna] = 0
        tablero[fila][columna] = temp
        T.fila = fila -1
        return T
    return T

def movAbajo(T):
    fila = T.fila
    columna = T.columna
    tablero = T.tablero
    if fila+1<=2:
        temp = tablero[fila+1][columna]
        tablero[fila+1][columna] = 0
        tablero[fila][columna] = temp
        T.fila = fila + 1
        return T   
    return T

def busca0(T):
    i=0
    while i<3:
        j=0
        while j<3:
            if T[i][j]==0:
                return (i,j)
            j=j+1
        i=i+1
    return (-1,-1)

def verificaNodosExpandidos(expandidos,nodoAux):
    i=0
    while i < len(expandidos):
        if comparaTablero(expandidos[i].tablero,nodoAux):
            return True
        i+=1
    return False

def BFS(T, TF):
    colaNodos = []
    tablerosVisto = []
    nodoAux = nuevoNodo(T.tablero, T.fila,T.columna)
    colaNodos.append(nodoAux)
    tablerosVisto.append(nodoAux)
    nodosExpandidos = 0
    while True:
        nodosExpandidos+=1
        print ("Nodos expandidos: ",nodosExpandidos)
        print ("Nodos almacenados en la cola: ", len(colaNodos))
        if len(colaNodos) == 0: 
            print("El tablero no tiene solucion")
            return False
        nodo = deepcopy(colaNodos.pop(0))
        imprimeTablero(nodo.tablero)
        if comparaTablero(nodo.tablero,TF):
            print("El tablero tiene solucion")
            return True
        i=0
        while i<4:
            if i==0:
                nodoAux=deepcopy(movAbajo(nuevoNodo(nodo.tablero, nodo.fila,nodo.columna)))
            elif i==1:
                nodoAux=deepcopy(movArriba(nuevoNodo(nodo.tablero, nodo.fila,nodo.columna)))
            elif i==2:
                nodoAux=deepcopy(movIzquerda(nuevoNodo(nodo.tablero, nodo.fila,nodo.columna)))
            elif i==3:
                nodoAux=deepcopy(movDerecha(nuevoNodo(nodo.tablero, nodo.fila,nodo.columna)))

            if verificaNodosExpandidos(tablerosVisto,nodoAux.tablero) == False:
                colaNodos.append(nodoAux)
                tablerosVisto.append(nodoAux)
            i+=1

        

def DFS(T, TF):
    stackNodos = []
    tablerosVisto = []
    nodoAux = nuevoNodo(T.tablero, T.fila,T.columna)
    stackNodos.append(nodoAux)
    tablerosVisto.append(nodoAux)
    nodosExpandidos = 0
    while True:
        nodosExpandidos+=1
        print ("Nodos expandidos: ",nodosExpandidos)
        print ("Nodos almacenados en la pila: ", len(stackNodos))
        if len(stackNodos) == 0:
            print("El tablero no tiene solucion")
            return False
        nodo = deepcopy(stackNodos.pop(len(stackNodos)-1))
        imprimeTablero(nodo.tablero)
        if comparaTablero(nodo.tablero,TF):
            print("El tablero tiene solucion")
            return True
        i=0
        while i<4:
            if i==0:
                nodoAux=deepcopy(movAbajo(nuevoNodo(nodo.tablero, nodo.fila,nodo.columna)))
            elif i==1:
                nodoAux=deepcopy(movArriba(nuevoNodo(nodo.tablero, nodo.fila,nodo.columna)))
            elif i==2:
                nodoAux=deepcopy(movIzquerda(nuevoNodo(nodo.tablero, nodo.fila,nodo.columna)))
            elif i==3:
                nodoAux=deepcopy(movDerecha(nuevoNodo(nodo.tablero, nodo.fila,nodo.columna)))

            if verificaNodosExpandidos(tablerosVisto,nodoAux.tablero) == False:
                stackNodos.append(nodoAux)
                tablerosVisto.append(nodoAux)
            i+=1
        

#NO RECOMENDADO
def creaTableroAleatorioSinRepetir(): #Puede dar el caso de tableros sin solucion
    Lista=[0,1,2,3,4,5,6,7,8]
    T=[]
    i=0
    while i<3:
        fila = []
        j=0
        while j<3:
            valor=Lista[randint(0,len(Lista)-1)]
            Lista.remove(valor)
            fila=fila+[valor]
            j+=1
        T=T+[fila]
        i+=1
    return (T)


def pideOpcion():
    op=0
    while op!=1 and op!=2 and op!=3 and op!=4 and op!=5  and op!=6  and op!=9 :
        print ()
        print (" Menu de opciones")
        print ("-----------------------")
        print ("[1] Mostrar tablero de estado final")
        print ("[2] Crear tablero aleatorio (NO RECOMENDADO)")
        print ("[3] Crear tablero aleatorio en base a uno con solucion")
        print ("[4] Mostrar tableroa a utilizar")
        print ("[5] Resolver mediante busqueda en amplitud (BFS)")
        print ("[6] Resolver mediante busqueda en profundidad (DFS)")
        print ("[9] terminar la ejecucion")
        try:
            op = int(input("Ingrese opcion: "))
        except Exception as err:
            print("Erro {}".format(err))

    return (op)

print()
print("                             (0 0)")
print("                    .---oOO---(_)-----.")
print("                    ╔═════════════════╗")
print("                    ║    8 Puzzle     ║")
print("                    ╚═════════════════╝")
print("                                  oOO")
print("                           |__|__|")
print("                            | ||")
print("                          ooO Ooo")
print()
print("´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´")
print("´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´")
print("´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´")
print("´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´")
print("´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
print("´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
print("´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
print("´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´")
print("´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´")
print("´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´")
print("´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´")
print("´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´")
print("´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´¶¶´´´´´´´´¶¶¶¶´´")
print("´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶´¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´")
print("´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´")
print("´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶´¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´")
print("¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶´¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶")
print("¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶´¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶")
print("´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´´´")
print("´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´¶¶´´´´´´´´´´´¶¶´¶¶¶´´¶¶¶¶¶¶´´´´´´´´´´")
print("´´´´´´´´´´´´´´¶¶¶¶¶¶´¶´´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´¶¶´¶´¶¶´¶¶´¶´¶¶¶¶¶¶¶´¶¶´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´¶¶¶¶´¶¶´¶´¶¶´¶´¶¶´¶´¶¶´¶¶¶¶¶´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´")
print("´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´")
print("´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´")
print("´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´")
print("´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´")
print("´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´")
print("´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶´´´´´´´´")
print ()
T = nuevoNodo([],1,1)
opcion=pideOpcion()
while opcion!=9:
    if opcion == 1:
        print()
        imprimeTablero(ESTADO_FINAL)
    elif opcion == 2:
        tab = creaTableroAleatorioSinRepetir()
        i,j=busca0(tab)
        T=nuevoNodo(tab, i, j)
        print()
        print ("Tablero creado con exito!")
        imprimeTablero(T.tablero)
    elif opcion == 3:
        TABLERO_BASE=[[1,2,3],[8,0,4],[7,6,5]]
        T=nuevoNodo(TABLERO_BASE, 1, 1)
        while True:
            try:
                CANT_MOV_DESORDEN=int(input("Ingrese cantidad de movimientos de desorden: "))
                break
            except Exception as err:
                print("Erro {}".format(err))
        T=desordenarTablero(T)
        print()
        print ("Tablero creado con exito!")
        imprimeTablero(T.tablero)
        
    elif opcion == 4:
        if len(T.tablero)>0:
            print()
            print ("Tablero a utilizar")
            imprimeTablero(T.tablero)
        else:
            print()
            print("Primero debe crear un tablero")
       
    elif opcion == 5:
        if len(T.tablero)>0:
            print()
            print ("BFS")
            tiempo_inicial=time.time()
            (BFS(T,ESTADO_FINAL))
            tiempo_final=time.time()
            tiempo_total=tiempo_final-tiempo_inicial
            print("Tiempo en encontrar la solucion mediante BSF: ", tiempo_total, " segundos")
        else:
            print()
            print("Primero debe crear un tablero")
    
    elif opcion == 6:
        if len(T.tablero)>0:
            print()
            print ("DFS")
            tiempo_inicial=time.time()
            (DFS(T,ESTADO_FINAL))
            tiempo_final=time.time()
            tiempo_total=tiempo_final-tiempo_inicial
            print("Tiempo en encontrar la solucion mediante DSF: ", tiempo_total, " segundos")
        else:
            print()
            print("Primero debe crear un tablero")

    opcion=pideOpcion()
print("fin programa")

