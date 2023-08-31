import mysql.connector
import os
from dotenv import load_dotenv
# from cores import *
from tkinter import *
from tkinter import messagebox
from env import *

load_dotenv('./env')

def mostrar_senha():
    if mostrar.get():
        campo_passwd.config(show="")
    else:
        campo_passwd.config(show="*")

def entrar(event=None):
    try:
        conn = mysql.connector.connect(
            host=os.environ['HOST'],
            port=os.environ['PORT'],
            user = campo_nome.get(),
            passwd = campo_passwd.get(),
            db=os.environ['DB']
        )

    except:
        messagebox.showerror('Error', 'Erro ao conectar')
    else:
        messagebox.showinfo('Sucesso', 'Conexao realizada com sucesso!')
    finally:
        campo_nome.delete(0, 'END')
        campo_passwd.delete(0, 'END')
        campo_nome.focus()


# Criando janela
janela = Tk()
janela.title('Tkinter - Projeto 01')
janela.geometry('310x300')
# janela.bind('<Return>', entrar)

# Dividindo a janela
frame_cima = Frame(
    master=janela,
    width=300,
    height=50
)
frame_cima.grid(row=0, column=0, padx=0, pady=1)

frame_baixo = Frame(
    master=janela,
    width=300,
    height=250
)

frame_baixo.grid(row=1, column=0)

# Configurando frame_cima
label = Label(
    master=frame_cima,
    text='Login',
    font=('Ariel', 25),
    bg="white",
    fg='black'
)
label.place(x=5, y=3)

linha = Label(
    master=frame_cima,
    width=275,
    height=100,
    bg="white",
    fg='black'
)
linha.place(x=20, y=47)


# configurando frame de baixo
nome = Label(
    master=frame_baixo,
    text='Nome',
    font=('Arial', 25),
    bg='white',
    fg='black'
)
nome.place(x=10, y=20)

campo_nome = Entry(
    master=frame_baixo,
    width=22,
    justify='left',
    font=('Arial', 12),
    highlightthickness=1,
    relief='solid'
)
campo_nome.place(x=10, y=50)

passwd = Label(
    master=frame_baixo,
    width=22,
    justify='left',
    font=('Arial', 12)
)
passwd.place(x=10, y=95)

campo_passwd = Entry(
    master=frame_baixo,
    width=22,
    justify='left',
    font=('Arial', 12),
    show="*",
    highlightthickness=1,
    relief='solid'
)
campo_passwd.place(x=10, y=130)

mostrar = IntVar()
mostrar_senha = IntVar()
check = Checkbutton(
    master=frame_baixo,
    text='Mostrar senha',
    variable=mostrar,
    justify='left',
    font=('Arial', 12),
    command=mostrar_senha
)
check.place(x=180, y=160)

btn_confirmar = Button(
    master=frame_baixo,
    width=28,
    text='ENTRAR',
    justify='left',
    height=2,
    font=('Arial', 12),
    command=entrar
)

btn_confirmar.place(x=30, y=190)

# Dando foco
campo_nome.focus()


janela.mainloop()