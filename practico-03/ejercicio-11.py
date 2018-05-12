#Ejercicio 11

import sys

print("""Ejercicio 11: Programar una función Divide que ingresa dos valores x, y y devuelve el cociente x/y. 
La función tiene que tener control de error, que imprima el nombre y el tipo de error.
Ejemplos: Divide(6,0) Divide(60,”hola”) Divide(True,5) \n""")

x = input("Ingrese primer valor: ")
y = input("Ingrese segundo valor: ")

try:
    print("El cociente de %s y %s es: "%(x,y), int(x)/int(y))
except:
    e = sys.exc_info()[1]
    print("\nLE ERRASTE PA:", e.args[0])
