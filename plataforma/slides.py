import tkinter as tk



def converter():
    try:
        centimetros = float(entry_centimetros.get())
        metros = centimetros / 100
        resultado_label.config(text=f'{centimetros} centímetros é igual a {metros} metros')

    except ValueError:
        resultado_label.config(text='Digite um valor válido')

janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")



entrada_label = tk.Label(janela, text="Digite a quantidade de centímetros:")
entrada_label.pack()


entry_centimetros = tk.Entry(janela)
entry_centimetros.pack()