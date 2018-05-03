#Ejercicio 4

import pymysql

print("""Hacer un progama Python para acceder a la tabla Personas y buscar el 
registro de una persona identificada por su DNI , mostrar los datos de la persona.""")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="password", db="soporte" )
cur = conn.cursor()

buscar = "select * from personas where dni=39721462"
cur.execute(buscar)

for x in cur.fetchall():
    print("ID: %d, Nombre: %s, Fecha Nacimiento: %s, DNI: %d, Altura: %d" %(x[0], x[1], x[2], x[3], x[4]))

cur.close()
conn.close()
