import tkinter as tk
from banda import Banda

class BandaApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Banda App")
        
        self.banda = Banda()
        self.banda.crear_banda()
        
        self.afinar_button = tk.Button(root, text="Afinar Banda", command=self.afinar_banda)
        self.afinar_button.pack()
        
        self.tocar_button = tk.Button(root, text="Tocar Banda", command=self.tocar_banda)
        self.tocar_button.pack()
        
        # Agregar imágenes de instrumentos
        self.imagenes_instrumentos = {
            "Guitarra": tk.PhotoImage(file="guitarra.png"),
            "Maracas": tk.PhotoImage(file="maracas.png"),
            "Charrasca": tk.PhotoImage(file="charrasca.png"),
            "Bajo": tk.PhotoImage(file="bajo.png"),
            "Violin": tk.PhotoImage(file="violin.png"),
        }

        # Crear etiquetas para mostrar las imágenes
        self.instrumento_label = tk.Label(root, image=None)
        self.instrumento_label.pack()

    def afinar_banda(self):
        self.banda.afinar_banda()
        instrumento_actual = self.banda.musicos[0].instrumento.__class__.__name__
        self.mostrar_imagen_instrumento(instrumento_actual)

    def tocar_banda(self):
        self.banda.tocar_banda()
        instrumento_actual = self.banda.musicos[0].instrumento.__class__.__name__
        self.mostrar_imagen_instrumento(instrumento_actual)
    
    def mostrar_imagen_instrumento(self, nombre_instrumento):
        if nombre_instrumento in self.imagenes_instrumentos:
            imagen = self.imagenes_instrumentos[nombre_instrumento]
            self.instrumento_label.configure(image=imagen)
            self.instrumento_label.image = imagen

if __name__ == "__main__":
    root = tk.Tk()
    app = BandaApp(root)
    root.mainloop()
