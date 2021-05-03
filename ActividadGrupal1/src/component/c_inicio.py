from src.windows import v_inicio
from src.component import c_menu
from src.component import c_registro
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
            c_menu.start()
            window.un_hide()
            break

        if event == "-REGISTRARSE-" :
            window.hide()
            c_registro.start()
            window.un_hide()

        if event == "-ENTRAR_INVITADO-" :
            window.hide()   ### no esconder cerrarse
            c_menu.start()
            window.un_hide()
            break


    return window