#Ejercicio 1

import pymysql

print("""Crear una base de datos con la tabla Persona con los datos de IdPesrona Int(), 
Nombre Char(30) , FechaNacimiento Date() , DNI Numeric(13) , Altura Int(). 
Hacer un progama Python para acceder a la tabla Personas e imprimir todos sus registros .""")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="password", db="soporte" )
cur = conn.cursor()

mostrar = "SELECT * FROM personas"
cur.execute(mostrar)

for x in cur.fetchall():
    print("ID: %d, Nombre: %s, Fecha Nacimiento: %s, DNI: %d, Altura: %d" %(x[0], x[1], x[2], x[3], x[4]))

cur.close()
conn.close()
