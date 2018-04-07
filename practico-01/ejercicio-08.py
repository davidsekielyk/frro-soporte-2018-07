#Ejercicio 7:
print("Ejercicio 8: Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. \nEscribir la función usando el bucle for anidado.\n")

def superposicion(a, b):
    for i in a:
        for j in b:
            if j == i:
                return True
    return False


a = [1, 2, 3, 4]
b = [4, 5, 6]

if superposicion(a, b):
    print("Las listas tienen al menos un miembro en comun :D")
else:
    print("Las listas no tienen miembros en comun")
