# PROGRAMA DE GESTOR DE TURNOS CAR UPS
## Elaborado por: Alan Guillermo Peñafiel Gonzalez

Programa en Python para gestionar clientes y turnos de un taller mecánico a base de Pilas, Colas y Listas enlazadas.

Se ejecuta el programa desde el main.py


### Opciones del menú
1. **Registrar cliente:** ingresa el nombre y la cédula.
2. **Buscar cliente:** busca por nombre.
3. **Ver clientes:** muestra los clientes registrados.
4. **Registrar turno:** genera un turno para un cliente registrado o permite registrarlo.
5. **Atender turno:** atiende al siguiente cliente en espera.
6. **Ver turnos:** muestra los turnos pendientes.
7. **Eliminar última acción:** elimina la acción más reciente del historial.
8. **Ver historial:** muestra las acciones registradas.
9. **Ejecutar pruebas:** comprueba el funcionamiento de las estructuras de datos.
0. **Salir:** cierra el programa.

**Importante:** ingresar cédulas de exactamente 10 dígitos numéricos, sin letras ni espacios.

### Estructuras de Datos Utilizadas

| Archivo | Estructura | Función |
|---|---|---|
| `lista.py` | Lista enlazada | Almacena y permite buscar clientes. |
| `cola.py` | Cola FIFO | Administra los turnos por orden de llegada. |
| `pila.py` | Pila LIFO | Conserva el historial de acciones y registros. |
| `main.py` | Programa principal | Integra las estructuras y el menú interactivo. |
