#Ejercicio 6:

print("Ejercicio 6: Definir una función inversa() que calcule la inversión de una cadena.")

def inversa(a):
    inv = ""
    for i in a:
        inv = i + inv 
    return inv

a = "estoy probando"
print("\nLa inversa de la cadena",a, "es:", inversa(a))

assert inversa(a) == "odnaborp yotse"
assert inversa(a) == "holanda que acelga"
