# COLA FIFO

## Inicializa la clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

## Implementación de la Cola
class Cola:
    def __init__(self):
        self.head = None  # frente de la cola
        self.tail = None  # final de la cola 

    def is_empty(self):
        # revisa si está vacía
        return self.head is None

    def enqueue(self, dato):
        # encola en el final
        nuevo = Nodo(dato)
        if self.is_empty():
            self.head = nuevo
            self.tail = nuevo
        else:
            self.tail.siguiente = nuevo
            self.tail = nuevo

    def dequeue(self):
        # extrae el inicio
        if self.is_empty():
            return None  # cola vacía
        dato = self.head.dato
        self.head = self.head.siguiente
        if self.head is None:
            self.tail = None
        return dato

    def peek(self):
        # revisa el frente de la cola
        if self.is_empty():
            return None
        return self.head.dato

    def mostrar(self):
        # O(n): recorre todos los nodos
        if self.is_empty():
            print("No hay turnos en espera.")
            return
        actual = self.head
        numero = 1
        while actual:
            print(f"{numero}. Nombre: {actual.dato}")
            actual = actual.siguiente
            numero += 1


def prueba_cola():
    cola = Cola()
    assert cola.is_empty()
    cola.enqueue("Ana")
    cola.enqueue("Luis")
    cola.enqueue("Rosa")
    assert cola.peek() == "Ana"
    assert cola.dequeue() == "Ana"
    assert cola.dequeue() == "Luis"
    assert cola.dequeue() == "Rosa"
    assert cola.is_empty()
    assert cola.dequeue() is None
    cola.enqueue("Pedro")
    assert cola.peek() == "Pedro"
    print("Prueba de la cola: OK")


if __name__ == "__main__":
    prueba_cola()

