#Gestor de Préstamos para la Biblioteca de la Universidad de Cuenca
#Parte 2.
###Implementación del diccionario y el treeMap (R1, R2) y de los conjuntos (R3, R4).

from utilidades import (
    crear_catalogo_ejemplo,
    registrar_libro,
    buscar_libro,
    catalogo_ordenado,
    crear_socios_ejemplo,
    registrar_socio,
    socio_registrado,
    crear_prestamos_ejemplo,
    socios_ambos_generos,
    socios_solo_novela,
    total_socios_con_prestamos,
)


def mostrar_menu():
    print("\n=== Biblioteca de la Universidad de Cuenca ===")
    print("1. Registrar nuevo libro")
    print("2. Buscar libro por código")
    print("3. Mostrar catálogo ordenado por código")
    print("4. Registrar socio")
    print("5. Verificar si un socio está registrado")
    print("6. Registrar préstamo (novela / ciencia)")
    print("7. Análisis de préstamos")
    print("0. Salir")


def main():
    catalogo = crear_catalogo_ejemplo()
    socios = crear_socios_ejemplo()
    prestamos_novela, prestamos_ciencia = crear_prestamos_ejemplo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código del libro: ").strip().upper()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            if registrar_libro(catalogo, codigo, titulo, autor):
                print("Libro registrado correctamente.")
            else:
                print(f"Ya existe un libro con el código {codigo}.")

        elif opcion == "2":
            codigo = input("Código a buscar: ").strip().upper()
            libro = buscar_libro(catalogo, codigo)
            if libro:
                print(f"{codigo}: {libro['titulo']} - {libro['autor']}")
            else:
                print("No existe un libro con ese código.")

        elif opcion == "3":
            print("\nCatálogo ordenado por código:")
            for codigo, libro in catalogo_ordenado(catalogo).items():
                print(f"{codigo} | {libro['titulo']} | {libro['autor']}")

        elif opcion == "4":
            id_socio = input("Identificador del socio: ").strip().upper()
            if registrar_socio(socios, id_socio):
                print("Socio registrado correctamente.")
            else:
                print("Ese socio ya estaba registrado (no se duplica).")

        elif opcion == "5":
            id_socio = input("Identificador del socio: ").strip().upper()
            if socio_registrado(socios, id_socio):
                print("El socio SÍ está registrado.")
            else:
                print("El socio NO está registrado.")

        elif opcion == "6":
            id_socio = input("Identificador del socio: ").strip().upper()
            if not socio_registrado(socios, id_socio):
                print("Primero debe registrar al socio.")
                continue
            genero = input("Género (novela/ciencia): ").strip().lower()
            if genero == "novela":
                prestamos_novela.add(id_socio)
                print("Préstamo de novela registrado.")
            elif genero == "ciencia":
                prestamos_ciencia.add(id_socio)
                print("Préstamo de ciencia registrado.")
            else:
                print("Género no válido.")

        elif opcion == "7":
            ambos = socios_ambos_generos(prestamos_novela, prestamos_ciencia)
            solo_novela = socios_solo_novela(prestamos_novela, prestamos_ciencia)
            total = total_socios_con_prestamos(prestamos_novela, prestamos_ciencia)
            print("\n--- Análisis de préstamos ---")
            print(f"Leen ambos géneros (intersección): {sorted(ambos)}")
            print(f"Solo leen novela (diferencia):     {sorted(solo_novela)}")
            print(f"Total de socios con préstamos (unión): {len(total)} -> {sorted(total)}")

        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
