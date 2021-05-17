import PySimpleGUI as sg
from ..windows import Utilidades as u

def build():
    layout = [u.buttons("Nivel 1",14,"-NIVEL_1-", pad =((10,10),(0,10)), size = (30,1)),
    u.buttons("Nivel 2",14,"-NIVEL_2-", pad =((10,10),(0,10)), size = (30,1)),
    u.buttons("Nivel 3",14,"-NIVEL_3-", pad =((10,10),(0,10)), size = (30,1)),
    u.buttons("VOLVER",14,"-VOLVER-", pad =((10,10),(0,10)), size = (30,1))]

    return sg.Window("MemPy",layout,background_color="#424642", element_justification="c", margins = (20,20))