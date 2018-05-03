#Ejercicio 12
print("Ejercicio 12: Determinar la suma de todos los numeros de 1 a N. N es un número que se ingresa por consola.\n")

a = int(input("ingrese un numero: "))

rdo = 0
for i in range(a):
    rdo = rdo + (a - i)

print("La suma de todos los numeros de 1 a",a, "es:",rdo)
