import PySimpleGUI as sg

tarefas = []

layout = [
    [sg.Text("Digite uma tarefa: "), sg.InputText(key="Tarefa"), sg.Button(key='Adicionar')],
    [sg.Listbox(values=tarefas, size=(40, 10), key="-LIST-")],
    [sg.Button('Remover'), sg.Button('Limpar'), sg.Button('Sair')]
]

janela = sg.Window("Lista de Tarefas", layout)

while True:
    events, values == janela.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if event == 'Adicionar' and values['Tarefa']:
        tarefas.append