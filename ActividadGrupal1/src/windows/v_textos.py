from tkinter.constants import CENTER
import PySimpleGUI as sg
from src.windows import Utilidades as u

def build(conf):

    frame_1 = [[sg.Text(conf.textos["Comienzo"], key="-TXT_ACTUAL-", background_color="#536162" , s=(15,4))]]
    col_1 = [[sg.Frame("Texto actual",frame_1, background_color="#536162" )]]
    
    frame_2 = [[sg.Combo(["Comienzo","Gano","Perdio","Quedan 30 segundos"], default_value = "Comienzo", font = ("Verdana",10), key = '-TEXTOS-')],
        [sg.Button("Seleccionar", key="-SELECT-")]]
    col_2 = [[sg.Frame("Tipos de textos", frame_2, background_color="#536162", element_justification= 'center')]]
    
    frame_3 = [[sg.InputText(font = "Verdana", key='-INPUT_TXT-', s=(15,1), focus=True)]]
    col_3 = [[sg.Frame("Nuevo texto", frame_3, background_color="#536162")]]

    l_cont = [[sg.Column(col_1,background_color="#536162"), sg.Column(col_2,background_color="#536162"), sg.Column(col_3,background_color="#536162")],
    [sg.Button('Guardar', key="-GUARDAR-")]]

    layout = [
    [sg.Text("MemPy", font=("Helvetica", 25), text_color="#f3f4ed",background_color="#424642",pad = ((0,0),(0,20)) )],
    [sg.Column(l_cont, background_color="#536162", element_justification="c", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color="#424642", element_justification="c", margins = (20,20))
