from abc import ABC, abstractmethod

# 1. Clase Abstracta Raíz
class Animal(ABC):
    def __init__(self):
        self._sonido = ""
        self._alimentos = ""
        self._hábitat = ""
        self._nombreCientífico = ""

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass


# 2. Clases Intermedias Abstractas (Cánido y Felino)
class Canido(Animal, ABC):
    pass

class Felino(Animal, ABC):
    pass


# 3. Clases Concretas
class Gato(Felino):
    def get_nombre_cientifico(self):
        return "Felis silvestris catus"

    def get_sonido(self):
        return "Maullido"

    def get_alimentos(self):
        return "Ratones"

    def get_habitat(self):
        return "Doméstico"


class Perro(Canido):
    def get_nombre_cientifico(self):
        return "Canis lupus familiaris"

    def get_sonido(self):
        return "Ladrido"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Doméstico"


class Lobo(Canido):
    def get_nombre_cientifico(self):
        return "Canis lupus"

    def get_sonido(self):
        return "Aullido"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Bosque"


class León(Felino):
    def get_nombre_cientifico(self):
        return "Panthera leo"

    def get_sonido(self):
        return "Rugido"

    def get_alimentos(self):
        return "Carnívoro"

    def get_habitat(self):
        return "Praderas"


# 4. Clase de Prueba (Main)
if __name__ == "__main__":
    # Creamos un arreglo/lista de animales polimórfica
    animales = [Gato(), Perro(), Lobo(), León()]

    # Recorremos la lista mostrando la información de cada uno
    for animal in animales:
        print(animal.get_nombre_cientifico())
        print(f"Sonido: {animal.get_sonido()}")
        print(f"Alimentos: {animal.get_alimentos()}")
        print(f"Hábitat: {animal.get_habitat()}")
        print()