# AFD 

## Descripción
Este proyecto implementa un Autómata Finito Determinista (AFD) en Python.  
El programa lee cadenas binarias desde un archivo llamado `entrada.txt` y determina si cada cadena es aceptada o no por el autómata.

El resultado se muestra en consola indicando la cadena evaluada y si el autómata la acepta.

## Lenguaje reconocido
El autómata acepta todas las cadenas binarias que **comienzan con el símbolo 0**.

Alfabeto:

{0,1}


## Estados del autómata

- **q1** → Estado inicial
- **q2** → Estado de aceptación
- **q3** → Estado de rechazo


## Función de transición

q1,0 → q2
q1,1 → q3
q2,0 → q2
q2,1 → q2
q3,0 → q3
q3,1 → q3

## Ejecución del programa

Abrir la terminal en la carpeta del proyecto y ejecutar:

python AFD.py

