# PROGRAMA DE GESTOR DE PRÉSTAMOS PARA UNA BIBLIOTECA UNIVERSITARIA
## Elaborado por: Alan Guillermo Peñafiel Gonzalez

Programa en Python para gestionar los registros y préstamos de la biblioteca de la Universidad de Cuenca

## Cómo ejecutar
```bash
pip install sortedcontainers   
python main.py
```

## Archivos
 `main.py`: menú de consola principal.
 
 `utilidades.py`: funciones de cada requerimiento.

## Menú de Opciones

`1. Registrar nuevo libro`

`2. Buscar libro por código`

`3. Mostrar catálogo ordenado por código`

`4. Registrar socio`

`5. Verificar si un socio está registrado`

##Tabla de Complejidades

| Requerimiento | Operación principal | Complejidad |
|---|---|---|
| R1 | Registrar / buscar por código | O(1) promedio |
| R2 | Ordenar catálogo | O(n log n) |
| R3 | Registrar / verificar socio | O(1) promedio |
| R4 | Intersección / diferencia / unión | O(min(n,m)) / O(n) / O(n+m) |
