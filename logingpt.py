from tkinter import *

def fazer_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    if usuario == "usuario" and senha == "senha":
        resultado_label.config(text="Login realizado com sucesso!", fg="green")
    else:
        resultado_label.config(text="Credenciais inválidas", fg="red")
    
    campo_usuario.delete(0, END)
    campo_senha.delete(0, END)

janela = Tk()
janela.title("Página de Login")

frame = Frame(janela, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label_usuario = Label(frame, text="Usuário:")
label_usuario.grid(row=0, column=0, sticky=W)

campo_usuario = Entry(frame)
campo_usuario.grid(row=0, column=1, padx=10)

label_senha = Label(frame, text="Senha:")
label_senha.grid(row=1, column=0, sticky=W)

campo_senha = Entry(frame, show="*")
campo_senha.grid(row=1, column=1, padx=10)

botao_login = Button(frame, text="Fazer Login", command=fazer_login)
botao_login.grid(row=2, columnspan=2, pady=10)

resultado_label = Label(frame, text="", fg="black")
resultado_label.grid(row=3, columnspan=2)

janela.mainloop()
