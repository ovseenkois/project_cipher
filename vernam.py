import PySimpleGUI as sg
import alphabets




def Encode(string, key, language):
    if language == 'rus':
        alphabet = alphabets.rus_alphabet
    else:
        alphabet = alphabets.eng_alphabet
    new_string =[]
    for i in range(len(string)):
        if alphabet[0] <= string[i] <= alphabet[-1] or alphabet[0].upper() <= string[i] <= alphabet[-1].upper():
            bin_code_string = bin(ord(string[i]))[2:]
            bin_code_string = '0' * (11 - len(bin_code_string)) + bin_code_string
            bin_code_key = bin(ord(key[i]))[2:]
            bin_code_key = '0' * (11 - len(bin_code_key)) + bin_code_key
            bin_code_new_string = ''.join([str((int(bin_code_string[i]) + int(bin_code_key[i])) % 2)for i in range(11)])
            new_string.append(chr(int(bin_code_new_string, 2)))
        else:
            new_string.append(string[i])
    return ''.join(new_string)

def Decode(string, key, language):
    if language == 'rus':
        alphabet = alphabets.rus_alphabet
    else:
        alphabet = alphabets.eng_alphabet
    new_string =[]
    for i in range(len(string)):
        if alphabet[0] <= string[i] <= alphabet[-1] or alphabet[0].upper() <= string[i] <= alphabet[-1].upper():
            bin_code_string = bin(ord(string[i]))[2:]
            bin_code_string = '0' * (11 - len(bin_code_string)) + bin_code_string
            bin_code_key = bin(ord(key[i]))[2:]
            bin_code_key = '0' * (11 - len(bin_code_key)) + bin_code_key
            bin_code_new_string = ''.join([str((int(bin_code_string[i]) + int(bin_code_key[i])) % 2)for i in range(11)])
            new_string.append(chr(int(bin_code_new_string, 2)))
        else:
            new_string.append(string[i])
    return ''.join(new_string)

def Make_window():
    layout = [[sg.Button('Back')],
              [sg.Text('Text:')],
              [sg.Multiline(size=(50, 10), expand_x=True, key='input')],
              [sg.Text('Alphabet'), sg.Text('Type of operation'), sg.Text('Key')],
              [sg.Combo(['rus', 'eng'], default_value='rus', readonly=True, key='language'),
               sg.Combo(['encode', 'decode'], default_value='encode', readonly=True, key='type of action'),
               sg.InputText(key='key')],
              [sg.Button('Apply', expand_x=True)],
              [sg.Text('Result:')],
              [sg.Multiline(size=(50, 10), expand_x=True, key='output')]]
    window = sg.Window('Vernam cipher', layout, size=(500,500))
    return window

def Cipher():
    window = Make_window()
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == 'Back':
            break
        window['output'].Update('')
        if event == 'Apply':
            if value['type of action'] == 'encode':
                window['output'].Update(Encode(value['input'], value['key'], value['language']))
            if value['type of action'] == 'decode':
                window['output'].Update(Decode(value['input'], value['key'], value['language']))
    window.close()


