##PROGRAMA PRINCIPAL DE GESTOR DE TURNOS
# main.py - Gestion de turnos del taller CarUPS
# Entrega 1: Pila de historial de acciones

from pila import Pila, prueba_pila


def mostrar_menu():
    print("\n===== TALLER CarUPS =====")
    print("1. Registrar turno")
    print("2. Atender turno")
    print("3. Deshacer la última acción")
    print("4. Ver registro reciente")
    print("0. Salir")


def main():
    historial = Pila()  # R1

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            historial.push("Registrar turno: " + nombre)
            print("Accion registrada en el historial.")

        elif opcion == "2":
            nombre = input("Nombre del cliente: ")
            historial.push("Atender turno: " + nombre)
            print("Accion registrada en el historial.")

        elif opcion == "3":
            accion = historial.pop()
            if accion is None:
                print("No hay acciones para deshacer.")
            else:
                print("Se deshizo la accion:", accion)

        elif opcion == "4":
            print("Registros recientes:")
            historial.mostrar()

        elif opcion == "0":
            print("Hasta luego.")

        else:
            print("Opcion no valida.")

main()