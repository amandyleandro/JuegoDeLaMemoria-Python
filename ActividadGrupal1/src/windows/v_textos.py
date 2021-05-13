import PySimpleGUI as sg
from src.windows import Utilidades as u

def build(configuracion):

    col_1 = [sg.Text(configuracion.textos["Comienzo"], s=(25,5))]
    col_2 = [[sg.Text("Textos")],
        [sg.Combo(["Comienzo","Gano","Perdio","Quedan 30 segundos"], default_value = "Comienzo", font = ("Verdana"), key = '-TEXTOS-')]]
    col_3 = [sg.InputText(font = "Verdana", key='-INPUT_TXT-', s=(25,5))]
    layout = [[col_1, col_2, col_3],
    [sg.Button('GUARDAR', key="-GUARDAR-")]]


    return sg.Window("Textos", layout, background_color="#424642", margins = (20,20))