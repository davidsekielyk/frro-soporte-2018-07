#Ejercicio 9

import pymysql
import sys

print("""Hacer un progama Python para acceder a la tabla Personas y PersonaPeso y
buscar el registro de una persona identificada por su DNI , mostrar los datos de la
persona y de su historial de peso .""")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="password", db="soporte" )
cur = conn.cursor()

dni = int(input("Ingrese el DNI de la persona: "))
sql = ("select idPersonas from personas where dni = %d")
cur.execute(sql%dni)
persona = cur.fetchone()
id = persona[0]

sqlPersona = ("select * from personas where idPersonas = %d"%id)
sqlPeso = ("select * from personaPeso where idPersona = %d"%id)

print("Datos de la persona: ")
cur.execute(sqlPersona)
for x in cur.fetchall():
    print("  Nombre: ",x[1])
    print("  Fecha de nacimiento:", str(x[2]))
    print("  DNI:",x[3])
    print("  Altura:",x[4])

print("\nHistorial de peso: ")
cur.execute(sqlPeso)
for x in cur.fetchall():
    print("Fecha: ",x[1],"----- Peso: ",x[2])

cur.close()
conn.close()
