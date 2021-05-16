def disney(datos, params):
    all = list(filter(lambda x: x['genre'] in params, datos))[:50]
    return list(map(lambda x: x['movie_title'], all))

def disneyAño(datos, params):
    all = list(filter(lambda x: params[0] < obtenerAño(x['release_date']) <= params[1] , datos))[:50]
    return list(map(lambda x: x['movie_title'], all))

def obtenerAño(año):
    l = año.split('-')
    return int(l[0])

criterios = {
    'lunes': 
    {
        "mañana":
        {
            'criterio': 'Peliculas de genero comedia de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ('Comedy')
        },
        "tarde":
        {
            'criterio': 'Peliculas de genero acción y musical de disney',
            'funcion': disney,
            'archivo' : 'disney_movies_total_gross',
            'params': ('Action', 'Musical')
        },
    },

    'martes': 
    {
        "mañana":
        {
            'criterio': 'Peliculas de disney entre los años 1940 y 1950',
            'funcion': disneyAño,
            'archivo' : 'disney_movies_total_gross',
            'params': (1940,1950)
        },
        "tarde":
        {
            'criterio': 'Peliculas de disney entre los años 1950 y 1960',
            'funcion': disneyAño,
            'archivo' : 'disney_movies_total_gross',
            'params': (1950,1960)
        },
    },

    'miercoles': 
    {
        "mañana":
        {
            'criterio': 'Peliculas de disney entre los años 1960 y 1970',
            'funcion': disneyAño,
            'archivo' : 'disney_movies_total_gross',
            'params': (1960,1970)
        },
        "tarde":
        {
            'criterio': 'Peliculas de disney entre los años 1970 y 1980',
            'funcion': disneyAño,
            'archivo' : 'disney_movies_total_gross',
            'params': (1970,1980)
        },
    },

    'jueves':
    {
        "mañana":
        {
            'criterio': 'Peliculas de disney entre los años 1980 y 1990',
            'funcion': disneyAño,
            'archivo' : 'disney_movies_total_gross',
            'params': (1980,1990)
        },
        "tarde":
        {
            'criterio': 'Peliculas de disney entre los años 1990 y 2000',
            'funcion': disneyAño,
            'archivo' : 'disney_movies_total_gross',
            'params': (1990,2000)
        },
    },

    'viernes': 
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

    'domingo': 
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
}


import datetime
from tkinter.constants import N

nro_dia = datetime.datetime.today().weekday()
hs = datetime.datetime.now().hour

nro_dia = 3
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