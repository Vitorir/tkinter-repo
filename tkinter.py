from tkinter import *

# def saudacao(event=None):
#     label2['text'] = f'Olá {field1}'

janela = Tk()
janela.title('Atividade de aula')
# janela.bind('<Return>', saudacao)

label1 = Label(
    master=janela,
    text='Digite seu nome: ',
    font=('Quicksand Regular', 14)
)
label1.grid(row=0, column=0, padx=5, pady=5)

field1 = Entry(
    master=janela
)
field1.grid(row=0, column=1, padx=5, pady=5)



janela.mainloop()