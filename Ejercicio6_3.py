# Clase: Profesor (Clase Padre)
class Profesor: # Superclase que representa un profesor genérico.
    
    def _imprimir(self):
        print("Es un profesor.")


# Clase: ProfesorTitular (Clase Hija)
class ProfesorTitular(Profesor): #Subclase de Profesor

    # Sobreescribimos el método de la clase padre
    def _imprimir(self):
        print("Es un profesor titular.")


# Clase: Prueba 
if __name__ == "__main__":
    profesor1 = ProfesorTitular()

    #El polimorfismo detecta que la variable contiene un ProfesorTitular y ejecuta su versión del método, no la del padre.
    profesor1._imprimir()