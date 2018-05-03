#Ejercicio 9:
print("Ejercicio 9: Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, 'x') debería devolver 'xxxxx'")

def generar_n_caracteres(n, c):
    mult = n * c
    return (mult)

a = 3
b = "g"

print("Multiplicamos el caracter",b, a, "veces:", generar_n_caracteres(a, b))

assert generar_n_caracteres(a, b) == "ggg"
assert generar_n_caracteres(a, b) == "gg"
