#Ejercicio 2

import pymysql

print("Hacer un progama Python para acceder a la tabla Personas e insertar en la tabla un registro de una persona.")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="password", db="soporte")
cur = conn.cursor()

insertar= "insert into personas values(113, 'Ramiro', '1983-02-10', 39628102, 184);"
cur.execute(insertar)

mostrar = "select * from personas"
cur.execute(mostrar)

for x in cur.fetchall():
    print("ID: %d, Nombre: %s, Fecha Nacimiento: %s, DNI: %d, Altura: %d" %(x[0], x[1], x[2], x[3], x[4]))

conn.commit()
cur.close()
conn.close()
