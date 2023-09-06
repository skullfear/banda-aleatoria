class Instrumento:
    def __init__(self, tipo, tocar, afinar):
        self.tipo = tipo
        self.tocar = tocar
        self. afinar = afinar


    def mostrar_informacion(self):
        return (self.tipo, self.tocar, self.afinar) 
    
class Musico(Instrumento):
    def saludar(self):
        return "hola"
        