import PySimpleGUI as sg

def build(user, board_data,cant_btn,cant_ayudas,total_ayudas):

    fuente = "verdana"
    texto_color = "#f3f4ed"
    fondo_color = "#536162"
    boton_color = ("#f3f4ed", "#c06014")
    fondo_fondo = "#424642"

    pares = int(cant_btn * cant_btn / 2)

    tam_bt = ()
    tam_info = ()
    if cant_btn == 6:
        tam_bt = (12,6)
        tam_info = (350,635)
    elif cant_btn == 8: 
        tam_bt = (10,5)
        tam_info = (350,720)
    elif cant_btn == 10: 
        tam_bt = (8,4)
        tam_info = (350,740)


    l_tablero = []
    for y in range(cant_btn):
        l_tablero += [
            [
                sg.Button(board_data[x][y],border_width = 1, pad=(0,0), size=tam_bt, key=f"cell-{x}-{y}")
                for x in range(cant_btn)
            ]
        ]

    l_info = [
        [sg.Text("Tiempo", font=(fuente, 25), text_color=texto_color, background_color=fondo_color,pad = ((0,0),(30,0)),)],
        [sg.Text("00:00", font=(fuente, 38), text_color=texto_color,pad = ((0,0),(0,40)), background_color= fondo_color, key='-TIMER-',),
        sg.Text(" / ", font=(fuente, 30), text_color=texto_color, background_color=fondo_color,pad = ((0,0),(0,25)),),
        sg.Text("Maximo \n 05:00", font=(fuente, 15), text_color=texto_color, background_color= fondo_color,pad = ((0,0),(0,25)))],
        [sg.Text(f"{user.username} ({user.puntos} Pts)", font=(fuente, 20), text_color=texto_color, background_color= fondo_color,pad = ((0,0),(0,20)) )],
        [sg.Text("Pts: 0", font=(fuente, 17), text_color=texto_color, background_color= fondo_color)],
        [sg.Text(f"Pares encontrados: 0/{pares}", font=(fuente, 17), text_color=texto_color, background_color= fondo_color)],
        [sg.Text("Dificultad: " + str(cant_btn) + "X" + str(cant_btn), font=(fuente, 17), text_color=texto_color, background_color= fondo_color)],
        [sg.Button("AYUDAS ", font = (fuente, 13), border_width = 1, button_color = boton_color, key = "-AYUDA-", pad = ((10,10),(10,160)))]+
        [sg.Text( str(cant_ayudas) +" / " + str(total_ayudas), font=(fuente, 17), text_color=texto_color, background_color= fondo_color,pad = ((10,10),(10,160)), key =("-X-"))],
        [sg.Button("SALIR", font = (fuente, 15), border_width = 1, button_color = boton_color, key = "-SALIR-", pad = ((6,0),(10,10)), size= (25,1))],
    ]

    layout = [
        [sg.Column(l_tablero, background_color= fondo_color, element_justification="c", pad=((5,10),(5,5)))] +
        [sg.Column(l_info, background_color= fondo_color,element_justification="c", size = tam_info, pad=((10,5),(5,5)))]
    ]

    board = sg.Window("MemPy", layout,background_color=fondo_fondo, element_justification="c", margins = (2,2),)
    return board
