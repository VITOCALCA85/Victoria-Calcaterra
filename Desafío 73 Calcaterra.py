#Lista con números repetidos
numeros = list((1, 2, 3, 4, 5, 2, 3, 4, 5))
print(numeros)
#Eliminar los duplicados y dejar una aparición de cada uno
def eliminar_duplicados_ordenado(list):
    nueva_list = []
    for elemento in list:
        if elemento not in nueva_list:
            nueva_list.append(elemento)
    return nueva_list
print("List original:", numeros)
print("List sin duplicados (conservando orden):", eliminar_duplicados_ordenado(numeros))
