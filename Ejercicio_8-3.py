import tkinter as tk
import math

class FiguraGeometrica: # Define base para todas las figuras
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

class Cilindro(FiguraGeometrica): #Calculos con las formulas correspondientes
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.calcular_volumen()
        self.calcular_superficie()
        
    def calcular_volumen(self):
        self.volumen = math.pi * math.pow(self.radio, 2) * self.altura
        
    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_base = math.pi * math.pow(self.radio, 2)
        self.superficie = area_lateral + (2 * area_base)

class Esfera(FiguraGeometrica): #Calculos con las formulas correspondientes
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.calcular_volumen()
        self.calcular_superficie()
        
    def calcular_volumen(self):
        self.volumen = (4/3) * math.pi * math.pow(self.radio, 3)
        
    def calcular_superficie(self):
        self.superficie = 4 * math.pi * math.pow(self.radio, 2)

class Piramide(FiguraGeometrica): #Calculos con las formulas correspondientes
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.calcular_volumen()
        self.calcular_superficie()
        
    def calcular_volumen(self):
        area_base = math.pow(self.base, 2)
        self.volumen = (area_base * self.altura) / 3
        
    def calcular_superficie(self):
        area_base = math.pow(self.base, 2)
        area_lateral = 4 * ((self.base * self.apotema) / 2)
        self.superficie = area_base + area_lateral


class VentanaPrincipal(tk.Tk): #Para elegir cual figura calcular
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("250x260")
        self.resizable(False, False)
        
        #Texto y botones centrados segun cant de caracteres
        self.lbl_titulo = tk.Label(self, text="Seleccione una figura", font=("Arial", 11, "bold"))
        self.lbl_titulo.pack(pady=15)
        
        self.btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro, width=15, height=2)
        self.btn_cilindro.pack(pady=5)
        
        self.btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera, width=15, height=2)
        self.btn_esfera.pack(pady=5)
        
        self.btn_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide, width=15, height=2)
        self.btn_piramide.pack(pady=5)

    #VENTANA CILINDRO
    def abrir_cilindro(self):
        ventana_cil = tk.Toplevel(self) #Abre la ventana sin cerrar la principal
        ventana_cil.title("Calcular Cilindro")
        ventana_cil.geometry("250x290")
        
        tk.Label(ventana_cil, text="Radio (cm):").pack(pady=5)
        txt_radio = tk.Entry(ventana_cil)
        txt_radio.pack()
        
        tk.Label(ventana_cil, text="Altura (cm):").pack(pady=5)
        txt_altura = tk.Entry(ventana_cil)
        txt_altura.pack()
        
        lbl_res_vol = tk.Label(ventana_cil, text="Volumen: ", font=("Arial", 10, "bold"))
        lbl_res_sup = tk.Label(ventana_cil, text="Superficie: ", font=("Arial", 10, "bold"))
        
        def realizar_calculo():
            cil = Cilindro(float(txt_radio.get()), float(txt_altura.get()))
            lbl_res_vol.config(text=f"Volumen: {cil.volumen:.2f} cm³")
            lbl_res_sup.config(text=f"Superficie: {cil.superficie:.2f} cm²")
            
        def limpiar_campos():
            txt_radio.delete(0, tk.END)
            txt_altura.delete(0, tk.END)
            lbl_res_vol.config(text="Volumen: ")
            lbl_res_sup.config(text="Superficie: ")
            
        btn_calc = tk.Button(ventana_cil, text="Calcular", command=realizar_calculo)
        btn_calc.pack(pady=10)
        
        lbl_res_vol.pack(pady=2)
        lbl_res_sup.pack(pady=2)

        btn_limpiar = tk.Button(ventana_cil, text="Limpiar", command=limpiar_campos)
        btn_limpiar.pack(pady=5)

    # VENTANA ESFERA
    def abrir_esfera(self):
        ventana_esf = tk.Toplevel(self)
        ventana_esf.title("Calcular Esfera")
        ventana_esf.geometry("250x240")
        
        tk.Label(ventana_esf, text="Radio (cm):").pack(pady=5)
        txt_radio = tk.Entry(ventana_esf)
        txt_radio.pack()
        
        lbl_res_vol = tk.Label(ventana_esf, text="Volumen: ", font=("Arial", 10, "bold"))
        lbl_res_sup = tk.Label(ventana_esf, text="Superficie: ", font=("Arial", 10, "bold"))
        
        def realizar_calculo():
            esf = Esfera(float(txt_radio.get()))
            lbl_res_vol.config(text=f"Volumen: {esf.volumen:.2f} cm³")
            lbl_res_sup.config(text=f"Superficie: {esf.superficie:.2f} cm²")

        def limpiar_campos():
            txt_radio.delete(0, tk.END)
            lbl_res_vol.config(text="Volumen: ")
            lbl_res_sup.config(text="Superficie: ")
            
        btn_calc = tk.Button(ventana_esf, text="Calcular", command=realizar_calculo)
        btn_calc.pack(pady=10)
        
        lbl_res_vol.pack(pady=2)
        lbl_res_sup.pack(pady=2)

        btn_limpiar = tk.Button(ventana_esf, text="Limpiar", command=limpiar_campos)
        btn_limpiar.pack(pady=5)

    # VENTANA PIRÁMIDE
    def abrir_piramide(self):
        ventana_pir = tk.Toplevel(self)
        ventana_pir.title("Calcular Pirámide")
        ventana_pir.geometry("250x330")
        
        tk.Label(ventana_pir, text="Base (cm):").pack(pady=5)
        txt_base = tk.Entry(ventana_pir)
        txt_base.pack()
        
        tk.Label(ventana_pir, text="Altura (cm):").pack(pady=5)
        txt_altura = tk.Entry(ventana_pir)
        txt_altura.pack()
        
        tk.Label(ventana_pir, text="Apotema (cm):").pack(pady=5)
        txt_apotema = tk.Entry(ventana_pir)
        txt_apotema.pack()
        
        lbl_res_vol = tk.Label(ventana_pir, text="Volumen: ", font=("Arial", 10, "bold"))
        lbl_res_sup = tk.Label(ventana_pir, text="Superficie: ", font=("Arial", 10, "bold"))
        
        def realizar_calculo(): #Calcula segun los datos ingresados
            pir = Piramide(float(txt_base.get()), float(txt_altura.get()), float(txt_apotema.get()))
            lbl_res_vol.config(text=f"Volumen: {pir.volumen:.2f} cm³")
            lbl_res_sup.config(text=f"Superficie: {pir.superficie:.2f} cm²")
        
        def limpiar_campos():
            txt_base.delete(0, tk.END)
            txt_altura.delete(0, tk.END)
            txt_apotema.delete(0, tk.END)
            lbl_res_vol.config(text="Volumen: ")
            lbl_res_sup.config(text="Superficie: ")
            
        btn_calc = tk.Button(ventana_pir, text="Calcular", command=realizar_calculo)
        btn_calc.pack(pady=10)
        
        lbl_res_vol.pack(pady=2) #Coloca los resultados donde van
        lbl_res_sup.pack(pady=2)

        btn_limpiar = tk.Button(ventana_pir, text="Limpiar", command=limpiar_campos)
        btn_limpiar.pack(pady=5)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()