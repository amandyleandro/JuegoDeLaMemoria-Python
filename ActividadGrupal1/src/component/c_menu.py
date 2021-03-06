from src.windows import v_menu
from src.component import c_configuraciones
from src.component import c_niveles
import PySimpleGUI as sg


def start(user):
    window = loop(user)
    window.close()

def loop(user):
    window = v_menu.build()

    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-SALIR-"):
            break
        
        if event == "-CONFIGURACIONES-":
            window.hide()
            c_configuraciones.start(user)
            window.un_hide()
        if event == "-JUGAR-":
            window.hide()
            c_niveles.start(user)
            window.un_hide()
    return window