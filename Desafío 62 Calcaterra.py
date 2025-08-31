#En primer lugar debo crear una clase llamada Musico que tenga un método instrumento.
class Musico:
    def instrumento(self):
        return "El Director del Coro liceal es Musico y el principal instrumento que toca es el piano"
#Luego debo crear dos subclases Guitarrista y Baterista que sobrescriban el método instrumento.    
class Guitarrista(Musico):
    def instrumento(self):
        return "El Guitarrista del Coro Liceal toca como principal instrumento la guitarra eléctrica"
    def informacion(self):
        return f"Guitarrista: {self.guitarrista}"
class Baterista(Musico):
    def instrumento(self):
        return "El Baterista del Coro Liceal toca la batería y también en ocasiones el tambor"
    def informacion(self):
        return f"Baterista: {self.baterista}"
#Finalmente se solicita instanciar objetos de estas clases y demostrar el poliformismo.
guitarrista = Guitarrista("El Guitarrista del Coro Liceal toca como principal instrumento la guitarra eléctrica")
print(guitarrista.informacion())
baterista = Baterista("El Baterista del Coro Liceal toca la batería y también en ocasiones el tambor")
print(baterista.informacion())


