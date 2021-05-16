def disney(datos, params):
    all = list(filter(lambda x: x['genre'] in params, datos))[:50]
    return list(map(lambda x: x['movie_title'], all))

criterios = {
    'lunes': 
    {
        "mañana":
        {
            'criterio': 'Peliculas de genero musical de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ('Comedy')
        },
        "tarde":
        {
            'criterio': 'Peliculas de genero Drama de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ('Action', 'Musical')
        },
    },

    'martes': {"mañana": {}, "tarde": {}},

    'miercoles': {"mañana": {}, "tarde": {}},

    'jueves': {"mañana": {}, "tarde": {}},

    'viernes': {"mañana": {}, "tarde": {}},

    'sabado':
    {
        "mañana":
        {
            'criterio': 'Peliculas de genero musical de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ('Adventure')
        },
        "tarde":
        {
            'criterio': 'Peliculas de genero Drama de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ('Drama')
        },
    },

    'domingo': {"mañana": {}, "tarde": {}},
}


import datetime
from tkinter.constants import N

nro_dia = datetime.datetime.today().weekday()
hs = datetime.datetime.now().hour

nro_dia = 0
hs = 13
semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
dia = semana[nro_dia]
turno = "mañana" if hs <= 12 else "tarde"

import csv
import os
import os.path
from collections import Counter

def abrirArchivo(arch):
    dir_carp = "Archivos\\data_csv"                                         ##### ?
    carpeta = os.path.join(os.getcwd(), dir_carp)
    archivo = open(os.path.join(carpeta, arch + ".csv"))

    with open(os.path.join(carpeta, arch + ".csv")) as archivo:
        datos = []
        for i in csv.DictReader(archivo):
            datos.append(dict(i))
    return datos


def setearCriterios():
    aux = criterios[dia][turno]
    datos= abrirArchivo(aux['archivo'])
    return aux['funcion'](datos,aux['params'])


for i in setearCriterios():
    print(i)