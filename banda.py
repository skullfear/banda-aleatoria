from instrumentos import *
from musico import Musico
from random import randint, choice

class Banda:
    def __init__(self):
        self.instrumento = [Guitarra(), Maracas(), Charrasca(), Bajo(), Violin()]
        self.musicos = []

    def asignar_instrumento(self):
        return choice(self.instrumento)

    def crear_banda(self):
        cant = randint(5,10) 
        for i in range(cant):
            self.musicos.append(Musico(self.asignar_instrumento()))
                                       
    def afinar_banda(self):
        for m in self.musicos:
            print(m.afinar_instrumento())
        
    def tocar_banda(self):
        for m in self.musicos:
            print(m.tocar_instrumento())
