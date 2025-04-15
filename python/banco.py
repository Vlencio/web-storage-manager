import sqlite3

def table():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def cadastrar(email, usuario, senha):
    try:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (usuario, email, senha) VALUES (?, ?, ?)', (usuario, email, senha))
        conn.commit()
    
    finally:
        conn.close()

    return print('cadastrado com sucesso')

def login(email, senha):
    try:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        cursor.execute('SELECT email, senha, usuario FROM usuarios WHERE email = ?', (email,))
        dados = cursor.fetchone()
        if not dados or dados[1] != senha:
            return False
        
        return True

    finally:
        conn.close()
