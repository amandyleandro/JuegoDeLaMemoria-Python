from src.windows import v_game
import time
import PySimpleGUI as sg 

def time_as_int():
    return int(round(time.time()*100))

def start():
    window = loop()
    window.close()

def loop():
    player = {"name":"Maria"}
    cant_btn = 8
    cant_ayudas = 5
    total_ayudas = cant_ayudas

    board_data = [[" "] * cant_btn for _i in range(cant_btn) ]
    window = v_game.build(player, board_data,cant_btn,cant_ayudas,total_ayudas)
    current_time = 0
    start_time = time_as_int()

    while True:
        event, _values = window.read(timeout=10)
        current_time = time_as_int() - start_time
        if event in (sg.WINDOW_CLOSED, "-SALIR-"):
            break
        if event == "-AYUDA-" or event == sg.WIN_CLOSED:
            if cant_ayudas != 0:
                cant_ayudas = cant_ayudas - 1
                #funcion Ayudar
                window["-X-"].Update("{} / {}".format(cant_ayudas,total_ayudas))

        window['-TIMER-'].Update('{:02d}:{:02d}'.format((current_time // 100) // 60,(current_time // 100) % 60))                                                          
    return window