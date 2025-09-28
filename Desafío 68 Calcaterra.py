#Lista de valores
valores = [5, 10, None]
#Procesar la lista
def procesar_lista(valores):
    resultados = []
    for v in valores:
        try:
            num = int(v)
            resultado = 100 / num
            resultados.append(resultado)
        except ZeroDivisionError:
            print(f"Error: no se puede dividir entre cero (valor: {v})")
            resultados.append(None)
        except ValueError:
            print(f"Error: el valor '{v}' no puede convertirse a número entero.")
            resultados.append(None)
        except TypeError:
            print(f"Error: tipo de dato no válido ({v}).")
            resultados.append(None)
        return resultados