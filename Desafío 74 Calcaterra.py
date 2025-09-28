#Crear 2 listas de números enteros de diferentes longitudes
lista1 = [3, 5, 7, 9]
lista2 = [2, 4, 6]
print("Lista 1:", lista1)
print("Lista 2:", lista2)
#Sumar las listas
def sumar_listas(lista1, lista2):
    resultado = sumar_listas(lista1, lista2)
#Determinar la longitud máxima entre ambas listas
    max_len = max(len(lista1), len(lista2))
    for i in range(max_len):
        val1 = lista1[i] if i < len(lista1) else 0
        val2 = lista2[i] if i < len(lista2) else 0
        resultado.append(val1 + val2)
        

 
