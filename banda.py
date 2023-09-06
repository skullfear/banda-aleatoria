from instrumentos import *
from random import choice

class Banda:
    def __init__(self):
        self.instrumento = []

    def agregar_instrumento(self, instrumento):
        self.instrumento.append(instrumento)

    def entregar_instrumento(self):
        return choice (self.instrumento)