#Escribe una función que calcule el factorial de un número entero. Con excepciones: no es entero, es negativo o es muy grande.
def factorial(n):
    try:
        if not isinstance(n, int):
            raise TypeError("El número debe ser un entero.")
        if n < 0:
            raise ValueError("El número debe ser positivo o cero.")
        if n > 1000:
            raise OverflowError("El número es demasiado grande para calcular el factorial.")
#Factorial
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
#Excepciones
    except TypeError as e:
        print("Error de tipo:", e)
    except ValueError as e:
        print("Error de valor:", e)
    except OverflowError as e:
        print("Error de desbordamiento:", e)
