from src.windows import v_configuraciones
import json
import PySimpleGUI as sg


def start():
    window = loop()
    window.close()

def loop():

    configuraciones = {"textos":[],
    "tiempo maximo": 120, 
    "casillas": "8x8", 
    "coincidencias": 2, 
    "tipo de casillas": "Ambas", 
    "ayuda": "No", 
    "paleta de colores": "Predeterminado"}
    window = v_configuraciones.build(configuraciones)
    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break
        
    return window