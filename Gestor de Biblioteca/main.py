#Gestor de Préstamos para la Biblioteca de la Universidad de Cuenca
#Parte 1.
###Implementación del diccionario y el treeMap.

from utilidades import (
    crear_catalogo_ejemplo,
    registrar_libro,
    buscar_libro,
    catalogo_ordenado,
)


def mostrar_menu():
    print("\n=== Biblioteca de la Universidad de Cuenca ===")
    print("1. Registrar nuevo libro")
    print("2. Buscar libro por código")
    print("3. Mostrar catálogo ordenado por código")
    print("0. Salir")


def main():
    catalogo = crear_catalogo_ejemplo()

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

        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
