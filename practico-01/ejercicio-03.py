#Ejercicio 3: Definir una función que calcule la longitud de una lista o una cadena dada
print("Ejercicio 3: Definir una función que calcule la longitud de una lista o una cadena dada\n")

def cont_longitud(a):
    contador = 0
    for i in a:
        contador=contador+1
    return contador

a = "(#-_-) ElDavo&ElChispo (#o_o)"
print("La longitud de la cadena",a, "es: ", cont_longitud(a))
