import PySimpleGUI as sg
from src.windows import Utilidades as u

def build(configuracion):

    frame_1 = [[sg.Text(configuracion.textos["Comienzo"], key="-TXT_ACTUAL-" , s=(25,5))]]
    #col_1 = [sg.Frame("Texto actual", frame_1)]
    
    frame_2 = [[sg.Combo(["Comienzo","Gano","Perdio","Quedan 30 segundos"], default_value = "Comienzo", font = ("Verdana"), key = '-TEXTOS-')],
        [sg.Button("Seleccionar", key="-SELECT-")]]
    #col_2 = [sg.Frame("Tipos de textos", frame_1)]
    
    col_3 = [[sg.InputText(font = "Verdana", key='-INPUT_TXT-', s=(25,20), focus=True)]]
    layout = [[sg.Column(frame_1), sg.Column(frame_2), sg.Column(col_3)],
    [sg.Button('GUARDAR', key="-GUARDAR-")]]


    return sg.Window("Textos", layout, background_color="#424642", margins = (20,20))