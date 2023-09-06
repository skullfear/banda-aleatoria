class Musico:
    def __init__(self, instrumento):
        self.instrumento = instrumento
    def afinar_instrumento(self):
        return self.instrumento.afinar()
    def tocar_instrumento(self):
        return self.instrumento.tocar()