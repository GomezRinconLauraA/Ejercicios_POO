class ArticuloCientifico:
   #Define objetos de tipo ArticuloCientifico con un título, autor, palabras clave, año de publicación y un resumen.

    def __init__(self, titulo: str, autor: str, palabras_claves: list = None, 
                 publicacion: str = "", año: int = 0, resumen: str = ""):
        
        self._titulo = titulo
        self._autor = autor
        # Si no se pasan palabras clave, inicializamos una lista vacía
        self._palabras_claves = palabras_claves if palabras_claves is not None else []
        self._publicacion = publicacion
        self._año = año
        self._resumen = resumen

    def imprimir(self):
       
        print(f"Título del artículo = {self._titulo}")
        print(f"Autor del artículo = {self._autor}")
        print("Palabras clave = ")
        
        # Recorre la lista para imprimir cada palabra clave
        for palabra in self._palabras_claves:
            print(palabra)
            
        print(f"Publicación = {self._publicacion}")
        print(f"Año = {self._año}")
        print(f"Resumen = {self._resumen}")


# Método main que instancia un artículo científico y muestra sus datos
if __name__ == "__main__":
    # palabras clave
    palabras = ["Física", "Espacio", "Tiempo"]
    
    articulo = ArticuloCientifico(
        titulo="La teoría especial de la relatividad",
        autor="Albert Einstein",
        palabras_claves=palabras,
        publicacion="Anales de Física",
        año=1913,
        resumen="Las leyes de la física son las mismas en todos los sistemas de referencia inerciales."
    )
    
    # Imprimimos los valores
    articulo.imprimir()