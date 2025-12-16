#scrivere un programma che generi una lista di numeri casuali compresi tra 1 e 100 che rappresentano
#misurazioni di intensità di un segnale. Il programma dopo aver generato la lista deve essere in grado  di
#modificarla in questa maniera: gli elementi di indice pari devono essere azzerati. Inoltre, dopo la codifica
#si vuole contare il numero di elementi sopra una soglia numerica.
#sottoproblemi:
#1)generare una lista di numeri compresi tra 1 e 100
#2)modificare la lista con la regola sopra
#3)contare il numero di elementi sopra soglia

import random

def lista(n):
    myList=[]
    for i in range(0,n):
        elemento = random.randint(1,100)
        myList.append(elemento)
    return myList

listax = lista(6)

def modificaLista(n,lista):
    n = len(lista)
    for i in range(0,n):
        if i % == 0:
            lista[i]=0


def soglia(n,lista,nSoglia):
    contatore = 0
    for i in range(0,n):
        if lista[i]>nSoglia
            contatore = contatore + 1
return (contatore)

nSoglia = soglia(6,listax,50)
