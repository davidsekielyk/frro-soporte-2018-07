from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_03 import DatosSocio


def pruebas():

    # alta
    datos = DatosSocio()
    socio = Socio(idSoci=111, dni=12345678, nombre="Juan", apellido="Perez")
    b = datos.alta(socio)
    assert b[0] == True

    # baja
    assert datos.borrar(socio)[0] == True

    # buscar
    socio_2 = Socio(idSoci=112, dni=12345679, nombre='Carlos', apellido='Perez')
    datos.alta(socio_2)
    assert datos.buscar(socio_2.idSoci) == socio_2

    # modificacion
    socio_3 = Socio(idSoci=113, dni=12345680, nombre='Susana', apellido='Gimenez')
    datos.alta(socio_3)
    socio_3_modif = datos.buscar(socio_3.idSoci)
    socio_3_modif.nombre = 'Moria'
    socio_3_modif.apellido = 'Casan'
    socio_3_modif.dni = 13264587
    b = datos.modificar(socio_3_modif)
    assert b[0] == True

    # todos
    assert len(datos.todos()) == 2

    # buscar dni
    socio_4 = Socio(idSoci=114, dni=12345678, nombre='Carlos', apellido='Perez')
    datos.alta(socio_4)
    assert datos.buscarDNI(socio_4.dni) == 1


if __name__ == '__main__':
    pruebas()
