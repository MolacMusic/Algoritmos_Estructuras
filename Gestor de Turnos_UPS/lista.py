#LISTA ENLAZADA


##Inicializa la clase Cliente
class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
 
    def __str__(self):
        return f"Nombre: {self.nombre} | Cedula: {self.cedula}"
 
 
def cedula_valida(cedula):
    # Valida un número de 10 dígitos
    return len(cedula) == 10 and cedula.isascii() and cedula.isdecimal()
 
##Inicializa la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
 
##Implementa la lista enlazada

class ListaClientes:
    def __init__(self):
        self.head = None  # cabeza/inicio de la lista
        self.tail = None  # ultimo nodo
 
    def is_empty(self):
        return self.head is None
 
    def buscar_por_nombre(self, nombre):
        #Operación O(n): recorre la lista y busca por nombre en no case sensitive.
        buscado = nombre.strip().casefold()
        actual = self.head
        while actual is not None:
            if actual.dato.nombre.casefold() == buscado:
                return actual.dato
            actual = actual.siguiente
        return None
 
    def agregar(self, cedula, nombre):
        # True si agrega, False si falla
        cedula = cedula.strip()
        nombre = nombre.strip()
        ##validación de nombres
        if not nombre:
            return False, "El nombre no puede estar vacio."
        if not cedula_valida(cedula):
            return False, "La cedula debe tener exactamente 10 digitos numericos."
        #Alerta de Nombre repetido
        if self.buscar_por_nombre(nombre) is not None:
            return False, "Ya existe un cliente con ese nombre."
        # Alertar si la cédula está repetida
        actual = self.head
        while actual is not None:
            if actual.dato.cedula == cedula:
                return False, "Ya existe un cliente con esa cedula."
            actual = actual.siguiente

        ##Después de validar todo ahora sí se agrega el nodo.
        nuevo = Nodo(Cliente(cedula, nombre)) #O(1)
        if self.is_empty():
            self.head = nuevo
            self.tail = nuevo
        else:
            self.tail.siguiente = nuevo
            self.tail = nuevo
        return True, "Cliente registrado."
 
    def mostrar(self):
        # O(n) recorre toda la lista desde el head
        if self.is_empty():
            print("No hay clientes registrados.")
            return
        actual = self.head
        numero = 1
        while actual is not None:
            print(f"{numero}. {actual.dato}")
            actual = actual.siguiente
            numero += 1
 
 
def prueba_lista():
    lista = ListaClientes()
    assert lista.is_empty()
    assert lista.buscar_por_nombre("Ana") is None
 
    assert lista.agregar("1234567890", "Ana")[0]
    assert lista.agregar("1098765432", "Luis")[0]
    assert not lista.agregar("123", "Rosa")[0]              # muy corta
    assert not lista.agregar("123456789012", "Rosa")[0]     # muy larga
    assert not lista.agregar("1234567890a", "Rosa")[0]      # con letra
    assert not lista.agregar("1111111111", "ana")[0]       # nombre repetido
    assert not lista.agregar("12345678901", "Pedro")[0]     # cedula repetida
    assert not lista.agregar("1111111111", "  ")[0]        # nombre vacio
 
    assert lista.buscar_por_nombre("luis").cedula == "1098765432"
    assert lista.buscar_por_nombre("Pedro") is None
    assert lista.head.dato.nombre == "Ana"
    assert lista.tail.dato.nombre == "Luis"
    print("Prueba de la lista: OK")
 
 
if __name__ == "__main__":
    prueba_lista()
