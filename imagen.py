import tkinter as tk
from PIL import Image, ImageTk
from principal import *

# Diccionario que relaciona instrumentos con rutas de imágenes
imagenes_instrumentos = {
    "guitarra": "guitarra.png",
    "bateria": "bateria.png",
    "piano": "piano.png",
    "bajo": "bajo.png",
    "flauta": "flauta.png"
}

# Función para mostrar la imagen del instrumento actual
def mostrar_imagen(instrumento):
    if instrumento in imagenes_instrumentos:
        imagen_path = imagenes_instrumentos[instrumento]
        imagen = Image.open(imagen_path)
        
        # Mostrar la imagen en el lienzo
        imagen_tk = ImageTk.PhotoImage(imagen)
        lienzo.create_image(0, 0, anchor=tk.NW, image=imagen_tk)
        lienzo.image = imagen_tk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Banda de Músicos")

# Crear botones para cargar imágenes de instrumentos
for instrumento in imagenes_instrumentos:
    boton = tk.Button(ventana, text=instrumento, command=lambda instr=instrumento: mostrar_imagen(instr))
    boton.pack()

# Crear un lienzo para mostrar la imagen
lienzo = tk.Canvas(ventana, width=400, height=400)
lienzo.pack()

# Iniciar la aplicación tkinter
ventana.mainloop()
