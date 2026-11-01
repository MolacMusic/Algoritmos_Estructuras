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
 
 
# ------------ R3: Socios registrados (conjunto) ---------
def crear_socios_ejemplo():
    ###Conjunto de identificadores de socios.
    return {"S001", "S002", "S003", "S004", "S005", "S006"}
 
 
def registrar_socio(socios, id_socio):
    ###Registra un socio. Devuelve False si ya estaba registrado.
    # registrar: O(1) en promedio (el set es una tabla hash)
    if id_socio in socios:
        return False
    socios.add(id_socio)
    return True
 
 
def socio_registrado(socios, id_socio):
    ###Verifica al instante si un identificador ya está registrado.
    # verificar pertenencia: O(1) en promedio
    return id_socio in socios

# ---------- R4: Análisis de préstamos (Op entre conjuntos) ---------
def crear_prestamos_ejemplo():
    ###Dos conjuntos de socios: con préstamos de novela y de ciencia.
    novela = {"S001", "S002", "S003"}
    ciencia = {"S003", "S004", "S005"}
    return novela, ciencia
 
 
def socios_ambos_generos(novela, ciencia):
    # intersección: O(min(n, m)) 
    return novela & ciencia
 
 
def socios_solo_novela(novela, ciencia):
    # diferencia: O(n) donde n = tamaño del conjunto novela
    return novela - ciencia
 
 
def total_socios_con_prestamos(novela, ciencia):
    # unión: O(n + m)
    return novela | ciencia
