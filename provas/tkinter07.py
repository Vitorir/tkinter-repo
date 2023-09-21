from tkinter import *
from tkinter import filedialog

janela = Tk()

janela.geometry('500x300')
janela.title('SysLista')


def gravar_informacoes():
    nome=txt_nome.get()
    telefone=txt_telefone.get()

    if nome and telefone: #se nao tiverem valores vazios em nome e telefone o
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt")])
        if not arquivo:
           return

        with open(arquivo, "a") as file:
            file.write(f"Nome: {nome}, Telefone: {telefone}\n")



    txt_nome.delete(0, END)  # pra apagar o nome quando o usuario clicar em cadastro
    txt_telefone.delete(0, END)




label_titulo = Label(janela, text='AGENDA TELEFÔNICA', font='Arial 20 bold', fg='white', bg='red')
label_titulo.place(x=60, y=15)

label_nome = Label(text='Nome:', font='Arial 16 bold', foreground='Black')
label_nome.place(x=60, y=70)
txt_nome = Entry(janela, font='Arial 16 bold', foreground='Black', width=20, border=3)
txt_nome.place(x=180, y=70)
label_telefone = Label(janela, text='Telefone:', font='Arial 16 bold', foreground='Black')
label_telefone.place(x=60, y=120)
txt_telefone = Entry(janela, font='Arial 16 bold', foreground='Black', width=20, border=3)
txt_telefone.place(x=180, y=120)
btn_cadastrar = Button(janela, text='Cadastrar', bg='orange', font='Arial 16 bold', fg='white', height=1, width=10, command=gravar_informacoes)
btn_cadastrar.place(x=150, y=200, )


janela.mainloop()