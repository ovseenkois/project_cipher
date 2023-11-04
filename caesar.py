import PySimpleGUI as sg
import alphabets

def Encode(string, shift, language):
    shift = int(shift)
    if language == 'rus':
        alphabet = alphabets.rus_alphabet
    else:
        alphabet = alphabets.eng_alphabet
    new_string = []
    len_alphabet = len(alphabet)
    for i in string:
        if i in alphabet.upper():
            new_string.append(alphabet.upper()[(alphabet.upper().index(i) + shift) % len_alphabet])
        elif i in alphabet:
            new_string.append(alphabet[(alphabet.index(i) + shift) % len_alphabet])
        else:
            new_string.append(i)
    return ''.join(new_string)

def Decode(string, shift, language):
    shift = int(shift)
    if language == 'rus':
        alphabet = alphabets.rus_alphabet
    else:
        alphabet = alphabets.eng_alphabet
    new_string = []
    len_alphabet = len(alphabet)
    for i in string:
        if i in alphabet.upper():
            new_string.append(alphabet.upper()[(alphabet.upper().index(i) - shift) % len_alphabet])
        elif i in alphabet:
            new_string.append(alphabet[(alphabet.index(i) - shift) % len_alphabet])
        else:
            new_string.append(i)
    return ''.join(new_string)


def make_window():
    list_shifts = ['decode without shift']
    list_shifts.extend([str(i) for i in range(1, 40)])
    layout = [[sg.Button('Back')],
              [sg.Text('Text to encode:')],
              [sg.Multiline(size=(50, 10), expand_x=True, key='input')],
              [sg.Text('Alphabet'), sg.Text('Type of operation'), sg.Text('Shift')],
              [sg.Combo(['rus', 'eng'], default_value='rus', readonly=True, key='language'),
               sg.Combo(['encode', 'decode'], default_value='encode', readonly=True, key='type of action'),
               sg.Combo(list_shifts, default_value='3', readonly=True, key='shift')],
              [sg.Button('Apply', expand_x=True)],
              [sg.Text('Result:')],
              [sg.Multiline(size=(50, 10), expand_x=True, key='output')]]
    window = sg.Window('Caesar cipher', layout)
    return window


def cipher():
    window = make_window()
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == 'Back':
            break
        window['output'].Update('')
        if event == 'Apply':
            if value['type of action'] == 'encode':
                window['output'].Update(Encode(value['input'], value['shift'], value['language']))
            if value['type of action'] == 'decode':
                window['output'].Update(Decode(value['input'], value['shift'], value['language']))
    window.close()







