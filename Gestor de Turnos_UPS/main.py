## PROGRAMA PRINCIPAL DE GESTOR DE TURNOS
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

        ##Registra un cliente en el gestor
        if opcion == "1":
            nombre = input("Nombre: ").strip()
            ##El bucle permite ingresar la cédula sin salir por posibles errores de tipeo o conteo.
            while True:
                cedula = input("Cédula (10 dígitos): ").strip()
                ok, mensaje = clientes.agregar(cedula, nombre)
                print(mensaje)
                if ok:
                    historial.push("Registrar cliente: " + nombre)
                    break
                if "cedula debe tener" in mensaje.lower():
                    print("Intente nuevamente.")
                else:
                    break
       
        ##Función de buscar por nombre en el registro
        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            cliente = clientes.buscar_por_nombre(nombre)
            if cliente is None:
                print("Cliente no encontrado.")
            else:
                print("Encontrado ->", cliente)
        
        ##Muestra los clientes registrados
        elif opcion == "3":
            clientes.mostrar()
        #Permite agendar un turno para un cliente ya registrado o para un nuevo cliente registrándolo previamente
        elif opcion == "4":
            nombre = input("Nombre del cliente: ").strip()
            cliente = clientes.buscar_por_nombre(nombre)
            ##El bloque if permite que agendar un turno para un cliente no registrado
            if cliente is None:
                print(f"El cliente '{nombre}' no está registrado.")
                respuesta = input("¿Desea registrarlo? (s/n): ").strip().lower()
                if respuesta == "s":
                    while True:
                        cedula = input("Cédula (10 dígitos): ").strip()
                        ok, mensaje = clientes.agregar(cedula, nombre)
                        print(mensaje)
                        if ok:
                            historial.push("Registrar cliente: " + nombre)
                            cliente = clientes.buscar_por_nombre(nombre)
                            break

                        if "cedula debe tener" in mensaje.lower():
                            print("Intente nuevamente.")
                        else:
                            break
                else:
                    print("Registro cancelado.")

            if cliente is not None:
                turnos.enqueue(cliente.nombre)
                historial.push("Registrar turno: " + cliente.nombre)
                print(f"Turno registrado para {cliente.nombre}.")
      
      ##Atiende turnos por FIFO
        elif opcion == "5":
            atendido = turnos.dequeue()
            if atendido is None:
                print("No hay turnos en espera.")
            else:
                historial.push("Atender turno: " + atendido)
                print(f"Atendiendo a {atendido}.")
        
        #Turnos en espera
        elif opcion == "6":
            turnos.mostrar()

        #Elimina la última acción del historial
        elif opcion == "7":
            accion = historial.pop()
            if accion is None:
                print("El historial esta vacio.")
            else:
                print("Accion eliminada del historial:", accion)
        
        ##Muestra el historial de más reciente a más antiguo
        elif opcion == "8":
            print("Historial de últimos cambios")
            historial.mostrar()

        ##Prueba estructural, devuelve ok.
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
