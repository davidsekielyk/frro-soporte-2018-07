#Ejercicio 1
print("""Ejercicio 1
Escribir una clase llamada rectángulo que contenga una base y una altura, y que contenga un
método que devuelva el área del rectángulo.
""")


class Triangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        print("El area del triangulo es:", self.base * self.altura)


triangulo = Triangulo(int(input("Ingrese la base del triangulo: ")),int(input("Ingrese la altura del triangulo: ")))
print()
triangulo.area()
