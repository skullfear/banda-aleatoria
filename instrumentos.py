class Instrumento:
    def afinar(afinar):
        return "Instrumento no afinable"
    
    def tocar(tocar):
        return "tocando instrumento"
        
class Guitarra(Instrumento):
    def afinar(self):
        return "afinando guitarra"
    def tocar(self):
        return "tocando Guitarra"
    
class Maracas(Instrumento):
    def afinar(self):
        return "no se pueden afinar las maracas"
    def tocar(self):
        return "tocando Maracas"
    
class Charrasca(Instrumento):
    def afinar(self):
        return "no se pueden afinar las Charrascas"
    def tocar(self):
        return "tocando Charrasca"
    
class Bajo(Instrumento):
    def afinar(self):
        return "afinando Bajo"
    def tocar(self):
        return "tocando Bajo"
     
class Violin(Instrumento):
    def afinar(self):
        return "afinando violin"
    def tocar(self):
        return "tocando violin"
        
