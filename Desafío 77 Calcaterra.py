#Definir el nodo del árbol binario
class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.val = valor
#Crear el nodo raíz
raiz = Nodo(1)
#Añadir nodos 
raiz.izq = Nodo(2)
raiz.der = Nodo(3)
#Añadir nodos hijos al nodo izquierdo del raíz
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)
#Añadir nodos hijos al nodo derecho del raíz
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)        
#Función que recorra el árbol en inorden y calcule la suma de todos los valores almacenados
def print_inorder(raiz):
    if raiz:
        print_inorder(raiz.izq)
        print(raiz.val, end=" ")
        print_inorder(raiz.der)
 
def suma_inorden(raiz):
    if raiz is None:
        return 0
    return suma_inorden(raiz.izquierdo) + raiz.valor + suma_inorden(raiz.derecho)     