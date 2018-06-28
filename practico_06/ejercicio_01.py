from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio

class NegocioSocio():

    def __init__(self):
        self.datos = DatosSocio()

    def reglas(self,nuevoSocio):
        b = True
        e = ""

        #Regla-1
        cant_dni = self.datos.session.query(Socio).filter(Socio.dni == nuevoSocio.dni).count()
        if cant_dni > 0:
            b = False
            e = "Ya existe ese DNI"

        #Regla-2
        if len(nuevoSocio.nombre) < 3 or len(nuevoSocio.nombre) > 15:
            b = False
            e = "Longitud del nombre menor a 3 o mayor a 15 caracteres"

        if len(nuevoSocio.apellido) < 3 or len(nuevoSocio.apellido) > 15:
            b = False
            e = "Longitud del apellido menor a 3 o mayor a 15 caracteres"

        #Regla-3
        if nuevoSocio.dni < 1000000:
            b = False
            e = "DNI no existe"

        #Regla-4
        cant_socios = self.datos.session.query(Socio).count()
        if cant_socios >= 200:
            b = False
            e = "Cantidad max de socios(200)"

        return b,e

    def alta(self,nuevoSocio):
        b = self.reglas(nuevoSocio)
        if b[0]:
            return self.datos.alta(nuevoSocio)
        else:
            return b[0],b[1]

    def borrar(self,viejoSocio):
        return self.datos.borrar(viejoSocio)

    def modificar(self,viejoSocio):
        return self.datos.modificar(viejoSocio)

    def buscar(self,id):
        return self.datos.buscar(id)

    def todos(self):
        return self.datos.todos()
