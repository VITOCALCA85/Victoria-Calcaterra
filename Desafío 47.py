#Creo clase y autor
class Autor:
    def __init__(self, libro):
        self.libro = libro
print(libro)
#Creo lista de libros
lista = []
#Agrego libros a esa lista
def agregar(libro):
    lista.append(libro)
print(lista.append)
#Elimino libros a esa lista
def eliminar(libro):
    if libro in lista:
        lista.remove(libro)   
print(lista.remove)
#Mostrar lista de resultados


