from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from banco import Banco

app = Flask(__name__)
CORS(app)

@app.route('/api/cadastrar', methods=['POST'])
def cadastro():
    dado = request.get_json()
    email = dado.get('email')
    usuario = dado.get('usuario')
    senha = dado.get('senha')
    with Banco() as banco:
        banco.cadastrar(email, usuario, senha)

    return jsonify({"mensagem": "Sucesso!"}), 201

@app.route('/api/login', methods=['POST'])
def logar():
    dado = request.get_json()
    email = dado.get('email')
    senha = dado.get('senha')
    with Banco() as banco:
        res = banco.login(email, senha)
    if res:
        return jsonify({"mensagem": "Logado"}), 200

    return jsonify({"mensagem": "Login inválido"}), 401

@app.route('/api/consultar_fornecedor', methods=['GET'])
def consultar_fornecedor():
    
    with Banco() as banco:
        resultados = banco.consultar_fornecedor()
    lista = []
    for tupla in resultados:
        fornecedor = {"id": tupla[0], "nome": tupla[1], "cnpj": tupla[2], "telefone": tupla[3], "email": tupla[4], "endereco": tupla[5]}
        lista.append(fornecedor)
    
    return jsonify(lista)

@app.route('/api/consultar_fornecedor', methods=['POST'])
def consultar_fornecedor_parametros():
    dado = request.get_json()
    chaves = []
    valores = []
    for chave, valor in dado.items():
        if valor:
            chaves.append(f'{chave} LIKE ?')
            valores.append(f'%{valor}%')
    chaves = tuple(chaves)
    valores = tuple(valores)
    if len(chaves) <= 0:
        return Response(status=204)
    with Banco() as banco:
        resultados = banco.consultar_fornecedor(coluna=chaves, parametros=valores)
    

    lista = []
    for tupla in resultados:
        fornecedor = {"id": tupla[0], "nome": tupla[1], "cnpj": tupla[2], "telefone": tupla[3], "email": tupla[4], "endereco": tupla[5]}
        lista.append(fornecedor)

    return jsonify(lista), 200

@app.route('/api/cadastrar_fornecedor', methods=['POST'])
def cadastrar_fornecedor():
    json = request.get_json()
    
    nome = json.get('nome')
    cnpj = json.get('cnpj')
    telefone = json.get('telefone')
    email = json.get('email')
    endereco = json.get('endereço')

    with Banco() as banco:
        banco.cadastrar_fornecedor(nome, cnpj, telefone, email, endereco)

    return jsonify({"mensagem": "Sucesso"}), 204

@app.route('/api/consultar_produto', methods=['GET'])
def consultar_produto():
    from datetime import datetime

    with Banco() as banco:
        resultados = banco.consultar_produto()
    lista = []
    for dado in resultados:
        dado = list(dado)
        produto = {"id": dado[0], "nome": dado[1], "quantidade": dado[2], "ativo": dado[3], "data_recebimento": dado[4], "id_fornecedor": dado[5], "nome_fornecedor": dado[6], "valor_unitario": dado[7]}
        lista.append(produto)
    
    return jsonify(lista)

@app.route('/api/consultar_produto', methods=['POST'])
def consultar_produto_parametros():
    dado = request.get_json()
    chaves = []
    valores = []
    for chave, valor in dado.items():
        if valor:
            chaves.append(f'{chave} LIKE ?')
            valores.append(f'%{valor}%')
    chaves = tuple(chaves)
    valores = tuple(valores)
    if len(chaves) <= 0:
        return Response(status=204)
    with Banco() as banco:
        resultados = banco.consultar_produto(coluna=chaves, parametros=valores)
    

    lista = []
    for tupla in resultados:
        produto = {"id": tupla[0], "nome": tupla[1], "quantidade": tupla[2], "ativo": tupla[3], "data_recebimento": tupla[4], "id_fornecedor": tupla[5]}
        lista.append(produto)

    return jsonify(lista), 200

@app.route('/api/cadastrar_produto', methods=['POST'])
def cadastrar_produto():
    json = request.get_json()
    
    nome = json.get('nome')
    quantidade = json.get('quantidade')
    ativo = json.get('ativo')
    data_recebimento = json.get('data_recebimento')
    endereco = json.get('id_fornecedor')

    with Banco() as banco:
        banco.cadastrar_produto(nome, quantidade, ativo, data_recebimento, endereco)

    return jsonify({"mensagem": "Sucesso"}), 204

@app.route('/api/editar_produto', methods=['POST'])
def editar_produto():
    dados = request.get_json()

    with Banco() as banco:
        response = banco.editar_produto(dados)
        if response:
            return Response(response='200')
        else:
            return Response(response='401')

@app.route('/api/adicionar_venda', methods=['POST'])
def adicionar_venda():
    dados = request.get_json()  
    dados = [dados.get('id_produto'), int(dados.get('quantidade')), int(dados.get('venda_unitaria')), dados.get('data_venda')]
    with Banco() as banco:
        banco.adicionar_venda(dados)
    
    return Response(response='200')

@app.route('/api/consultar_vendas', methods=['GET'])
def consultar_vendas():
    from datetime import datetime

    with Banco() as banco:
        resultados = banco.consultar_vendas()
    lista = []
    for dado in resultados:
        dado = list(dado)
        produto = {"id": dado[0], "id_produto": dado[1], "nome_produto": dado[2], "quantidade_venda": dado[3], "venda_unitaria": dado[4], "data_venda": dado[5], "lucro": dado[6]}
        lista.append(produto)
    return jsonify(lista)

@app.route('/api/consultar_vendas', methods=['POST'])
def consultar_venda_parametros():
    dado = request.get_json()
    chaves = []
    valores = []
    for chave, valor in dado.items():
        if valor:
            chaves.append(f'{chave} LIKE ?')
            valores.append(f'%{valor}%')
    chaves = tuple(chaves)
    valores = tuple(valores)
    if len(chaves) <= 0:
        return Response(status=204)
    with Banco() as banco:
        resultados = banco.consultar_vendas(coluna=chaves, parametros=valores)
    
    lista = []
    for tupla in resultados:
        produto = {"id": tupla[0], "id_produto": tupla[1], "nome_produto": tupla[2], "quantidade_venda": tupla[3], "venda_unitaria": tupla[4], "data_venda": tupla[5], "lucro": tupla[6]}
        lista.append(produto)

    return jsonify(lista), 200

@app.route('/api/editar_venda', methods=['PATCH'])
def editar_venda():
    dados = request.get_json()

    with Banco() as banco:
        response = banco.editar_venda(dados)
        if response:
            return Response(response='200')
        else:
            return Response(response='401')

@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    with Banco() as banco:
        lista = banco.dashboard()
    
    return jsonify(lista)

if __name__ == '__main__':
    app.run(debug=True)