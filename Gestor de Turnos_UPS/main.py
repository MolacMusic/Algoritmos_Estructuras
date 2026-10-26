##PROGRAMA PRINCIPAL DE GESTOR DE TURNOS
# main.py - Gestion de turnos del taller CarUPS
# Entrega 1: Pila de historial de acciones

# main.py - Gestion de turnos del taller CarUPS
# Integra: Pila (historial) y Cola (turnos)

from pila import Pila, prueba_pila
from cola import Cola, prueba_cola


def mostrar_menu():
    print("\n===== TALLER CarUPS =====")
    print("1. Registrar turno")
    print("2. Atender siguiente turno")
    print("3. Ver turnos en espera")
    print("4. Eliminar ultima accion del historial")
    print("5. Ver historial de acciones")
    print("6. Ejecutar pruebas")
    print("0. Salir")


def main():
    historial = Pila()
    turnos = Cola()

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            turnos.enqueue(nombre)
            historial.push("Registrar turno: " + nombre)
            print("Turno registrado.")

        elif opcion == "2":
            atendido = turnos.dequeue()
            if atendido is None:
                print("No hay turnos en espera.")
            else:
                historial.push("Atender turno: " + atendido)
                print(f"Atendiendo a {atendido}.")

        elif opcion == "3":
            turnos.mostrar()

        elif opcion == "4":
            accion = historial.pop()
            if accion is None:
                print("El historial esta vacio.")
            else:
                print("Accion eliminada del historial:", accion)

        elif opcion == "5":
            print("Historial (de la mas reciente a la mas antigua):")
            historial.mostrar()

        elif opcion == "6":
            prueba_pila()
            prueba_cola()

        elif opcion == "0":
            print("Hasta luego.")

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
