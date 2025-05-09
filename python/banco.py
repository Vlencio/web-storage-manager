import sqlite3

def table():
    #%%
    import sqlite3
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
                   
INSERT INTO produtos (nome, quantidade, ativo, data_recebimento, id_fornecedor) VALUES
('Extensão elétrica', 488, TRUE, '2024-12-29', 97),
('Cimento CP II', 171, FALSE, '2024-08-26', 4),
('Interruptor Simples', 438, FALSE, '2025-03-25', 97),
('Lâmpada LED', 470, TRUE, '2024-09-24', 85),
('Caixa dágua', 31, FALSE, '2024-08-22', 28),
('Lixa dágua', 467, FALSE, '2024-04-27', 46),
('Tijolo baiano', 82, FALSE, '2024-11-22', 97),
('Canos PVC', 494, FALSE, '2025-04-10', 41),
('Caixa de ferramentas', 221, TRUE, '2025-02-14', 20),
('Caixa dágua', 226, TRUE, '2024-07-14', 76),
('Arame galvanizado', 242, FALSE, '2025-02-19', 99),
('Luvas de proteção', 401, TRUE, '2024-06-18', 6),
('Parafuso', 193, TRUE, '2024-08-15', 37),
('Interruptor Simples', 478, TRUE, '2024-09-19', 56),
('Broca SDS', 369, TRUE, '2024-11-29', 16),
('Luvas de proteção', 218, FALSE, '2024-04-29', 24),
('Capacete de segurança', 272, FALSE, '2024-09-21', 24),
('Tinta Acrílica', 342, FALSE, '2025-03-30', 52),
('Trena 5m', 93, FALSE, '2024-06-27', 66),
('Canos PVC', 273, TRUE, '2024-11-29', 58),
('Broca SDS', 265, FALSE, '2025-03-26', 2),
('Interruptor Simples', 238, TRUE, '2024-12-03', 95),
('Tomada', 437, TRUE, '2024-06-25', 50),
('Luvas de proteção', 258, TRUE, '2024-11-19', 24),
('Válvula de descarga', 394, FALSE, '2024-09-12', 78),
('Nível de bolha', 14, FALSE, '2024-11-28', 23),
('Cotovelo PVC', 386, TRUE, '2024-07-16', 93),
('Caixa dágua', 308, TRUE, '2024-11-07', 17),
('Caixa de ferramentas', 310, TRUE, '2024-08-17', 78),
('Furadeira', 218, FALSE, '2025-04-03', 60),
('Canos PVC', 370, TRUE, '2024-10-26', 69),
('Caixa de ferramentas', 481, TRUE, '2024-12-13', 77),
('Arame galvanizado', 360, TRUE, '2024-06-07', 18),
('Trena 5m', 160, TRUE, '2024-11-21', 5),
('Cotovelo PVC', 458, TRUE, '2024-05-11', 78),
('Martelo', 206, FALSE, '2025-01-07', 96),
('Joelho PVC', 480, FALSE, '2024-12-07', 69),
('Fio 2,5mm', 56, TRUE, '2025-02-15', 91),
('Telha cerâmica', 134, FALSE, '2024-09-01', 20),
('Torneira elétrica', 480, TRUE, '2025-02-17', 6),
('Caixa dágua', 225, TRUE, '2024-08-30', 82),
('Broca SDS', 315, TRUE, '2024-05-27', 49),
('Arame galvanizado', 480, FALSE, '2025-02-07', 17),
('Chave de Fenda', 66, TRUE, '2024-12-06', 2),
('Martelo', 311, TRUE, '2024-11-14', 1),
('Lixa dágua', 359, FALSE, '2024-06-20', 35),
('Joelho PVC', 149, TRUE, '2025-02-21', 86),
('Trena 5m', 427, FALSE, '2024-11-21', 62),
('Capacete de segurança', 91, TRUE, '2024-09-10', 95),
('Nível de bolha', 125, TRUE, '2025-01-01', 11),
('Furadeira', 320, FALSE, '2025-03-06', 42),
('Tinta Acrílica', 5, TRUE, '2025-04-10', 37),
('Tinta Acrílica', 74, TRUE, '2025-02-13', 27),
('Parafuso', 495, FALSE, '2024-06-08', 90),
('Arame galvanizado', 3, TRUE, '2024-06-05', 55),
('Prego', 161, FALSE, '2024-09-10', 41),
('Nível de bolha', 91, TRUE, '2025-04-03', 81),
('Extensão elétrica', 385, TRUE, '2024-06-06', 45),
('Torneira elétrica', 399, FALSE, '2025-01-21', 71),
('Furadeira', 283, FALSE, '2025-02-10', 23),
('Torneira elétrica', 402, TRUE, '2025-04-05', 51),
('Parafuso', 390, TRUE, '2024-06-17', 11),
('Arame galvanizado', 235, FALSE, '2025-04-10', 27),
('Caixa de ferramentas', 242, FALSE, '2024-12-24', 82),
('Válvula de descarga', 198, TRUE, '2025-01-12', 78),
('Cotovelo PVC', 30, FALSE, '2024-08-21', 8),
('Tinta Acrílica', 404, FALSE, '2024-07-15', 100),
('Cimento CP II', 259, FALSE, '2025-01-02', 65),
('Martelo', 82, TRUE, '2024-07-07', 70),
('Tinta Acrílica', 347, TRUE, '2024-08-01', 73),
('Prego', 470, FALSE, '2024-09-24', 35),
('Telha cerâmica', 284, FALSE, '2024-05-27', 20),
('Furadeira', 33, FALSE, '2025-03-22', 34),
('Broca SDS', 170, FALSE, '2025-01-13', 99),
('Parafuso', 51, TRUE, '2025-02-23', 47),
('Tijolo baiano', 381, FALSE, '2024-08-07', 72),
('Furadeira', 116, FALSE, '2024-09-05', 66),
('Furadeira', 85, FALSE, '2025-01-25', 6),
('Cotovelo PVC', 25, FALSE, '2024-07-29', 49),
('Arame galvanizado', 102, TRUE, '2024-07-11', 38),
('Martelo', 124, FALSE, '2024-12-09', 11),
('Prego', 385, TRUE, '2024-08-02', 61),
('Furadeira', 136, FALSE, '2024-07-21', 85),
('Capacete de segurança', 72, FALSE, '2024-09-06', 28),
('Telha cerâmica', 387, FALSE, '2024-10-13', 79),
('Parafuso', 494, FALSE, '2025-01-16', 33),
('Lâmpada LED', 495, TRUE, '2024-10-11', 74),
('Tinta Acrílica', 129, FALSE, '2024-11-04', 42),
('Cotovelo PVC', 294, TRUE, '2025-02-07', 91),
('Prego', 175, FALSE, '2024-12-03', 15),
('Fio 2,5mm', 208, FALSE, '2025-02-25', 27),
('Parafuso', 333, TRUE, '2025-01-25', 5),
('Torneira elétrica', 277, TRUE, '2024-12-20', 10),
('Telha cerâmica', 433, TRUE, '2024-11-20', 59),
('Prego', 158, FALSE, '2024-11-07', 59),
('Válvula de descarga', 144, TRUE, '2024-10-12', 28),
('Lixa dágua', 97, TRUE, '2024-11-20', 79),
('Broca SDS', 214, TRUE, '2024-12-08', 1),
('Parafuso', 5, TRUE, '2025-01-27', 26),
('Cimento CP II', 104, FALSE, '2025-04-15', 65);

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

    def consultar_produto(self, coluna = None, parametros = None):
        try:
            if not parametros:
                self.cursor.execute('SELECT * FROM produtos')
                resultados = self.cursor.fetchall()
                  
            else:
                query = 'SELECT * FROM fornecedores WHERE ' + ' AND '.join(coluna)
                self.cursor.execute(query, parametros)
                resultados = self.cursor.fetchall()
            
            return resultados
        
        except Exception as e:
            return print(f'Algo deu errado.\n{e}')

    def editar_produto(self, coluna, parametros):
        pass

# %%
