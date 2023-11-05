# -*- coding: utf-8 -*-

import numpy as np
def Apriori_gen(Itemset, tamano):
    """Too generate new (k+1)-itemsets can see README Join Stage"""
    canditato = []
    indice_canditato = 0
    for i in range (0,tamano):
        element = str(Itemset[i])
        for j in range (i+1,tamano):
            element1 = str(Itemset[j])
            if element[0:(len(element)-1)] == element1[0:(len(element1)-1)]:
                    unionset = element[0:(len(element)-1)]+element1[len(element1)-1]+element[len(element)-1] #Combinar (k-1)-Itemset con k-Itemset
                    unionset = ''.join(sorted(unionset))  #ordenar itemset con dict order
                    canditato.append(unionset)
    return canditato

def Apriori_prune(Ck,MinSoport):
    L = []
    for i in Ck:
        if Ck[i] >= minsoport:
            L.append(i)
    return sorted(L)
def Apriori_conteo_subset(Candidato,Candidato_tamano):

    Lk = dict()
    archivo = open('/content/sample_data/datos2.txt')
    for l in archivo:
        l = str(l.split())
        conteo = 0
        for i in range (0,Candidato_tamano):
            habilitar = str(Candidato[i])
            if habilitar not in Lk:
                Lk[habilitar] = 0
            bandera = True
            for k in habilitar:
                if k not in l:
                    bandera = False
            if bandera:
                Lk[habilitar] += 1
    archivo.close()
    return Lk
minsoport = 3
C1={}
archivo = open('/content/sample_data/datos2.txt')

for linea in archivo:
    for item in linea.split():
        if item in C1:
            C1[item] +=1
        else:
            C1[item] = 1
archivo.close()
print(C1)
L = []
L1 = Apriori_prune(C1,minsoport)
L = Apriori_gen(L1,len(L1))
print ('***************************************')
print ('Frecuencia 1-itemset ',L1)
print ('***************************************')
k=2
while L != []:
    C = dict()
    C = Apriori_conteo_subset(L,len(L))
    frecuencia_itemset = []
    frecuencia_itemset = Apriori_prune(C,minsoport)
    print ('------------------------------------')
    print ('Frecuencia',k,'-itemset ',frecuencia_itemset)
    #print ('------------------------------------')
    L = Apriori_gen(frecuencia_itemset,len(frecuencia_itemset))
    k += 1