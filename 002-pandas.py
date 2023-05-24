#  Copyright (c) 2023. José Manuel Abelleira López.
#
import getch as kb
import pandas as pd
import os

personas = pd.read_excel('personas2.xlsx')

print(40*"* ")
print("Tabla original de datos")
print(40*"* ")
print("")

print(personas)

print(40*"* ")
print("Salarios agrupados por estudios y género, ordenados por fecha de nacimiento de más viejos a más jóvenes")
print(40*"* ")
print("")

print(personas.groupby(['ESTUDIOS', 'GÉNERO', 'NOMBRE', 'SALARIO ANUAL']).mean().sort_values(['ESTUDIOS', 'FECHA NACIMIENTO'], ascending=False))

kb.pause(40*"* ")
os.system('clear')
