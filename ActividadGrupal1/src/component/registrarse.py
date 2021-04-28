from src.windows import v_registrarse
from src.component import menu
import PySimpleGUI as sg


def start():
    window = loop()
    window.close()

def loop():
    window = v_registrarse.build()

    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break

        if event == "-REGISTRARSE-":
            menu.start()
            break
        

    return window