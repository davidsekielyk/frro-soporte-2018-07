#Ejercicio 7

import pymysql
import datetime

print("""Hacer un Progrma Python donde pueda insertar registros en PersonaPeso y
que valide que la persona existe y que no existe de esa persona un registro de fecha
posterior al que queremos ingresar.""")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="password", db="soporte" )
cur = conn.cursor()

def InsertarPeso(id,fecha):
    peso = int(input("Ingrese el peso: "))

    nuevoPeso = "insert into personaPeso values('%d','%s','%d')"
    cur.execute(nuevoPeso%(id,fecha,peso))

    print("Se registro el peso %d del id:%d la fecha %s" %(peso,id,fecha))

def FechaM(id):
    fecha = input("Ingrese la fecha de cuando se peso en formato YYYY-MM-DD: ")
    anio, mes, dia = map(int, fecha.split("-"))
    fecha = datetime.date(anio,mes,dia)

    fechasPeso = "select fecha from personaPeso where idPersona = %d"
    cur.execute(fechasPeso%id)

    fechaMenor = False
    for x in cur.fetchall():
        if x[0] > fecha:
            fechaMenor = True

    if fechaMenor == True:
        print("Existen fechas mayores a la que queres ingresar")
    else:
        InsertarPeso(id,fecha)

def ExisteId():
    id = int(input("Ingrese id de la persona: "))

    idExistentes = "select idPersonas from personas"
    cur.execute(idExistentes)

    existe = False
    for x in cur.fetchall():
        if id == x[0]:
            existe = True

    if existe ==  False:
        print("El id de la persona que ingresaste NO EXISTE")
    else:
        FechaM(id)

ExisteId()

conn.commit()
cur.close()
conn.close()
