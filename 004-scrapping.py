#  Copyright (c) 2023. José Manuel Abelleira López.
#


import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import wget
import os
import tkinter as tk
from tkinter import ttk, font


def obtener_temp():

    # Borrar el archivo xml local si existe
    if os.path.exists('datos_xml.xml'):
        os.remove('datos_xml.xml')

    url_xml = 'https://www.aemet.es/xml/municipios/localidad_15045.xml'

    # Descargar el archivo xml de la página
    wget.download(url_xml, 'datos_xml.xml')

    # Parsear el archivo
    root = ET.parse('datos_xml.xml')

    # abrir el nodo XML
    root_nodo = root.getroot()

    # Crear un diccionario para guardar los datos
    datos = {}

    # Buscar la provincia por su tag
    for nombre_nodo in root_nodo.iter('provincia'):
        datos['Provincia: '] = nombre_nodo.text

    # Buscar el nombre por su tag
    for nombre_nodo in root_nodo.iter('nombre'):
        datos['Nombre: '] = nombre_nodo.text

    # Buscar los hijos del nodo predicción, hijo del root_nodo

    dias = root_nodo.findall('prediccion/dia')

    # Obtener los datos del primer día
    for dia in range(1):
        datos[dia + 1] = {}
        datos[dia + 1]['fecha'] = dias[dia].attrib['fecha']
        datos[dia + 1]['Temperatura maxima'] = dias[dia].find('temperatura/maxima').text
        datos[dia + 1]['Temperatura minima'] = dias[dia].find('temperatura/minima').text

    solicitado = {}
    solicitado['Provincia: '] = datos['Provincia: ']
    solicitado['Nombre: '] = datos['Nombre: ']
    solicitado['Temperatura maxima: '] = datos[1]['Temperatura maxima']
    solicitado['Temperatura minima: '] = datos[1]['Temperatura minima']
    return solicitado


root = tk.Tk()
root.geometry('320x200')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Calcular x e y para centrar la ventana
root.update()
posx = (root.winfo_screenwidth()-320) // 2
posy = (root.winfo_screenheight()-200) // 2

root.geometry(f'+{posx}+{posy}')


datos = obtener_temp()

marc_temp = ttk.LabelFrame(root, text=datos['Nombre: '])
marc_temp.grid(row=0, column=0, padx=10, pady=0, sticky='nsew')
marc_temp.columnconfigure(0, weight=1)
marc_temp.columnconfigure(1, weight=2)


et_max = ttk.Label(marc_temp, text='Temperatura maxima:', justify='left', anchor='w', font='bold')
et_max.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
text_max = ttk.Label(marc_temp, text=datos['Temperatura maxima: '] + 'ºC', justify='right', anchor='e', font='bold')
text_max.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

et_min = ttk.Label(marc_temp, text='Temperatura mínima:', justify='left', anchor='w', font='bold')
et_min.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
text_min = ttk.Label(marc_temp, text=datos['Temperatura minima: '] + 'ºC', justify='right', anchor='e', font='bold')
text_min.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

root.mainloop()
