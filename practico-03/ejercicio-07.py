#Ejercicio 7

import pymysql

print("""Crear un tabla relacionada con Persona para guardar su peso corporal en una
fecha , PersonaPeso IdPersona Int() , Fecha Date() , Peso Int.""")
print("")

conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="password", db="soporte" )
cur = conn.cursor()

crearTablaPeso ="""
                    create table personaPeso
                    (
                        idPersona int, 
                        fecha date,
                        peso int,
                        primary key (idPersona, fecha),
                        index (idPersona),
                        foreign key (idPersona) references personas(idPersonas)
                    )

                """
cur.execute(crearTablaPeso)

conn.commit()
cur.close()
conn.close()
