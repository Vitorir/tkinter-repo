from tkinter import *
from tkinter import messagebox

def fazer_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "senha123":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")

# Criando janela
janela = Tk()
janela.title("Página de Login")
janela.geometry("300x200")

# Criando widgets
label_username = Label(janela, text="Nome de usuário:")
label_username.pack()

entry_username = Entry(janela)
entry_username.pack()

label_password = Label(janela, text="Senha:")
label_password.pack()

entry_password = Entry(janela, show="*")
entry_password.pack()

btn_login = Button(janela, text="Login", command=fazer_login)
btn_login.pack()

# Executando janela
janela.mainloop()