from tkinter.constants import CENTER
import PySimpleGUI as sg
from src.windows import Utilidades as u

def build(conf):

    frame_1 = [[sg.Text(conf.textos["Comienzo"], key="-TXT_ACTUAL-", background_color="#536162", font=("verdana", 12), s=(15,4))]]
    col_1 = [[sg.Frame("Texto actual", frame_1, font=("Verdana",11), background_color="#536162" )]]
    
    frame_2 = [[sg.Combo(["Comienzo","Gano","Perdio","Quedan 30 segundos"], default_value = "Comienzo", font=("Verdana"), key = '-TEXTOS-')],
        u.buttons("SELECCIONAR",12,"-SELECT-", pad =((10,10),(0,10)), size = (12,1))]
    col_2 = [[sg.Frame("Tipos de textos", frame_2, background_color="#536162", font=("Verdana",11), element_justification= 'center')]]
    
    frame_3 = [[sg.InputText(key='-INPUT_TXT-', font=("Verdana",12), s=(15,1), focus=True)]]
    col_3 = [[sg.Frame("Nuevo texto", frame_3, font=("Verdana",11), background_color="#536162")]]

    l_cont = [[sg.Column(col_1,background_color="#536162"), sg.Column(col_2,background_color="#536162"), sg.Column(col_3,background_color="#536162")],
    u.buttons("GUARDAR",12,"-GUARDAR-", pad =((10,10),(0,10)), size = (15,1)) +
    u.buttons("VOLVER",12,"-VOLVER-",pad =((10,10),(0,10)),size = (15,1))]
    layout = [
    [sg.Text("MemPy", font=("Helvetica", 25), text_color="#f3f4ed",background_color="#424642",pad = ((0,0),(0,20)) )],
    [sg.Column(l_cont, background_color="#536162", element_justification="c", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color="#424642", element_justification="c", margins = (20,20))
