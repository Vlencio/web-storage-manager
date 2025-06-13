import sqlite3

def table():
    #%%
    import sqlite3
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('''
                ALTER TABLE vendas ADD COLUMN lucro REAL NOT NULL  

''')
    conn.commit()
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
            self.cursor.execute('INSERT INTO produtos (nome, quantidade, ativo, data_recebimento, id_fornecedor) VALUES (?, ?, ?, ?, ?)', (nome, quantidade, ativo, data_recebimento, id_fornecedor))
            self.conn.commit()

        except Exception as e:
            return print(f'Algo deu errado.\n{e}')

        return print('Produto cadastrado com sucesso.')

    def consultar_produto(self, coluna = None, parametros = None):
        try:
            if not parametros:
                self.cursor.execute('SELECT * FROM produtos')
                resultados = self.cursor.fetchall()
                  
            else:
                query = 'SELECT * FROM produtos WHERE ' + ' AND '.join(coluna)
                self.cursor.execute(query, parametros)
                resultados = self.cursor.fetchall()
            
            return resultados
        
        except Exception as e:
            return print(f'Algo deu errado.\n{e}')

    def editar_produto(self, dados):
        produto_id = dados.get('id')
        campos = ['nome', 'quantidade', 'ativo', 'data_recebimento', 'id_fornecedor']
        valores = [dados[campo] for campo in campos if campo in dados]
        valores[2] = 1 if valores[2] == 'Sim' else 0
        virgula = ', '.join([f"{campo} = ?" for campo in campos if campo in dados])
        try:
            self.cursor.execute(f'''
                                UPDATE produtos
                                SET {virgula}
                                WHERE id = ?
            ''', valores + [produto_id])
            self.conn.commit()
            return True
        
        except Exception as e:
            print(f'Erro: {e}')
            return False

    def adicionar_venda(self, dados):
        #dados = [dados.get('id_produto'), dados.get('nome_produto'), dados.get('quantidade_venda'), dados.get('valor'), dados.get('data_venda')]
        self.cursor.execute('SELECT valor_unitario, nome FROM produtos WHERE id = ?', dados[0])
        consulta = self.cursor.fetchone()
        dados.append(float(dados[2]) - consulta[0])
        dados.append(consulta[1])
        self.cursor.execute('INSERT INTO vendas (id_produto, quantidade_venda, valor, data_venda, lucro, nome_produto) VALUES (?, ?, ? ,?, ?, ?)', dados)
        self.conn.commit()

        return

    def consultar_vendas(self, coluna = None, parametros = None):
        try:
            if not parametros:
                self.cursor.execute('SELECT * FROM vendas')
                resultados = self.cursor.fetchall()
                  
            else:
                query = 'SELECT * FROM vendas WHERE ' + ' AND '.join(coluna)
                self.cursor.execute(query, parametros)
                resultados = self.cursor.fetchall()
            
            return resultados
        
        except Exception as e:
            return print(f'Algo deu errado.\n{e}')

    def editar_venda(self, dados):
        produto_id = dados.get('id')
        produto_id2 = dados.get('id_produto')

        self.cursor.execute('SELECT valor_unitario FROM produtos WHERE id = ?', produto_id2)
        valor = float(self.cursor.fetchone()[0])

        campos = ['quantidade_venda', 'valor', 'data_venda']
        valores = [dados[campo] for campo in campos if campo in dados]
        lucro = float(valores[1]) - float(valor)
        campos.append('lucro')
        valores.append(lucro)
        virgula = ', '.join([f"{campo} = ?" for campo in campos if campo in dados]) + f', lucro = ?'
        try:
            self.cursor.execute(f'''
                                UPDATE vendas
                                SET {virgula}
                                WHERE id = ?
            ''', valores + [produto_id])
            self.conn.commit()
            return True
        
        except Exception as e:
            print(f'Erro: {e}')
            return False

    def dashboard(self):
        self.cursor.execute('SELECT lucro FROM vendas')
        tuplas = self.cursor.fetchall()
        self.cursor.execute('SELECT quantidade_venda FROM vendas')
        tuplas2 = self.cursor.fetchall()
        lucro = 0
        for tupla, tupla2 in zip(tuplas, tuplas2):
            lucro += float(tupla[0]) * tupla2[0]
        
        self.cursor.execute('SELECT quantidade FROM produtos WHERE ativo = 1')
        tuplas = self.cursor.fetchall()
        produtos = 0
        for tupla in tuplas:
            produtos += int(tupla[0])
        
        self.cursor.execute('SELECT * FROM fornecedores')
        tuplas = self.cursor.fetchall()
        fornecedores = len(tuplas)
        return [lucro, produtos, fornecedores]
