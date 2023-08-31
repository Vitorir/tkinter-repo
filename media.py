import PySimpleGUI as sg

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

layout = [
    [sg.Text('Calculadora de Média de Alunos')],
    [sg.Text('Insira as notas dos alunos (para encerrar, deixe o campo em branco):')],
    [sg.InputText(key='nota')],
    [sg.Button('Adicionar Nota'), sg.Button('Calcular Média'), sg.Button('Sair')],
    [sg.Text('Médias individuais:')],
    [sg.Listbox(values=[], size=(30, 10), key='medias')],
]

notas_alunos = []

window = sg.Window('Calculadora de Média', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Adicionar Nota':
        try:
            nota = float(values['nota'])
            notas_alunos.append(nota)
            sg.popup(f'Nota {nota} adicionada com sucesso!')
            window['nota'].update('')
        except ValueError:
            sg.popup_error('Insira um valor numérico válido para a nota.')
    elif event == 'Calcular Média':
        media = calcular_media(notas_alunos)
        window['medias'].update(values=[f'Média da turma: {media:.2f}'])
    else:
        pass

window.close()
