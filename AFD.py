def evaluar(cadena):

    transiciones = {
        ("q1", "0"): "q2",
        ("q1", "1"): "q3",
        ("q2", "0"): "q2",
        ("q2", "1"): "q2",
        ("q3", "0"): "q3",
        ("q3", "1"): "q3"
    }

    estado = "q1"

    for simbolo in cadena:
        if (estado, simbolo) in transiciones:
            estado = transiciones[(estado, simbolo)]
        else:
            return False

    return estado == "q2"  


with open("entrada.txt", "r") as archivo:
    for linea in archivo:
        cadena = linea.strip()

        if evaluar(cadena):
            print(cadena, ": ACEPTA")
        else:
            print(cadena, ": NO ACEPTA")
