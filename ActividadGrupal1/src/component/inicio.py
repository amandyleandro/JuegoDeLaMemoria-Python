from src.windows import v_inicio
from src.component import menu
from src.component import registrarse
import PySimpleGUI as sg


def start():
    window = loop()
    window.close()

def loop():
    window = v_inicio.build()

    while True:
        event, _values = window.read()

        if event in (sg.WIN_CLOSED,"Exit"):
            break
        
        if event == "-INICIAR_SESION-" :
            window.hide()    ### no esconder cerrarse
            menu.start()
            window.un_hide()
            break

        if event == "-REGISTRARSE-" :
            window.hide()
            registrarse.start()
            window.un_hide()

        if event == "-ENTRAR_INVITADO-" :
            window.hide()   ### no esconder cerrarse
            menu.start()
            window.un_hide()
            break


    return window