#Ejercicio 5
import random

print("""Ejercicio 5: 
Escribir una funcion que tome como parámetro una lista de Estudiantes, y devuelva un diccionario
con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.""")

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
        self.nombre_carrera = nom_c
        self.anio_ing = a_ing
        self.cant_tot_materias = cant_tot_mat
        self.cant_materias_ap = cant_mat_ap

    def avance(self):
        print("Porcentaje de la carrera aprobada:", (self.cant_materias_ap * 100) / self.cant_tot_materias,"%")

    def edad_ingreso(self):
        print("Edad al ingresar:", self.edad - (2018 - self.anio_ing))


luis = Estudiante("Luis", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
carlos = Estudiante("Carlos", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
juan = Estudiante("Juan", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
david = Estudiante("David", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
lucas = Estudiante("Lucas", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
maria = Estudiante("Maria", random.randint(18, 30), "F", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
julia = Estudiante("Julia", random.randint(18, 30), "F", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
carla = Estudiante("Carla", random.randint(18, 30), "F", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
fernando = Estudiante("Fernando", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
ricardo = Estudiante("Ricardo", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))
aristobulo = Estudiante("Aristobulo", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "ISI", random.randint(2010, 2018), 50, random.randint(0, 50))

lucre = Estudiante("Lucre", random.randint(18, 30), "F", random.randint(65, 150), random.randint(150, 210), "IQ", random.randint(2010, 2018), 43, random.randint(0, 43))
sofia = Estudiante("Sofia", random.randint(18, 30), "F", random.randint(65, 150), random.randint(150, 210), "IQ", random.randint(2010, 2018), 43, random.randint(0, 43))
micaela = Estudiante("Micaela", random.randint(18, 30), "F", random.randint(65, 150), random.randint(150, 210), "IQ", random.randint(2010, 2018), 43, random.randint(0, 43))
lucia = Estudiante("Lucia", random.randint(18, 30), "F", random.randint(65, 150), random.randint(150, 210), "IQ", random.randint(2010, 2018), 43, random.randint(0, 43))
francisco = Estudiante("Fransisco", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "IQ", random.randint(2010, 2018), 43, random.randint(0, 43))
martin = Estudiante("Martin", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "IQ", random.randint(2010, 2018), 43, random.randint(0, 43))
cristian = Estudiante("Cristian", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "IQ", random.randint(2010, 2018), 43, random.randint(0, 43))

alejandro = Estudiante("Alejandro", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "IE", random.randint(2010, 2018), 55, random.randint(0, 55))
ivan = Estudiante("Ivan", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "IE", random.randint(2010, 2018), 55, random.randint(0, 55))
jeff = Estudiante("Jeff", random.randint(18, 30), "M", random.randint(65, 150), random.randint(150, 210), "IE", random.randint(2010, 2018), 55, random.randint(0, 55))


def do_dic(lista):
    dicc_carreras = {}
    for i in lista:
        if i.nombre_carrera in dicc_carreras:
            dicc_carreras[i.nombre_carrera] = dicc_carreras[i.nombre_carrera] + 1
        else:
            dicc_carreras[i.nombre_carrera] = 1
    return dicc_carreras


lista_estudiantes = [luis, carlos, juan, david, lucas, maria, julia, carla, fernando, ricardo, aristobulo,
                     lucre, sofia, micaela, lucia, francisco, martin, cristian, alejandro, ivan, jeff]
print(do_dic(lista_estudiantes))
