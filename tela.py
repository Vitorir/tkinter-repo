# 1a: Importação
import PySimpleGUI as sg

# 2a: Layout
layout = [
    [sg.Text('Comente: '), sg.Input(key='-IN-')],
    [sg.Text("Saída aqui", size=(30, 1), key='-OUT-')],
    [sg.Button('OK'), sg.Button('Exit')]
]

# 3a: Janela
janela = sg.Window('Title', layout)

# 4a: Laço de Eventos
# Quando le a janela, espera um evento;
while True:
    event, values = janela.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    janela['-OUT-'].update(values['-IN-']) # atualizar o elemento com chave 'out'
    # com os valores que entram do elemento com chave 'in'

janela.close()