import PySimpleGUI as sg
from src.windows import Utilidades as u

def build():

    l_cont_form = [
        u.texts("Usuario",17),
        [sg.InputText('',font = ("Verdana"), size=(35,1),pad = ((0,0),(0,10)), key = "-USERNAME-" )],
        u.texts("Contraseña",17),
        [sg.InputText('',font = ("Verdana"), password_char = "*", size=(35,1),pad = ((0,0),(0,0)), key = "-PASSW-" )],
    ]

    l_cont = [
        u.texts("Inicio de Sesion",25,pad =((62,62),(20,16))),
        [sg.Column(l_cont_form, background_color="#536162",element_justification="l", pad=(0,0))],
        u.buttons('INICIAR SESION',17,"-INICIAR_SESION-",pad = ((0,0),(15,25))),
        u.texts("¿Sos nuevo?",15,pad = (0,10)),
        u.buttons('REGISTRARSE',17,"-REGISTRARSE-",pad = (0,9)),
        u.buttons('ENTRAR COMO INVITADO',0,"-ENTRAR_INVITADO-",pad = ((0,0),(0,20))),
    ]

    layout = [
        [sg.Text('MemPy', font=("Helvetica", 45), text_color="#f3f4ed",background_color="#424642",pad = ((0,0),(0,20)) )],
        [sg.Column(l_cont, background_color="#536162", element_justification="c", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color="#424642", element_justification="c", margins = (20,20))
