import PySimpleGUI as sg
import alphabets
from random import randint



def Encode(string, key, language):
    flag = False
    if language == 'rus':
        alphabet = alphabets.rus_alphabet
    else:
        alphabet = alphabets.eng_alphabet
    if key == 'generate a key':
        flag = True
        key = []
        for i in range(len(string)):
            key.append(alphabet[randint(0, len(alphabet) - 1)])
        key = ''.join(key)
    new_string = []
    len_alphabet = len(alphabet)
    for i in range(len(string)):
        if string[i] in alphabet:
            code_string = alphabet.index(string[i].lower())
            code_key = alphabet.index(key[i % len(key)].lower())
            new_string.append(alphabet[(code_string + code_key) % len_alphabet])
        elif string[i] in alphabet.upper():
            code_string = alphabet.index(string[i].lower())
            code_key = alphabet.index(key[i % len(key)].lower())
            new_string.append(alphabet[(code_string + code_key) % len_alphabet].upper())
        else:
            new_string.append(string[i])
    if flag:
        return [''.join(new_string), key]
    return [''.join(new_string)]

def Decode(string, key, language):
    if language == 'rus':
        alphabet = alphabets.rus_alphabet
    else:
        alphabet = alphabets.eng_alphabet
    new_string = []
    len_alphabet = len(alphabet)
    for i in range(len(string)):
        if string[i] in alphabet:
            code_string = alphabet.index(string[i].lower())
            code_key = alphabet.index(key[i % len(key)].lower())
            new_string.append(alphabet[(code_string - code_key) % len_alphabet])
        elif string in alphabet.upper():
            code_string = alphabet.index(string[i].lower())
            code_key = alphabet.index(key[i % len(key)].lower())
            new_string.append(alphabet[(code_string - code_key) % len_alphabet].upper())
        else:
            new_string.append(string[i])
    return ''.join(new_string)


def Make_window():
    layout = [[sg.Button('Back')],
              [sg.Text('Text:')],
              [sg.Text('Input file: '), sg.InputText(do_not_clear=False, key='input file'), sg.FileBrowse()],
              [sg.Multiline(size=(50, 10), expand_x=True, key='input')],
              [sg.Text('Alphabet'), sg.Text('Type of operation'), sg.Text('Key'),
               sg.InputText(key='key file', size=(15,1), do_not_clear=False), sg.FileBrowse()],
              [sg.Combo(['rus', 'eng'], default_value='rus', readonly=True, key='language'),
               sg.Combo(['encode', 'decode'], default_value='encode', readonly=True, key='type of action'),
               sg.Combo(['generate a key'], key='key', size=(50, 1))],
              [sg.Button('Apply', expand_x=True)],
              [sg.Text('Result:')],
              [sg.Text('Output file: '), sg.InputText(do_not_clear=False, key='output file'), sg.FileBrowse()],
              [sg.Multiline(size=(50, 10), expand_x=True, key='output')]]
    window = sg.Window('Visener cipher', layout, size=(500, 600))
    return window

def Cipher():
    window = Make_window()
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == 'Back':
            break
        window['output'].Update('')
        if event == 'Apply':
            if value['input file'] != '':
                try:
                    input_file = open(value['input file'], 'r')
                    input = input_file.read()
                    input_file.close()
                except:
                    sg.popup_ok('no such directory or file')
                    continue
            else:
                input = value['input']
            if value['output file'] != '':
                try:
                    check = open(value['output file'], 'r')
                    check.close()
                    write_to_file = True
                except:
                    sg.popup_ok('no such directory or file')
                    continue
            else:
                write_to_file = False
            if value['key file'] != '':
                try:
                    key_file = open(value['key file'], 'r')
                    key = key_file.read()
                    key_file.close()
                except:
                    sg.popup_ok('no such directory or file')
            else:
                key = value['key']
            if key != 'generate a key':
                if len(''.join(input.lower().split())) != len(''.join(key.lower().split())):
                    sg.popup_ok('the length of the key must be the same as the length of the string')
                    continue
            if value['type of action'] == 'encode':
                if write_to_file:
                    output_file = open(value['output file'], 'w')
                    encoded_string = Encode(input, key, value['language'])
                    if len(encoded_string) == 2:
                        output_file.write(f'Your key: {encoded_string[1]} \n{encoded_string[0]}')
                    else:
                        output_file.write(encoded_string[0])
                    output_file.close()
                else:
                    encoded_string = Encode(input, key, value['language'])
                    if len(encoded_string) == 2:
                        window['output'].Update(f'Your key: {encoded_string[1]} \n{encoded_string[0]}')
                    else:
                        window['output'].Update(encoded_string[0])
            if value['type of action'] == 'decode':
                if write_to_file:
                    output_file = open(value['output file'], 'w')
                    output_file.write(Decode(input, key, value['language']))
                    output_file.close()
                else:
                    window['output'].Update(Decode(input, key, value['language']))
    window.close()



