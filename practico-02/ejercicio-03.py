# Ejercicio 3
import random

print("""Ejercicio 3
Escribir una clase llamada Persona que cumpla las siguientes condiciones:
     Atributos: nombre, edad, sexo (H hombre, M mujer), peso, altura.
     Métodos:
        o es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
        o print_data(): imprime por pantalla toda la información del objeto.
        o generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo DNI. Llamar desde el método __init__, solo una vez.""")


class Persona():
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True

    def print_data(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nSexo:", self.sexo, "\nPeso:", self.peso, "\nAltura:",
              self.altura, "\nDNI:", self.dni)

    def generar_dni(self):
        return random.randint(00000000, 99999999)

print()
persona = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")), input("Ingrese sexo (M/F): "), int(input("Ingrese peso: ")), int(input("Ingrese altura (en cm): ")))
print()
if persona.es_mayor_edad():
    print(persona.nombre, "es mayor de edad.")
else:
    print(persona.nombre,"es menor de edad.")
persona.print_data()

