from src.windows import v_configuraciones
from src.model.configuracion import configuracion
from src.component import c_textos
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
            conf = configuracion(username, conf.textos , values["-CASILLAS-"], values["-COINCIDENCIAS-"], values["-TIEMPO-"], values["-ESTILO-"], values["-ELEMENTOS-"], values["-AYUDAS-"])
            conf.guardarJson()
            break
        if event == "-CONF_TXT-":
            window.hide()
            conf.textos = c_textos.start(conf)
            window.un_hide()
    return window