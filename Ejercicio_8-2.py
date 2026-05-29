import tkinter as tk
from tkinter import messagebox


import math 

class Notas:
    def __init__(self): # Lista vacía para almacenar las 5 notas
        self.lista_notas = []

    def calcular_promedio(self): 
        suma = sum(self.lista_notas)
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma_cuadrados = 0
        
        for nota in self.lista_notas: # Para la desviación, a cada nota se le resta el promedio y se eleva al cuadrado
            suma_cuadrados += (nota - promedio) ** 2
            
        # Dividimos entre el número de notas y sacamos raíz cuadrada
        varianza = suma_cuadrados / len(self.lista_notas)
        return math.sqrt(varianza)

    def calcular_mayor(self):
        return max(self.lista_notas)

    def calcular_menor(self):
        return min(self.lista_notas)
    
    
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #Configurar titulo y tamaño de la ventana
        self.title("Notas_estudiante")
        self.geometry("280x380")
        self.resizable(False, False)
        
        #ESPACIOS PARA INGRESAR LAS NOTAS
        # Nota 1
        self.lbl_nota1 = tk.Label(self, text="Nota 1:")
        self.lbl_nota1.place(x=20, y=20) #Ubicacion subtitulo
        self.txt_nota1 = tk.Entry(self, width=10) #Tamaño caja
        self.txt_nota1.place(x=120, y=20) #Ubicacion caja
        
        # Nota 2
        self.lbl_nota2 = tk.Label(self, text="Nota 2:")
        self.lbl_nota2.place(x=20, y=50)
        self.txt_nota2 = tk.Entry(self, width=10)
        self.txt_nota2.place(x=120, y=50)
        
        # Nota 3
        self.lbl_nota3 = tk.Label(self, text="Nota 3:")
        self.lbl_nota3.place(x=20, y=80)
        self.txt_nota3 = tk.Entry(self, width=10)
        self.txt_nota3.place(x=120, y=80)
        
        # Nota 4
        self.lbl_nota4 = tk.Label(self, text="Nota 4:")
        self.lbl_nota4.place(x=20, y=110)
        self.txt_nota4 = tk.Entry(self, width=10)
        self.txt_nota4.place(x=120, y=110)
        
        # Nota 5
        self.lbl_nota5 = tk.Label(self, text="Nota 5:")
        self.lbl_nota5.place(x=20, y=140)
        self.txt_nota5 = tk.Entry(self, width=10)
        self.txt_nota5.place(x=120, y=140)
        
        # CREAR BOTONES
        self.btn_calcular = tk.Button(self, text="Calcular", command = self.calcular)
        self.btn_calcular.place(x=20, y=180, width=100)
        
        self.btn_limpiar = tk.Button(self, text="Limpiar", command = self.limpiar)
        self.btn_limpiar.place(x=140, y=180, width=100)
        
        # --- Etiquetas para mostrar los resultados ---
        self.lbl_promedio = tk.Label(self, text="Promedio: ")
        self.lbl_promedio.place(x=20, y=230)
        
        self.lbl_desviacion = tk.Label(self, text="Desviación estándar: ")
        self.lbl_desviacion.place(x=20, y=260)
        
        self.lbl_mayor = tk.Label(self, text="Nota mayor: ")
        self.lbl_mayor.place(x=20, y=290)
        
        self.lbl_menor = tk.Label(self, text="Nota menor: ")
        self.lbl_menor.place(x=20, y=320)

    def calcular(self): # Al presionar "Calcular"
        n1 = float(self.txt_nota1.get()) # Extrae las notas ingresadas y las convierte 
        n2 = float(self.txt_nota2.get()) # en float para operar con ellas
        n3 = float(self.txt_nota3.get())
        n4 = float(self.txt_nota4.get())
        n5 = float(self.txt_nota5.get())
        
        mis_notas = Notas()
        mis_notas.lista_notas = [n1, n2, n3, n4, n5]
            
        self.lbl_promedio.config(text=f"Promedio: {mis_notas.calcular_promedio():.2f}") #Redondeo a 2 decimales
        self.lbl_desviacion.config(text=f"Desviación estándar: {mis_notas.calcular_desviacion():.2f}")
        self.lbl_mayor.config(text=f"Nota mayor: {mis_notas.calcular_mayor():.2f}")
        self.lbl_menor.config(text=f"Nota menor: {mis_notas.calcular_menor():.2f}")
            

    def limpiar(self):     # Borrar lo calculado al presionar "Limpiar"
        self.txt_nota1.delete(0, tk.END)
        self.txt_nota2.delete(0, tk.END)
        self.txt_nota3.delete(0, tk.END)
        self.txt_nota4.delete(0, tk.END)
        self.txt_nota5.delete(0, tk.END)
        
        self.lbl_promedio.config(text="Promedio: ")
        self.lbl_desviacion.config(text="Desviación estándar: ")
        self.lbl_mayor.config(text="Nota mayor: ")
        self.lbl_menor.config(text="Nota menor: ")

# Para ejecutar la ventana
if __name__ == "__main__": 
    app = VentanaPrincipal()
    app.mainloop()