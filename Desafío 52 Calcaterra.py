#Crear clase Libro
#Agregar los atributos privados título, autor y ISNB (Número Estándar Internacional de Libros)
class Libro:
    class Libro:
     def __init__(self, título="", autor="" , ISNB=""):
        self._título = título
        self._autor = autor
        self._ISNB = ISNB
#Proporcionar métodos getter y setter para cada atributo
    def get_título(self):
        return self._título
    def set_título(self, título):
        self.__título = título
    def get_autor(self):
        return self._autor
    def set_autor(self, autor):
        self.__autor= autor
    def get_ISNB(self):
        return self._ISNB
    def set_ISNB(self, ISNB):
        self.__ISNB = ISNB
#Mostrar los resultados
    def mostrar_libro(self):
        print(f"título: {self.título}")
        print(f"autor: {self.autor}")   
        print(f"ISNB: {self.ISNB}")
       