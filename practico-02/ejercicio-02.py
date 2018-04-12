#Ejercicio 2
from math import pi
print("""Ejercicio 2
Escribir una clase llamada círculo que contenga un radio, con un método que devuelva el área y
otro que devuelva el perímetro del círculo.""")

class Circulo():
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        print("El area del circulo es:", pi * self.radio * self.radio)

    def perimetro(self):
        print("El perimetro del circulo es:", 2 * pi * self.radio)

print()
circulo = Circulo(int(input("Ingrese radio del circulo: ")))
print()
circulo.area()
print()
circulo.perimetro()
    
