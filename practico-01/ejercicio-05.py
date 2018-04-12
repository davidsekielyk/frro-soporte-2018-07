#Ejercicio 5:

print("Ejercicio 5: Escribir una función multip() que multiplique respectivamente todos los números de una lista.\n")

def multip(a):
    rdo = 1
    for i in a:
        rdo = rdo * i
    return rdo

a = [1, 2, 3, 4]
print(multip(a))

assert multip(a)==24
assert multip(a)==27
