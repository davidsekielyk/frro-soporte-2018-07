#Ejercicio 4:

print("Ejercicio 4: Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.\n")

def esVocal(a):
    if a in vocales:
        return True

a = "f"
vocales = ['a','e','i','o','u']

if esVocal(a.lower()):
    print("La letra ",a, " es una vocal")
else:
    print("La letra ",a, " es una consonante")
