import PySimpleGUI as sg

fuente = "verdana"
texto_color = "#f3f4ed"
fondo_color = "#536162"
boton_color = ("#f3f4ed", "#c06014")

def texts(*args, pad = (0,0)):
    return [sg.Text(args[0], font=(fuente, args[1]), text_color=texto_color, background_color=fondo_color, pad = pad)]

def buttons(*args, key ="", pad = (0,0), size = (0,0)):
    return [sg.Button(args[0], font = (fuente, args[1]), key = args[2], border_width = 1, button_color =boton_color, pad = pad, size = size)]
