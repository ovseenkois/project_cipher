import PySimpleGUI as sg
import caesar
import visener
import vernam

def Make_Window():
    layout = [[sg.Button('Caesar cipher', expand_x=True, expand_y=True)],
              [sg.Button('Visener cipher', expand_x=True, expand_y=True)],
              [sg.Button('Vernam cipher', expand_x=True, expand_y=True)]]
    window = sg.Window('Menu', layout, size=(500, 600))
    return window

def Cipher():
    window = Make_Window()
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Caesar cipher':
            window.Hide()
            caesar.Cipher()
            window.UnHide()
        if event == 'Visener cipher':
            window.Hide()
            visener.Cipher()
            window.UnHide()
        if event == 'Vernam cipher':
            window.Hide()
            vernam.Cipher()
            window.UnHide()
    window.close()





