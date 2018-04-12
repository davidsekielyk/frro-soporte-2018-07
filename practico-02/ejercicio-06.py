#Ejercicio 6
from datetime import datetime
import random


print("""Ejercicio 6:
Programar una clase Persona con un constructor donde reciba una fecha de nacimiento (objeto datetime.datetime).
    # La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la persona (entero).
    # Para obtener la fecha actual, usar el metodo de clase "now" de la clase datetime (ya importada).""")


class Persona:
    def __init__(self, nacimiento):
        self.fecha_nac = nacimiento

    def edad(self):
        time = datetime.now()
        if (time.month < self.fecha_nac.month) or ((time.month == self.fecha_nac.month) and (time.day < self.fecha_nac.day)):
            return (int(time.year) - int(self.fecha_nac.year) - 1)
        else:
            return (int(time.year) - int(self.fecha_nac.year))

print()
#print("Fecha de nacimiento:")
#f_nac = datetime(int(input("Año: ")), int(input("Mes: ")), int(input("Dia: ")))

f_nac = input("Fecha de nacimiento (dd/mm/aaaa): ")
f_nac = datetime.strptime(f_nac, "%d/%m/%Y")

print()
persona = Persona(f_nac)
print("Edad:", persona.edad(), "años")
