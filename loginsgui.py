import PySimpleGUI as sg

def fazer_login(username, password):
    if username == "admin" and password == "senha123":
        sg.popup("Login realizado com sucesso!")
    else:
        sg.popup("Nome de usuário ou senha incorretos.")

# Definindo o layout da janela
layout = [
    [sg.Text("Nome de usuário"), sg.Input(key="-USERNAME-")],
    [sg.Text("Senha"), sg.Input(key="-PASSWORD-", password_char="*")],
    [sg.Button("Login")]
]

# Criando a janela
window = sg.Window("Tela de Login", layout)

# Loop para ler eventos e dados da janela
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Login":
        username = values["-USERNAME-"]
        password = values["-PASSWORD-"]
        fazer_login(username, password)

# Fechando a janela
window.close()