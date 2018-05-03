#Ejercicio 3

import pymysql

print("Hacer un progama Python para acceder a la tabla Personas e eliminar un registro de una persona")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="password", db="soporte" )
cur = conn.cursor()

eliminar = "delete from personas where idPersonas=113"
cur.execute(eliminar)

mostrar = "select * from personas"
cur.execute(mostrar)

for x in cur.fetchall():
    print("ID: %d, Nombre: %s, Fecha Nacimiento: %s, DNI: %d, Altura: %d" %(x[0], x[1], x[2], x[3], x[4]))

conn.commit()
cur.close()
conn.close()
