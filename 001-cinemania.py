#  Copyright (c) 2023. José Manuel Abelleira López.
#
#  Copyright (c) 2023. José Manuel Abelleira López.
# Base de datos de Cinemanía usando mysqlconnector desde python
#
# a) Lista los críticos que hayan puntuado una película (la que quieras) con menos de 7 puntos.
# b) Lista las 10 películas que tengan mejor promedio de puntuación del año xxxx (el que quieras)
import os
import platform
import mysql.connector as con
sistema = platform.system()
if sistema == "Windows":
    import msvcrt as kb
else:
    import getch as kb

print(40*"* ")
print("Lista los críticos que hayan puntuado una película (la que quieras)\ncon menos de 7 puntos")
print(40*"* ")
print("")

try:
    with con.connect(
            host='localhost',
            user='pepe',
            password='8116',
            database='cinemania'
    ) as conexion:
        with conexion.cursor() as sql:
            sql.execute(f"SELECT nombre, primer_apellido, COUNT(peliculas_actores.id_actor) "
                        f"FROM peliculas_actores "
                        f"INNER JOIN actores_atrices "
                        f"ON peliculas_actores.id_actor = actores_atrices.id_actor "
                        f"GROUP BY peliculas_actores.id_actor "
                        f"ORDER BY COUNT(peliculas_actores.id_actor) DESC")
            listactores = list(sql.fetchall())
            for actor in listactores:
                print(f'{actor[0]} {actor[1]} - {actor[2]}')
except con.Error as err:
    print(err)
    print("Error de conexión")

kb.pause(40*"* ")
os.system('clear')

