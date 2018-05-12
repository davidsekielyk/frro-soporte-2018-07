#Ejercicio 10

import pymysql
import json
import datetime

print("""Hacer un progama Python para acceder a la tabla Personas y PersonaPeso y
devuelve todos los registros la tabla en variable JSON , mostrar el resultado .""")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", password="password", db="soporte" )
cur = conn.cursor()

def TablaJson(k):
    for x in cur.fetchall():
        x = list(x)
        for i in x:
            if type(i) is datetime.date:
                x[k] = str(i)
        print(json.dumps(x))


print("JSON tabla personas:")
mostrar_personas = "select * from personas"
cur.execute(mostrar_personas)
TablaJson(2)

print("\nJSON tabla peso:")
mostrar_peso = "select * from personaPeso"
cur.execute(mostrar_peso)
TablaJson(1)

cur.close()
conn.close()
