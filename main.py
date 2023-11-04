import PySimpleGUI as sg
import menu
import caesar
import visener

sg.theme('Black')

menu_window = sg.Window('Menu', menu.layout, size=(250, 250))

while True:
    menu_event, menu_value = menu_window.read()
    if menu_event == sg.WIN_CLOSED:
        break
    if menu_event == 'Caesar cipher':
        menu_window.Hide()
        caesar.cipher()
        menu_window.UnHide()
    if menu_event == 'Visener cipher':
        menu_window.Hide()
        visener.cipher()
        menu_window.UnHide()
    # if menu_event == 'Vernam cipher':

menu_window.close()



