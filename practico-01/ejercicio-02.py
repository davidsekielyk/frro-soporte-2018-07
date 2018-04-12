#Ejercicio 2: Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
print("Ejercicio 2: Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.\n")

def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = 4544
b = 234
c = 663

print("EL maximo entre ",a, ", ",b, " y ",c, "es: ",max_de_tres(a, b, c))

assert max_de_tres(a, b, c) == a
assert max_de_tres(a, b, c) == b
assert max_de_tres(a, b, c) == c
