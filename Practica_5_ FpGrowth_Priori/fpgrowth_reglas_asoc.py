# -*- coding: utf-8 -*-
"""FPgrowth_reglas_asoc.ipynb"""


#Función para cargar archivos y devolver listas de transacciones
def cargar_datos(archivo):
    with open(archivo) as f:
        contenido = f.readlines()

    contenido = [x.strip() for x in contenido]
    Transaccion = []

    for i in range(0, len(contenido)):
        Transaccion.append(contenido[i].split())

    return Transaccion

#Para convertir la transacción inicial y mantenerla frozenset
def Set_inicio(dataset):
    retDict = {}
    for trans in dataset:
        retDict[frozenset(trans)] = 1
    return retDict

#clase de nodo arbol FP
class nodos_arbol:
    def __init__(self, Nodo,conteo,nodoPadre):
        self.nodoC = Nodo
        self.count = conteo
        self.nodoLiga = None
        self.padre = nodoPadre
        self.hijo = {}

    def incremento_contador(self, contador):
        self.count += contador

#Para crear Raiz_arbol y itemsets ordenados para arbol FP
def crear_FP_Arbol(dataset, minSoport):
    Raiz_arbol = {}
    for transaccion in dataset:
        for item in transaccion:
            Raiz_arbol[item] = Raiz_arbol.get(item,0) + dataset[transaccion]
    for k in list(Raiz_arbol):
        if Raiz_arbol[k] < minSoport:
            del(Raiz_arbol[k])

    frecuent_itemset = set(Raiz_arbol.keys())

    if len(frecuent_itemset) == 0:
        return None, None

    for k in Raiz_arbol:
        Raiz_arbol[k] = [Raiz_arbol[k], None]

    retTree = nodos_arbol('Null Set',1,None)
    for itemset,contar in dataset.items():
        frecuen_transaccion = {}
        for item in itemset:
            if item in frecuent_itemset:
                frecuen_transaccion[item] = Raiz_arbol[item][0]
        if len(frecuen_transaccion) > 0:
            ordenar_itemset = [v[0] for v in sorted(frecuen_transaccion.items(), key=lambda p: p[1], reverse=True)]
            #actualizar FPTree
            actualizarArbol(ordenar_itemset, retTree, Raiz_arbol, contar)
    return retTree, Raiz_arbol

def actualizarArbol(itemset, FPTree, Raiz_arbol, count):
    if itemset[0] in FPTree.hijo:
        FPTree.hijo[itemset[0]].incremento_contador(count)
    else:
        FPTree.hijo[itemset[0]] = nodos_arbol(itemset[0], count, FPTree)

        if Raiz_arbol[itemset[0]][1] == None:
            Raiz_arbol[itemset[0]][1] = FPTree.hijo[itemset[0]]
        else:
            actualizar_nodo(Raiz_arbol[itemset[0]][1], FPTree.hijo[itemset[0]])

    if len(itemset) > 1:
        actualizarArbol(itemset[1::], FPTree.hijo[itemset[0]], Raiz_arbol, count)


def actualizar_nodo(Nodo_test, nodo_objetivo):
    while (Nodo_test.nodoLiga != None):
        Nodo_test = Nodo_test.nodoLiga

    Nodo_test.nodoLiga = nodo_objetivo


def FPTree_transversal(nodo_hoja, ruta_opcion):
 if nodo_hoja.padre != None:
    ruta_opcion.append(nodo_hoja.nodoC)
    FPTree_transversal(nodo_hoja.padre, ruta_opcion)

def encontrar_ruta(basePat, nodos_arbol):
 patron_cond_base = {}

 while nodos_arbol != None:
    ruta_opcion = []
    FPTree_transversal(nodos_arbol, ruta_opcion)
    if len(ruta_opcion) > 1:
        patron_cond_base[frozenset(ruta_opcion[1:])] = nodos_arbol.count
    nodos_arbol = nodos_arbol.nodoLiga

 return patron_cond_base


def Buscar_Tree(FPTree, indicarTabla, minSuport, prefix, frecuent_itemset):
    bigL = [v[0] for v in sorted(indicarTabla.items(),key=lambda p: p[1][0])]
    for basePat in bigL:
        new_frecuentset = prefix.copy()
        new_frecuentset.add(basePat)

        frecuent_itemset.append(new_frecuentset)

        Patron_base_condi = encontrar_ruta(basePat, indicarTabla[basePat][1])

        Condicional_FPTree, Cond_cabecera = crear_FP_Arbol(Patron_base_condi,minSuport)

        if Cond_cabecera != None:
            Buscar_Tree(Condicional_FPTree, Cond_cabecera, minSuport, new_frecuentset, frecuent_itemset)

archivo = '/content/sample_data/datos3.txt'
print("Mínimo conteo de soporte:")
soporte_minimo = 3
print(soporte_minimo)
initSet = Set_inicio(cargar_datos(archivo))
FPtree, indicarTabla = crear_FP_Arbol(initSet, soporte_minimo)

frecuent_itemset = []

Buscar_Tree(FPtree, indicarTabla, soporte_minimo, set([]), frecuent_itemset)

print("Todas las frecuencias de los itemsets:")
print(frecuent_itemset)