#Ejercicio 7
from datetime import datetime

print("""Crear una clase Ejercicio con los metodos:
    - inicio: se pasa una fecha y devuelve el 1 de julio anterior
    - fin: se pasa una fecha y devuelve el 30 de junio proximo
    - semana: devuelve el numero de semana contando a partir del 1 de julio anterior\n""")


class Ejercicio():
    def __init__(self, fecha):
        self.dia = fecha.day
        self.mes = fecha.month
        self.año = fecha.year
        self.semana = fecha.isocalendar()[1]

    def inicio(self):
        if self.mes >= 7:
            fecha = "1/7/" + str(self.año)
            return (fecha)
        else:
            fecha = "1/7/" + (str(self.año - 1))
            return(fecha)

    def fin(self):
        if self.mes <= 6:
            fecha = "30/6/" + str(self.año)
            return(fecha)
        else:
            fecha = "30/6/" + (str(self.año + 1))
            return(fecha)

    def nrosemana(self):
        if self.mes >= 7:
            fecha = "1/7/" + str(self.año)
            fecha = datetime.strptime(fecha, "%d/%m/%Y")
            return (self.semana - fecha.isocalendar()[1])
        else:
            fecha = "1/7/" + (str(self.año - 1))
            fecha = datetime.strptime(fecha, "%d/%m/%Y")
            return (self.semana + fecha.isocalendar()[1])


fecha = input("Fecha de nacimiento (dd/mm/aaaa): ")
fecha = datetime.strptime(fecha, "%d/%m/%Y")

ejercicio = Ejercicio(fecha)
print("\nMetodo incio:", ejercicio.inicio())
print("Metodo fin:", ejercicio.fin())
print("Metodo semana:", ejercicio.nrosemana())

