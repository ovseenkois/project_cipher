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


def Make_window():
    list_shifts = ['decode without shift']
    list_shifts.extend([str(i) for i in range(1, 40)])
    layout = [[sg.Button('Back')],
              [sg.Text('Text:')],
              [sg.Text('Input file: '), sg.InputText(do_not_clear=False, key='input file'), sg.FileBrowse()],
              [sg.Multiline(size=(50, 10), expand_x=True, key='input')],
              [sg.Text('Alphabet'), sg.Text('Type of operation'), sg.Text('Shift')],
              [sg.Combo(['rus', 'eng'], default_value='rus', readonly=True, key='language'),
               sg.Combo(['encode', 'decode'], default_value='encode', readonly=True, key='type of action'),
               sg.Combo(list_shifts, default_value='3', readonly=True, key='shift')],
              [sg.Button('Apply', expand_x=True)],
              [sg.Text('Result:')],
              [sg.Text('Output file: '), sg.InputText(do_not_clear=False, key='output file'), sg.FileBrowse()],
              [sg.Multiline(size=(50, 10), expand_x=True, key='output')]]
    window = sg.Window('Caesar cipher', layout, size=(500, 500))
    return window


def DecodeWithoutShift(string, language):
    string = string.lower()
    if language == 'rus':
        alphabet = alphabets.rus_alphabet
        frequency_alphabet = alphabets.rus_frequency
    else:
        alphabet = alphabets.eng_alphabet
        frequency_alphabet = alphabets.eng_frequncy
    len_alphabet = len(alphabet)
    min_delta_shift = 999999
    min_sum_of_delta = 999999
    for shift in range(len_alphabet):
        decode_string = Decode(string, shift, language)
        frequency = {}
        for i in decode_string:
            if i in alphabet:
                if i in frequency.keys():
                    frequency[i] = (frequency[i] / 100 * len(decode_string) + 1) / len(decode_string) * 100
                else:
                    frequency[i] = 1 / len(decode_string) * 100
        sum_of_delta = 0
        for letter in frequency.keys():
            sum_of_delta += (frequency_alphabet[letter] - frequency[letter])**2
        if sum_of_delta < min_sum_of_delta:
            min_sum_of_delta = sum_of_delta
            min_delta_shift = shift
    return Decode(string, min_delta_shift, language)


def Cipher():
    window = Make_window()
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == 'Back':
            break
        window['output'].Update('')
        if event == 'Apply':
            if value['type of action'] == 'encode':
                window['output'].Update(Encode(value['input'], value['shift'], value['language']))
            if value['type of action'] == 'decode':
                if value['shift'] == 'decode without shift':
                    window['output'].Update(DecodeWithoutShift(value['input'], value['language']))
                else:
                    window['output'].Update(Decode(value['input'], value['shift'], value['language']))
    window.close()







