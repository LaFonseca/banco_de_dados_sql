import pyodbc
from tkinter import *

class CadastroCliente:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Cliente")

        self.label_nome = Label(master, text="Nome")
        self.label_nome.grid(row=0, column=0)

        self.label_sobrenome = Label(master, text="Sobrenome")
        self.label_sobrenome.grid(row=1, column=0)

        self.label_cpf = Label(master, text="CPF")
        self.label_cpf.grid(row=2, column=0)

        self.label_telefone = Label(master, text="Telefone")
        self.label_telefone.grid(row=3, column=0)

        self.label_email = Label(master, text="Email")
        self.label_email.grid(row=4, column=0)

        self.label_endereco = Label(master, text="Endereço")
        self.label_endereco.grid(row=5, column=0)

        self.entry_nome = Entry(master)
        self.entry_nome.grid(row=0, column=1)

        self.entry_sobrenome = Entry(master)
        self.entry_sobrenome.grid(row=1, column=1)

        self.entry_cpf = Entry(master)
        self.entry_cpf.grid(row=2, column=1)

        self.entry_telefone = Entry(master)
        self.entry_telefone.grid(row=3, column=1)

        self.entry_email = Entry(master)
        self.entry_email.grid(row=4, column=1)

        self.entry_endereco = Entry(master)
        self.entry_endereco.grid(row=5, column=1)

        self.button_cadastrar = Button(master, text="Cadastrar",
                                       command=self.cadastrar)
        self.button_cadastrar.grid(row=6, column=1)

        
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=Nome_do_seu_servidor'
                              'Database=Nome_do_seu_banco'
                              'Trusted_Connection=yes;')

        
        cursor = self.conn.cursor()
        cursor.execute('''
                        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='clientes' and xtype='U')
                        CREATE TABLE clientes
                        (id INT PRIMARY KEY,
                        nome VARCHAR(50),
                        sobrenome VARCHAR(50),
                        cpf VARCHAR(11),
                        telefone VARCHAR(20),
                        email VARCHAR(50),
                        endereco VARCHAR(100))
                        ''')

    def cadastrar(self):
        cursor = self.conn.cursor()

        
        cursor.execute("SELECT MAX(id) FROM clientes")
        result = cursor.fetchone()
        if result[0] is not None:
            id = result[0] + 1
        else:
            id = 1

        nome = self.entry_nome.get()
        sobrenome = self.entry_sobrenome.get()
        cpf = self.entry_cpf.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()
        endereco = self.entry_endereco.get()

        
        cursor.execute("SELECT * FROM clientes WHERE cpf=?", (cpf,))
        result = cursor.fetchone()
        if result is not None:
            print("CPF já cadastrado!")
            return

        
        cursor.execute("INSERT INTO clientes (id, nome, sobrenome, cpf, telefone, email, endereco) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (id, nome, sobrenome, cpf, telefone, email, endereco))

        
        self.conn.commit()

        print("Cliente cadastrado com sucesso!")
        self.entry_nome.delete(0, END)
        self.entry_sobrenome.delete(0, END)
        self.entry_cpf.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_endereco.delete(0, END)


root = Tk()
my_gui = CadastroCliente(root)
root.mainloop()