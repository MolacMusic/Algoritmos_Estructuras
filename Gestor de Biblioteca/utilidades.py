# (Gestor de Préstamos - Biblioteca U. de Cuenca)
##utilidades.py - Funciones auxiliares 

# R2: SortedDict funge de estructura para el TreeMap
# Instala Sorted para ordenar. Sino Sort.
try:
    from sortedcontainers import SortedDict
except ImportError:
    SortedDict = None


# ----------- R1: Diccionario (HashMap)-------
def crear_catalogo_ejemplo():
    ###Catálogo inicial: clave = código del libro, valor = dict con título y autor.###
    return {
        "L010": {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
        "L003": {"titulo": "Huasipungo", "autor": "Jorge Icaza"},
        "L025": {"titulo": "Introduction to Algorithms", "autor": "Thomas H. Cormen"},
        "L001": {"titulo": "Cosmos", "autor": "Carl Sagan"},
        "L017": {"titulo": "Los Sangurimas", "autor": "José de la Cuadra"},
    }


"""Registra un libro. Devuelve False si el código ya existe."""
def registrar_libro(catalogo, codigo, titulo, autor):

    # registrar: O(1) en promedio (inserta en la tabla hash)
    if codigo in catalogo:
        return False
    catalogo[codigo] = {"titulo": titulo, "autor": autor}
    return True


"""Busca un libro por su código. Devuelve None si no existe."""
def buscar_libro(catalogo, codigo):
    # buscar por clave: O(1) en promedio (hash -> índice directo)
    return catalogo.get(codigo)


# ------------ R2: Catálogo ordenado (TreeMap) ---------
def catalogo_ordenado(catalogo):
    ###Devuelve el catálogo ordenado por código de libro.
    # ordenar: O(n log n)
    # recorrer el TreeMap es: O(n) ya que está balanceado.
    if SortedDict is not None:
        return SortedDict(catalogo)
    return dict(sorted(catalogo.items()))
