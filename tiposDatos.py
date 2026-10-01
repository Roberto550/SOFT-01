"""
Variables: Un espacio en la memoria de la computadora donde se guarda un dato 
Sintaxis: nombreVariable = datoQueAlmacenaLaVariable

Tipos de variables:
    - Números: 12, 12.3, -25, -63.78
    - String: "Alexander", "ABF-222"
    - Boolean: true/false, verdadero/falso, 1/0
"""
nombreJugador = "Camila"
nombreJugador = "Rose" 
nombreJugador = input("Ingrese su nombre (presione enter para continuar): ")
print("Bienvenido(a)", nombreJugador)

# Conversión de datos 
puntaje = int(input("Ingrese su puntaje: "))
print("Su puntaje más 5 es: ", puntaje + 5)

tipoCambio = float(input("El tipo de cambio del euro: "))
print("El tipo de cambio del euro es: ", tipoCambio + 5)