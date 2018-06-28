from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


def opMenu():
    print("Ingrese una de las siguientes opciones")
    print("1-Alta")
    print("2-Borrar")
    print("3-Modificar")
    print("4-Buscar")
    print("5-Todos")
    print("0-Terminar")
    global op
    b = True
    while b:
        try:
            op = int(input("Opcion: "))
            b = False
        except:
            print("Ingresa un numero (-.-) ")

def nuevoSocio():
    ns = Socio()
    print("\nIngrese los datos de un nuevo socio:")
    ns.idSoci = int(input("ID: "))
    ns.dni = int(input("DNI: "))
    ns.nombre = input("Nombre: ")
    ns.apellido = input("Apellido: ")
    return ns

def viejoSocio():
    id = int(input("\nIngresa id del socio que quieres eliminar: "))
    vs = ds.buscar(id)
    return vs

def modificarSocio():
    ms = Socio()
    ms.idSoci = int(input("Ingrese ID del socio que quiere modificar: "))
    print("\nIngrese los datos que quiere modificar del socio:")
    ms.dni = int(input("DNI: "))
    ms.nombre = input("Nombre: ")
    ms.apellido = input("Apellido: ")
    return ms


ds = DatosSocio()
opMenu()
while op != 0:
    if op == 1:
        ns = nuevoSocio()
        b = ds.alta(ns)
        if b[0]:
            print("Se ha registrado un nuevo socio\n")
        else:
            print("\nYa existe esa persona")
            print("ERROR:", b[1].args[0])
    elif op == 2:
        vs = viejoSocio()
        b = ds.borrar(vs)
        if b[0]:
            print("Se ha eliminado un socio\n")
        else:
            print("\nNo se ha podido eliminar el socio")
            print("ERROR:", b[1].args[0])
    elif op == 3:
        ms = modificarSocio()
        b = ds.modificar(ms)
        if b[0]:
            print("Se ha modificado un socio\n")
        else:
            print("\nNo se ha podido modificar el socio")
            print("ERROR:", b[1].args[0])
    elif op == 4:
        id = int(input("\nIngresa id del socio que quieres buscar: "))
        soc = ds.buscar(id)
        print("ID: ", soc.idSoci)
        print("DNI: ", soc.dni)
        print("Nombre: ", soc.nombre)
        print("Apellido: ", soc.apellido)
        print("-------------------------------------------")
    elif op == 5:
        ls = ds.todos()
        print('\nLista de personas:')
        for p in ls:
            print("ID: ", p.idSoci)
            print("DNI: ", p.dni)
            print("Nombre: ", p.nombre)
            print("Apellido: ", p.apellido)
            print("--------------------------------------------")
    else:
        print("\nHDP elegi una de esas opciones\n")
    opMenu()
