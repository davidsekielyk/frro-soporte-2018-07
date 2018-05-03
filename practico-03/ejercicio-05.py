#Ejercicio 5

import pymysql

print("""Hacer un progama Python para acceder a la tabla Personas y actualiza los 
datos de una persona identificada, mostrar los datos de la persona.""")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="password", db="soporte" )
cur = conn.cursor()

actualizar = "update personas set  altura = 190 where dni=39721462"
cur.execute(actualizar)

mostrar = "select * from personas where dni=39721462"
cur.execute(mostrar)

for x in cur.fetchall():
    print("ID: %d, Nombre: %s, Fecha Nacimiento: %s, DNI: %d, Altura: %d" %(x[0], x[1], x[2], x[3], x[4]))


conn.commit()
cur.close()
conn.close()
