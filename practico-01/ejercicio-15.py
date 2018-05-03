#Ejercicio 15:
print("Ejercicio 15: Reescribe el programa que pide al usuario una lista de números e imprime en pantalla el máximo y mínimo de los números introducidos al final, \ncuando el usuario introduce “fin”. Escribe ahora el programa de modo que almacene los números que el usuario introduzca en una lista y usa las funciones Max () y min () \npara calcular los números máximo y mínimo después de que el bucle termine.\n")

lista = []

a = input("Ingrese un numero (o 'fin' para cortar): ")
while a != "fin":
    lista.append(int(a))
    a = input("Ingrese un numero (o 'fin' para cortar): ")

print("\nEl mayor numero de la lista es:",max(lista), "\nEl menor numero de la lista es:",min(lista))
