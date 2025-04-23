import sqlite3

def table():
    #%%
    import sqlite3
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
INSERT INTO fornecedores (nome, cnpj, telefone, email, endereco) VALUES
('Fornecedora Vale Tudo Ltda', '12.345.678/0001-90', '(11) 91234-5678', 'contato@valetudoltda.com.br', 'Rua das Palmeiras, 123 - São Paulo/SP'),
('Distribuidora Estrela Azul', '98.765.432/0001-01', '(21) 98765-4321', 'vendas@estrelaazul.com.br', 'Av. Atlântica, 456 - Rio de Janeiro/RJ'),
('Comercial Nova Era ME', '45.678.912/0001-22', '(31) 99876-1234', 'suporte@novaera.com.br', 'Rua dos Andradas, 789 - Belo Horizonte/MG'),
('Supra Fornecimentos LTDA', '67.890.123/0001-33', '(51) 99123-4567', 'atendimento@supra.com.br', 'Av. Ipiranga, 321 - Porto Alegre/RS'),
('Alpha Produtos e Serviços', '23.456.789/0001-44', '(41) 98765-0987', 'contato@alphaps.com.br', 'Rua XV de Novembro, 654 - Curitiba/PR'),
('Max Supply Importações', '34.567.890/0001-55', '(61) 99654-3210', 'vendas@maxsupply.com.br', 'SQN 210, Bloco B - Brasília/DF'),
('Delta Comercial BR', '56.789.012/0001-66', '(71) 99234-5670', 'delta@comercialbr.com.br', 'Rua Chile, 890 - Salvador/BA'),
('FornecPlus Soluções Ltda', '78.901.234/0001-77', '(85) 98760-4321', 'fornecplus@solucoes.com.br', 'Av. Beira Mar, 112 - Fortaleza/CE'),
('EcoFornecedor Sustentável', '89.012.345/0001-88', '(91) 99110-2233', 'contato@ecofornecedor.com.br', 'Travessa das Flores, 55 - Belém/PA'),
('Rápido Distribuições S/A', '10.123.456/0001-99', '(62) 99888-7766', 'atendimento@rapidodist.com.br', 'Rua Goiás, 777 - Goiânia/GO');

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
            self.cursor.execute('INSERT INTO produtos (nome, quantidade, ativo, data_recebimento, id_fornecedor) VALUES (?, ?, ?, ?, ?)', nome, quantidade, ativo, data_recebimento, id_fornecedor)
            self.conn.commit()
        
        except Exception as e:
            return print(f'Algo deu errado.\n{e}')

        return print('Produto cadastrado com sucesso.')
