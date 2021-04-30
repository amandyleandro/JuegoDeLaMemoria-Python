from src.windows import v_menu
from src.component import c_configuraciones
from src.component import c_game
import PySimpleGUI as sg


def start():
    
    window = loop()
    window.close()

def loop():
    window = v_menu.build()

    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-SALIR-"):
            break
        
        if event == "-CONFIGURACIONES-":
            window.hide()
            c_configuraciones.start()
            window.un_hide()
        if event == "-JUGAR-":
            window.hide()
            c_game.start()
            window.un_hide()
    return window