from src.windows import v_niveles
from src.component import c_game
import PySimpleGUI as sg

def start(user):
    window = loop(user)
    window.close()

def loop(user):
    window = v_niveles.build()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break
        if event == "-NIVEL_1-":
            window.hide()
            c_game.start(user, "Nivel 1")
            window.un_hide()
        if event == "-NIVEL_2-":
            window.hide()
            c_game.start(user, "Nivel 2")
            window.un_hide()
        if event == "-NIVEL_3-":
            window.hide()
            c_game.start(user, "Nivel 3")
            window.un_hide()
    return window