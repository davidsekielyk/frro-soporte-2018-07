from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import sys

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'personas'
    idPersonas = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    fechaNacimiento = Column(Date)
    dni = Column(Integer)
    altura = Column(Integer)

engine = create_engine('sqlite:///test.db')
#engine = create_engine('mysql+pymysql://root:password@localhost/agencia_personal')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def creaTabla():
    Base.metadata.create_all(engine)

def alta():
    obPersona = Persona()
    print("Ingrese los datos de una nueva Persona:\n")

    obPersona.idPersonas = int(input("Id:"))

    obPersona.nombre = input("Nombre: ")

    fecha = input("Fecha de Nacimiento (formato YYYY-MM-DD): ")
    anio, mes, dia = map(int, fecha.split("-"))
    fecha = datetime.date(anio,mes,dia)
    obPersona.fechaNacimiento = fecha

    obPersona.dni = int(input("DNI: "))

    obPersona.altura = int(input("Altura: "))

    try:
        session.add(obPersona)
        print("Se ha registrado una nueva persona\n")
        session.commit()
    except:
        print("\nYa existe esa persona")
        e = sys.exc_info()[1]
        print("ERROR:", e.args[0])

def listar():
    lp = session.query(Persona).all() #--- lista
    print('\nLista de personas:')
    for p in lp:
        print("ID: ", p.idPersonas)
        print("Nombre: ", p.nombre)
        print("Fecha de Nacimiento: ", p.fechaNacimiento)
        print("DNI: ", p.dni)
        print("Altura: ", p.altura)
        print("--------------------------------------------")

def borrar():
    id = int(input("\nIngresa id de la persona que quieres eliminar: "))
    session.query(Persona).filter(Persona.idPersonas == id).delete()
    session.commit()
    print("Se ha eliminado la persona con id = %d \n"%id)


def opMenu():
    print("Ingrese una de las siguientes opciones")
    print("1-Alta")
    print("2-Listar")
    print("3-Baja")
    print("0-Terminar")
    global op
    b = True
    while b:
        try:
            op = int(input("Opcion: "))
            b = False
        except:
            print("Ingresa un numero (-.-) ")


creaTabla()
opMenu()
while op != 0:
    if op == 1 :
        alta()
    elif op == 2:
        listar()
    elif op == 3:
        borrar()
    else:
        print("\nHDP elegi una de esas cuatro opciones\n")
    opMenu()

