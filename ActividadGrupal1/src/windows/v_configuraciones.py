import PySimpleGUI as sg
from ..windows import Utilidades as u


def build(configuracion):
    
    pad_t = ((10,0),(0,15))
    pad_i = ((10,0),(0,15))

    l_cont_form = [
    u.texts("Textos",15, pad = pad_t) + u.buttons("CONFIGURAR TEXTOS",11,"-CONF_TXT-", pad =((50,10),(0,10)), size = (25,1)),
    u.texts("Tiempo maximo",15, pad = pad_t) + [sg.Spin([i for i in range(120,300)], initial_value= configuracion["tiempo"], font = ("Verdana"), size = (3,1), key = "-TIEMPO-",pad = pad_i )],
    u.texts("Dimensión del nivel 1",15, pad = pad_t) + [sg.Combo(["4x4", "6x6"],default_value = configuracion["cant_casillas"]["Nivel 1"],font = ("Verdana"),key = "-CASILLAS_1-", pad = pad_i )],
    u.texts("Dimensión del nivel 2",15, pad = pad_t) + [sg.Combo(["8x8", "10x10"],default_value = configuracion ["cant_casillas"]["Nivel 2"],font = ("Verdana"),key = "-CASILLAS_2-", pad = pad_i )],
    u.texts("Dimensión del nivel 3",15, pad = pad_t) + [sg.Combo(["12x12", "14x14"],default_value = configuracion["cant_casillas"]["Nivel 3"],font = ("Verdana"),key = "-CASILLAS_3-", pad = pad_i )],
    u.texts("Cantidad de coincidencias",15, pad = pad_t) + [sg.Spin([i for i in range(1,4)], initial_value= configuracion["coincidencias"], font = ("Verdana"), size = (3,1),key = "-COINCIDENCIAS-", pad = pad_i )],
    u.texts("Tipo de casillas",15, pad = pad_t) + [sg.Combo(["Palabras", "Imagenes", "Ambas"],default_value = configuracion["tipo_elementos"],font = ("Verdana"),key = "-ELEMENTOS-", pad = pad_i )],
    u.texts("Estilos",15, pad = pad_t) + [sg.Combo(["t1", "t2", "t3", "t4", "t5"],default_value = configuracion["estilo"],font = ("Verdana"), size = (15,1),key = "-ESTILO-", pad = pad_i )],
    u.texts("Ayudas",15, pad = pad_t) + [sg.Combo(["Si", "No"] , default_value= configuracion["ayudas"], font = ("Verdana"), size = (3,1),key = "-AYUDAS-", pad = pad_i )],
    ]

    l_cont = [
    u.texts("Configuraciones",25,pad = ((0,0),(20,16))),
    [sg.Column(l_cont_form, background_color="#536162", element_justification="l",pad = pad_t)],
    u.buttons("GUARDAR",14,"-GUARDAR-", pad =((10,10),(0,10)), size = (30,1)),
    u.buttons("VOLVER",13,"-VOLVER-",pad =((10,10),(0,10)),size = (30,1)), #+ u.buttons("RESTABLECER",13,"-RESTABLECER-",pad =((0,10),(0,10)),size = (15,1)),
    ]

    layout = [
    [sg.Text("MemPy", font=("Helvetica", 45), text_color="#f3f4ed",background_color="#424642",pad = ((0,0),(0,20)) )],
    [sg.Column(l_cont, background_color="#536162", element_justification="c", pad=(0,0))]
    ]

    return sg.Window("MemPy", layout,background_color="#424642", element_justification="c", margins = (20,20))

"""window = build()
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()"""