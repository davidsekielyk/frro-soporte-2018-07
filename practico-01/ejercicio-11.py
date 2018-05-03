#Ejercicio 11:
print("Ejercicio 11: Determinar la cantidad de dígitos de un número ingresado.\n")

#a = int(input("Escriba el numero: "))
a = 324

cont = 1
i = 1
rta = a / i
while rta > 10 or rta < 1:
    cont = cont + 1
    i = i*10
    rta = a / i

print("La cantidad de digitos del numero",a, "es:",cont)
