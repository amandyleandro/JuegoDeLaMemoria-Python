import PySimpleGUI as sg
from ..windows import Utilidades as u


def build(configuracion):
    
    pad_t = ((0,0),(0,15))
    pad_i = ((10,0),(0,15))

    l_cont_form = [
    u.texts("Textos",17, pad = pad_t),
    u.texts("Tiempo maximo",17, pad = pad_t) + [sg.Spin([i for i in range(120,300)], initial_value= configuracion.tiempo, font = ("Verdana"), size = (3,1), key = "-TIEMPO-",pad = pad_i )],
    u.texts("Cantidad de casillas",17, pad = pad_t) + [sg.Combo(["8x8", "10x10", "12x12"],default_value = configuracion.cant_casillas,font = ("Verdana"),key = "-CASILLAS-", pad = pad_i )],
    u.texts("Cantidad de coincidencias",17, pad = pad_t) + [sg.Spin([i for i in range(1,4)], initial_value= configuracion.coicidencias, font = ("Verdana"), size = (3,1),key = "-COINCIDENCIAS-", pad = pad_i )],
    u.texts("Tipo de casillas",17, pad = pad_t) + [sg.Combo(["Palabras", "Imagenes", "Ambas"],default_value = configuracion.tipo_elementos,font = ("Verdana"),key = "-ELEMENTOS-", pad = pad_i )],
    u.texts("Estilos",17, pad = pad_t) + [sg.Combo(["t1", "t2", "t3", "t4", "t5"],default_value = configuracion.estilo,font = ("Verdana"), size = (15,1),key = "-ESTILO-", pad = pad_i )],
    u.texts("Ayudas",17, pad = pad_t) + [sg.Combo(["Si", "No"] , default_value= configuracion.ayudas, font = ("Verdana"), size = (3,1),key = "-AYUDAS-", pad = pad_i )],
    ]

    l_cont = [
    u.texts("Configuraciones",25,pad = ((0,0),(20,16))),
    [sg.Column(l_cont_form, background_color="#536162", element_justification="l",pad = pad_t)],
    u.buttons("GUARDAR",14,"-GUARDAR-", pad =((10,10),(0,10)), size = (30,1)),
    u.buttons("VOLVER",13,"-VOLVER-",pad =((10,20),(0,10)),size = (15,1)) + u.buttons("RESTABLECER",13,"-RESTABLECER-",pad =((0,10),(0,10)),size = (15,1)),
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