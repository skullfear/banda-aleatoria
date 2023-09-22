import tkinter as tk
from banda import Musico, Banda
from PIL import Image, ImageTk
from principal import *
from tkinter import filedialog

# Diccionario que relaciona instrumentos con rutas de imágenes
imagenes_instrumentos = {
    "guitarra": None,
    "bateria": None,
    "piano": None,
    "bajo": None,
    "flauta": None
}

# Función para mostrar la imagen del instrumento actual
def mostrar_imagen(instrumento):
    if imagenes_instrumentos[instrumento] is not None:
        imagen_path = imagenes_instrumentos[instrumento]
        imagen = Image.open(imagen_path)
        
        # Mostrar la imagen en el lienzo
        imagen_tk = ImageTk.PhotoImage(imagen)
        lienzo.create_image(0, 0, anchor=tk.NW, image=imagen_tk)
        lienzo.image = imagen_tk

# Función para cargar y asignar una imagen a un instrumento
def cargar_imagen(instrumento):
    # Abrir el cuadro de diálogo para seleccionar un archivo de imagen
    ruta_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.png;*.gif;*.bmp;*.jpeg")])
    
    if ruta_imagen:
        imagenes_instrumentos[instrumento] = ruta_imagen
        mostrar_imagen(instrumento)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Banda de Músicos")

# Crear botones "Cargar Imagen" para cada instrumento
for instrumento in imagenes_instrumentos:
    boton_cargar = tk.Button(ventana, text=f"Cargar Imagen para {instrumento}", command=lambda instr=instrumento: cargar_imagen(instr))
    boton_cargar.pack()

# Crear un lienzo para mostrar la imagen
lienzo = tk.Canvas(ventana, width=400, height=400)
lienzo.pack()

# Iniciar la aplicación tkinter
ventana.mainloop()