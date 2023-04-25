import tkinter as tk
from tkinter import messagebox
import sqlite3
import csv
def cadastrar_cliente():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    if nome == '' or sobrenome == '' or email == '' or telefone == '':
        messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')
        return
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("INSERT INTO clientes VALUES (NULL,?,?,?,?)", (nome, sobrenome, email, telefone))
    conn.commit()
    conn.close()
    messagebox.showinfo('Cadastro', 'Cliente cadastrado com sucesso.')
    # Limpar campos de entrada
    entry_nome.delete(0, 'end')
    entry_sobrenome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')
def exportar_csv():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clientes")
    with open('clientes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'sobrenome', 'email', 'telefone'])
        for row in c:
            writer.writerow(row)
    conn.close()
    messagebox.showinfo('Exportar Excel', 'Dados exportados para o arquivo "clientes.csv" com sucesso.')
# Interface gráfica
root = tk.Tk()
root.title('Cadastro de Clientes')
root.geometry("600x300")
# Labels
label_nome = tk.Label(root, text='Nome:')
label_nome.grid(row=0, column=0, padx=5, pady=5)
label_sobrenome = tk.Label(root, text='Sobrenome:')
label_sobrenome.grid(row=1, column=0, padx=5, pady=5)
label_email = tk.Label(root, text='Email:')
label_email.grid(row=2, column=0, padx=5, pady=5)
label_telefone = tk.Label(root, text='Telefone:')
label_telefone.grid(row=3, column=0, padx=5, pady=5)
# Campos de entrada
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=0, column=1, padx=5, pady=5)
entry_sobrenome = tk.Entry(root, width=50)
entry_sobrenome.grid(row=1, column=1, padx=5, pady=5)
entry_email = tk.Entry(root, width=50)
entry_email.grid(row=2, column=1, padx=5, pady=5)
entry_telefone = tk.Entry(root, width=50)
entry_telefone.grid(row=3, column=1, padx=5, pady=5)
# Botões
button_cadastrar = tk.Button(root, text='Cadastrar', command=cadastrar_cliente)
button_cadastrar.grid(row=4, column=0, padx=5, pady=5)
button_exportar_csv = tk.Button(root, text='Exportar Excel', command=exportar_csv)
button_exportar_csv.grid(row=4, column=1, padx=5, pady=5)
root.mainloop()