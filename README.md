# banco_de_dados_sql
Banco de dados em SQL criado via Python. Integração e cadastro de clientes.


Importante alterar os campos abaixo. Server e Database

self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=Nome_do_seu_servidor'
                              'Database=Nome_do_seu_banco'
                              'Trusted_Connection=yes;')
