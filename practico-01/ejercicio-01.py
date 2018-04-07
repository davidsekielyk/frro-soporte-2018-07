#Trabajo Practico 1 - Grupo 7 - (#-_-) ElDavo&ElChispo (#o_o)

#Ejercicio 1: Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
print("Ejercicio 1: Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.\n")

def maximo(a, b):
    if a > b:
        return a
    else:
        return b

a = 12
b = 23
print("EL maximo entre ",a, " y ",b," es: ",maximo(a,b))
