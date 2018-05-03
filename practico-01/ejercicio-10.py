#Ejercicio 10:
print("Ejercicio 10: Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.\n")

def mas_larga(lista):
    maxLen = 0
    for i in lista:
        if len(i) > maxLen:
            maxLen = len(i)
            palabra = i
    return palabra

a = ["hola", "que", "tal"]
print("La palabra mas larga de la lista es:", mas_larga(a))
