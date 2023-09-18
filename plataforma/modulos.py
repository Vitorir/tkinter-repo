import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox

def salvar_contato():
    nome = nome_entry.get()
    telefone = telefone_entry.get()
    if 'contatos.txt' not in contatos_criados:
        arquivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo: 
        contatos_criados.add('contatos.txt')
    else:
        arquivo = open('contatos.txt', 'a')
    if arquivo:
        arquivo.write(f"Nome: {nome}, Telefone: {telefone}\n")
        arquivo.close()
        nome_entry.delete(0, tk.END)
        telefone_entry.delete(0, tk.END)
    else:
         messagebox.showerror("Erro", "Não foi possível criar o arquivo.")

root = tk.Tk()
root.title("Cadastro de Contatos")
root.geometry("230x300")

contatos_criados = set()
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root, width=30)
nome_entry.pack()
telefone_label = tk.Label(root, text="Telefone:")
telefone_label.pack()
telefone_entry = tk.Entry(root, width=30)
telefone_entry.pack()
cadastrar_button = tk.Button(root, text="Cadastrar", command=salvar_contato)
cadastrar_button.pack()

root.mainloop()