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
    board_data = [[" "] * 8 for _i in range(8) ]
    window = v_game.build(player, board_data)
    current_time = 0
    start_time = time_as_int()

    while True:
        event, _values = window.read(timeout=10)
        current_time = time_as_int() - start_time
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break
        window['-TIMER-'].Update('{:02d}:{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60))                                                          
    return window