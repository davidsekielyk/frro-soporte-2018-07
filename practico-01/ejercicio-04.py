#Ejercicio 4:

print("Ejercicio 4: Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.\n")

def esVocal(a):
    if ord(a) == 65 or  ord(a) == 69 or ord(a) == 73 or  ord(a) == 79 or ord(a) == 85 or  ord(a) == 97 or  ord(a) == 101 or  ord(a) == 105 or  ord(a) == 111 or  ord(a) == 117:
        return True

a = "f"
if esVocal(a):
    print("La letra ",a, " es una vocal")
else:
    print("La letra ",a, " es una consonante")
