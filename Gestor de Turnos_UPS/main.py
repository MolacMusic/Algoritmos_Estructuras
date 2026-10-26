##PROGRAMA PRINCIPAL DE GESTOR DE TURNOS

# main.py - Gestion de turnos del taller CarUPS
# Integra: Pila (historial), Cola (turnos) y Lista enlazada (clientes)

from pila import Pila, prueba_pila
from cola import Cola, prueba_cola
from lista import ListaClientes, prueba_lista


def mostrar_menu():
    print("\n===== TALLER CarUPS =====")
    print("1. Registrar cliente (cedula y nombre)")
    print("2. Buscar cliente por nombre")
    print("3. Ver clientes registrados")
    print("4. Registrar turno")
    print("5. Atender siguiente turno")
    print("6. Ver turnos en espera")
    print("7. Eliminar ultima accion del historial")
    print("8. Ver historial de acciones")
    print("9. Ejecutar pruebas")
    print("0. Salir")


def main():
    historial = Pila()
    turnos = Cola()
    clientes = ListaClientes()

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Elija una opcion: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            while True:
                cedula = input("Cédula: ").strip()
                if not cedula.isdigit() or len(cedula) != 10:
                    print("La cedula debe tener 10 digitos. Intente nuevamente.")
                else:
                    break
            ok, mensaje = clientes.agregar(cedula, nombre)
            print(mensaje)
            if ok:
                historial.push("Registrar cliente: " + nombre)


        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            cliente = clientes.buscar_por_nombre(nombre)
            if cliente is None:
                print("Cliente no encontrado.")
            else:
                print("Encontrado ->", cliente)

        elif opcion == "3":
            clientes.mostrar()

        elif opcion == "4":
            nombre = input("Nombre del cliente: ")
            cliente = clientes.buscar_por_nombre(nombre)
            if cliente is None:
                print("El cliente no esta registrado. Use la opcion 1 primero.")
            else:
                # Los turnos se manejan solo por nombre
                turnos.enqueue(cliente.nombre)
                historial.push("Registrar turno: " + cliente.nombre)
                print("Turno registrado.")

        elif opcion == "5":
            atendido = turnos.dequeue()
            if atendido is None:
                print("No hay turnos en espera.")
            else:
                historial.push("Atender turno: " + atendido)
                print(f"Atendiendo a {atendido}.")

        elif opcion == "6":
            turnos.mostrar()

        elif opcion == "7":
            accion = historial.pop()
            if accion is None:
                print("El historial esta vacio.")
            else:
                print("Accion eliminada del historial:", accion)

        elif opcion == "8":
            print("Historial (de la mas reciente a la mas antigua):")
            historial.mostrar()

        elif opcion == "9":
            prueba_pila()
            prueba_cola()
            prueba_lista()

        elif opcion == "0":
            print("Hasta luego.")

        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()
