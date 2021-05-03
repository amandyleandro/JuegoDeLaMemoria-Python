from ..windows import v_registro
#from ..component import c_menu
from ..model.usuario import usuario
import PySimpleGUI as sg


def start():
    window = loop()
    window.close()

def loop():
    window = v_registro.build()

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break

        if event == "-REGISTRARSE-":
            # if not event == "-USERNAME-" or not event == "-PASSW-" or not event == "-GENERO-" or not event == "-EDAD-" or not event == "-REP_PSSW-":
            #     print("No se rellenaron todos los valores pedidos") 
            #     sg.popup(error)
            user = usuario(values["-USERNAME-"].strip(),values["-PASSW-"],values["-GENERO-"],values["-EDAD-"]) #creo el usuario con la clase
            rep_contra = values["-REP_PASSW-"]
            error = user.validarRegister(rep_contra)
            if error == "": 
                user.guardarUsuarioJson()
                break
            else:
                sg.popup(error)

    return window
