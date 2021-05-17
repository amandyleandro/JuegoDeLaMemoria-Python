from src.windows import v_textos
from src.model.configuracion import configuracion
import PySimpleGUI as sg

def start(conf):
    window, text = loop(conf)
    window.close()
    return text
def loop(conf):
    window = v_textos.build(conf)
    texto = conf.textos
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED,"Exit", "-VOLVER-"):
            break
        if event == "-SELECT-":
            window.Element('-TXT_ACTUAL-').Update(value=conf.textos[values['-TEXTOS-']])
        if event == "-GUARDAR-":
            if not values["-INPUT_TXT-"]:
                error = "Debe ingresar un texto"
                sg.popup(error)
            else:
                texto[values["-TEXTOS-"]] = values["-INPUT_TXT-"]
                break
    return window, texto