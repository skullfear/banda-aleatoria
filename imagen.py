import tkinter as tk
from tkinter import ttk

class Instrumento:
    def afinar(self):
        return "Instrumento no afinable"

    def tocar(self):
        return "Tocando instrumento"

class Guitarra(Instrumento):
    def afinar(self):
        return "Afinando guitarra"

    def tocar(self):
        return "Tocando guitarra"

class Maracas(Instrumento):
    def tocar(self):
        return "Tocando maracas"

class Charrasca(Instrumento):
    def tocar(self):
        return "Tocando charrasca"

class Bajo(Instrumento):
    def afinar(self):
        return "Afinando bajo"

    def tocar(self):
        return "Tocando bajo"

class Violin(Instrumento):
    def afinar(self):
        return "Afinando violín"

    def tocar(self):
        return "Tocando violín"

def mostrar_info_instrumento():
    instrumento = combo_instrumento.get()
    if instrumento == "Guitarra":
        resultado_label.config(text=Guitarra().afinar() + "\n" + Guitarra().tocar())
    elif instrumento == "Maracas":
        resultado_label.config(text=Maracas().tocar())
    elif instrumento == "Charrasca":
        resultado_label.config(text=Charrasca().tocar())
    elif instrumento == "Bajo":
        resultado_label.config(text=Bajo().afinar() + "\n" + Bajo().tocar())
    elif instrumento == "Violín":
        resultado_label.config(text=Violin().afinar() + "\n" + Violin().tocar())
    else:
        resultado_label.config(text="Instrumento no encontrado")

ventana = tk.Tk()
ventana.title("Aplicación de Instrumentos")

instrumentos = ["Guitarra", "Maracas", "Charrasca", "Bajo", "Violín"]
combo_instrumento = ttk.Combobox(ventana, values=instrumentos)
combo_instrumento.pack()

mostrar_button = tk.Button(ventana, text="Mostrar Info", command=mostrar_info_instrumento)
mostrar_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()

