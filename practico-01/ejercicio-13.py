#Elercicio 13:
print("Ejercicio 13: Programe una funcion que determine si un numero entero suministrado como argumento es primo.\n")

def es_primo(a):
    for i in range(a-2):
        if (a%(i+2)) == 0:
            return False
    return True

nro = int(input("Ingrese numero: "))
if es_primo(nro):
    print("El numero", nro, "es primo")
else:
    print("El numero", nro, "no es primo")
