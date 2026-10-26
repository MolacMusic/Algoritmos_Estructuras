#PILA LIFO 
###Controla el historial de acciones y registros del gestor
#------------------------------

##Inicializa la clase nodo
class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

##El método LIFO es el adecuado ya que es el que permite mediante su método pop permite eliminar o "deshacer" la última acción realizada.
##Implenetación de la íla
class Pila:
    def __init__(self):
        self.cima = None

    def is_empty(self):
        # Revisa si la pila está vacía para evitar el underflow
        return self.cima is None

    def push(self, dato):
        #O(1) se crea un nuevo nodo y se enlaza a la cima/head
        self.cima = Nodo(dato, self.cima)

    def pop(self):
        #O(1) -> se saca solo el nodo de la cima/head
        if self.is_empty():
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

    def peek(self):
        # O(1) vigila la cima o cabecera.
        if self.is_empty():
            return None
        return self.cima.dato

    def mostrar(self):
        #de grado O(n): Recorre todos los nodos.
        if self.is_empty():
            print("El historial esta vacio.")
            return
        ##Recorrido de la pila general (se recorre hasta que está vacía, none)
        actual = self.cima
        while actual is not None:
            print("-", actual.dato)
            actual = actual.siguiente


def prueba_pila():
    pila = Pila()
    assert pila.is_empty()
    pila.push("Registrar turno")
    pila.push("Atender turno")
    ##Compara por LIFO si la cima es el último elemento agregado.
    assert pila.peek() == "Atender turno" 
    assert pila.pop() == "Atender turno"   
    assert pila.pop() == "Registrar turno"
    assert pila.is_empty()
    assert pila.pop() is None              # pop con la pila vacia
    print("Prueba de la pila: OK")


if __name__ == "__main__":
    prueba_pila()
