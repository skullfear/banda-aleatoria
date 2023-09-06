from banda import *

t = Banda()

t.agregar_instrumento(Musico("guitarra", "tocando guitarra", "afinando guitarra"))
t.agregar_instrumento(Musico("bateria", "tocando bateria", "afinando bateria"))
t.agregar_instrumento(Musico("piano", "tocando piano", "afinando piano"))
t.agregar_instrumento(Musico("bajo", "tocando bajo", "afinando bajo"))
t.agregar_instrumento(Musico("flauta", "tocando flauta", "afinando flauta"))

for i in range(3):
    a = t.entregar_instrumento()
    print(a.saludar(), a.mostrar_informacion())