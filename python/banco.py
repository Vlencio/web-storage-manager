import sqlite3

def table():
    #%%
    import sqlite3
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS produtos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   quantidade INTEGER NOT NULL,
                   ativo BOOLEAN NOT NULL,
                   data_recebimento DATE NOT NULL,
                   id_fornecedor INTEGER NOT NULL,
                   FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id)
                )
''')
    #%%

class Banco():
    def __init__(self):
        self.conn = sqlite3.connect('banco.db')
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def cadastrar(self, email, usuario, senha):
        try:
            self.cursor.execute('INSERT INTO usuarios (usuario, email, senha) VALUES (?, ?, ?)', (usuario, email, senha))
            self.conn.commit()
        
        except Exception as e:
            self.conn.rollback()
            return print(f'Algo deu errado.\n{e}')       

        return print('cadastrado com sucesso')

    def login(self, email, senha):
        try:
            self.cursor.execute('SELECT email, senha, usuario FROM usuarios WHERE email = ?', (email,))
            dados = self.cursor.fetchone()
            if not dados or dados[1] != senha:
                return False
            
            return True

        except Exception as e:
            self.conn.rollback()
            return print(f'Algo deu errado.\n{e}')       

    def cadastrar_fornecedor(self, nome, cnpj, telefone, email, endereco):
        try:
            self.cursor.execute('INSERT INTO fornecedores (nome, cnpj, telefone, email, endereco) VALUES (?, ?, ?, ?, ?)', (nome, cnpj, telefone, email, endereco))
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            return print(f'Algo deu errado.\n{e}')

        return print('Fornecedor cadastrado com sucesso.')

    def consultar_fornecedor(self, coluna = None, parametros = None):
        try:
            if not parametros:
                self.cursor.execute('SELECT * FROM fornecedores')
                resultados = self.cursor.fetchall()
                return resultados
            
            else:
                query = 'SELECT * FROM fornecedores WHERE ' + ' AND '.join(coluna)
                self.cursor.execute(query, parametros)
                resultados = self.cursor.fetchall()
                return resultados
        
        except Exception as e:
            return print(f'Algo deu errado.\n{e}')

    def cadastrar_produto(self, nome, quantidade, ativo, data_recebimento, id_fornecedor):
        try:
            self.cursor.execute('INSERT INTO produtos (nome, quantidade, ativo, data_recebimento, id_fornecedor) VALUES (?, ?, ?, ?, ?)', nome, quantidade, ativo, data_recebimento, id_fornecedor)
            self.conn.commit()
        
        except Exception as e:
            return print(f'Algo deu errado.\n{e}')

        return print('Produto cadastrado com sucesso.')



