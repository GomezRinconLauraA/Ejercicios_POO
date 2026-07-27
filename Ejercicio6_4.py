# Clase: Profesor (Clase Padre)
class Profesor:
    def _imprimir(self):
        print("Es un profesor.")


# Clase: ProfesorTitular (Clase Hija)
class ProfesorTitular(Profesor):
    def __init__(self):
        self._años = 0 

    def _imprimir(self):
        print("Es un profesor titular.")

    def _imprimirAños(self):
        print(f"Años = {self._años}")


# Clase: Prueba3
if __name__ == "__main__":
    profesor1 = ProfesorTitular()
    
    profesor1._imprimirAños()

    # A diferencia de Java (que no compila aquí), Python busca el método en el 
    # objeto real en tiempo de ejecución y por eso imprime 'Años = 0'.