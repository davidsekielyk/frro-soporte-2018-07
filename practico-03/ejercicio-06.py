#Ejercicio 6

import pymysql
import json
import datetime

print("""Hacer un progama Python para acceder a la tabla Personas y devuelve todos
los registros la tabla en variable JSON, mostrar el resultado.""")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="password", db="soporte")
cur = conn.cursor()

mostrar = "select * from personas"
cur.execute(mostrar)

#Forma Chispa
for x in cur.fetchall():
    nueva_tupla = []
    for i in x:
        if type(i) == type(x[2]):
            nueva_tupla.append(str(i))
        else:
            nueva_tupla.append(i)
    to_json = json.dumps(nueva_tupla)
    print(to_json)

#Forma David
for x in cur.fetchall():
    x = list(x)
    for i in x:
        if type(i) is datetime.date:
            x[2] = str(i)
    print(json.dumps(x))


cur.close()
conn.close()



