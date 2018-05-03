#Ejercicio 4
import random
print("""Ejercicio 4
Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
     Atributos: nombre de la carrera, año de ingreso a la misma, cantidad de materias de la carrera, y cantidad de materias aprobadas.
     Metodos:
        o avance(): indica que porcentaje de la carrera tiene aprobada.
        o edad_ingreso(): indica que edad tenia al ingresar a la carrera.""")


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

class Estudiante(Persona):
    def __init__(self,nombre, edad, sexo,peso, altura, nom_c, a_ing, cant_tot_mat, cant_mat_ap):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()
        self.nomnre_carrera = nom_c
        self.anio_ing = a_ing
        self.cant_tot_materias = cant_tot_mat
        self.cant_materias_ap = cant_mat_ap

    def avance(self):
        print("Porcentaje de la carrera aprobada:", (self.cant_materias_ap * 100) / self.cant_tot_materias,"%")

    def edad_ingreso(self):
        print("Edad al ingresar:", self.edad - (2018 - self.anio_ing))

print()
estudiante = Estudiante(input("Ingrese nombre: "), int(input("Ingrese edad: ")), input("Ingrese sexo (M/F): "),
                        int(input("Ingrese peso: ")), int(input("Ingrese altura (en cm): ")), input("Nombre de la carrera: "),
                        int(input("Año de ingreso: ")), int(input("Cantidad total de materias de la carrera: ")),
                        int(input("Cantidad de materias aprobadas: ")))
print()
estudiante.print_data()
estudiante.avance()
estudiante.edad_ingreso()
