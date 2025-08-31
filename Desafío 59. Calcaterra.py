#Parto de la clase Libro del desafío 52 anterior
class Libro:
    def __init__(self, título="", autor="" , ISNB=""):
        self._título = título
        self._autor = autor
        self._ISNB = ISNB
#Diseño una clase LibroDigital que herede de Libro y añado atributos como formato (e.g.,PDF,EPUB) y tamaño_archivo.
    class LibroDigital( Libro):
     def __init__(self, título="", autor="" , ISNB="", formato="", tamaño_archivo=""):
        super().__init__(título, autor, ISNB)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo
#Luego debo implementar una subclase EBook que sobrescriba un método de mostrar información específica, como enlaces de descarga.
    class EBook( LibroDigital):
     def __init__(self, título="", autor="" , ISNB="", formato="", tamaño_archivo="", enlaces_descarga=""):
      super().__init__(título, autor, ISNB, formato, tamaño_archivo)
      self.enlaces_descarga = enlaces_descarga
    def informacion(self):
        return f"{super().informacion()} - enlaces_descarga: {self.enlaces_descarga}"
    
    
    