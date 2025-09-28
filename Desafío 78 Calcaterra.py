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
#Función que recorra el árbol en postorden y devuelva el valor máximo 
def print_postorder(raiz):
    if raiz:
        print_postorder(raiz.izq)
        print_postorder(raiz.der)
        print(raiz.val, end=" ")
def maximo_postorden(raiz):
    if raiz is None:
        return float('-inf')  # Valor mínimo para comparación
    max_izq = maximo_postorden(raiz.izquierdo)
    max_der = maximo_postorden(raiz.derecho)
    return max(raiz.valor, max_izq, max_der)    