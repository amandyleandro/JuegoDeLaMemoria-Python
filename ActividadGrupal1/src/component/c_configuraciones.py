from src.windows import v_configuraciones
from src.model.configuracion import configuracion
import json
import PySimpleGUI as sg


def start(username):
    window = loop(username)
    window.close()

def loop(username):
    conf = configuracion(username)
    window = v_configuraciones.build(conf.buscarConfig())
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break
        if event == "-GUARDAR-":
            conf = configuracion(username, "", values["-CASILLAS-"], values["-COINCIDENCIAS-"], values["-TIEMPO-"], values["-ESTILO-"], values["-ELEMENTOS-"], values["-AYUDAS-"])
            conf.guardarJson()
            break
    return window