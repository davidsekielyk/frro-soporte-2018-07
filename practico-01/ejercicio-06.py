#Ejercicio 6:

print("Ejercicio 6: Definir una función inversa() que calcule la inversión de una cadena.")

def inversa(a):
    inv = ""
    for i in range(len(a)):
        inv = inv + (a[-(i+1)])
    return inv

a = "estoy probando"
print("\nLa inversa de la cadena",a, "es:", inversa(a))
