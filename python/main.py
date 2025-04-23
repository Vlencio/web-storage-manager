from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from banco import Banco

app = Flask(__name__)
CORS(app)

@app.route('/api/cadastrar', methods=['POST'])
def cadastro():
    dados = request.get_json()
    email = dados.get('email')
    usuario = dados.get('usuario')
    senha = dados.get('senha')
    with Banco() as banco:
        banco.cadastrar(email, usuario, senha)

    return jsonify({"mensagem": "Sucesso!"}), 201

@app.route('/api/login', methods=['POST'])
def logar():
    dados = request.get_json()
    email = dados.get('email')
    senha = dados.get('senha')
    with Banco() as banco:
        res = banco.login(email, senha)
    if res:
        return jsonify({"mensagem": "Logado"}), 200

    return jsonify({"mensagem": "Login inválido"}), 401

@app.route('/api/consultar_fornecedor', methods=['GET'])
def consultar_fornecedor():
    
    banco = Banco()
    resultados = banco.consultar_fornecedor()

    lista = []
    for tupla in resultados:
        fornecedor = {"id": tupla[0], "nome": tupla[1], "cnpj": tupla[2], "telefone": tupla[3], "email": tupla[4], "endereco": tupla[5]}
        lista.append(fornecedor)
    
    return jsonify(lista)

@app.route('/api/consultar_fornecedor', methods=['POST'])
def consultar_fornecedor_parametros():
    dados = request.get_json()
    chaves = []
    valores = []
    for chave, valor in dados.items():
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
def adicionar_fornecedor():
    json = request.get_json()
    
    nome = json.get('nome')
    cnpj = json.get('cnpj')
    telefone = json.get('telefone')
    email = json.get('email')
    endereco = json.get('endereço')

    with Banco() as banco:
        banco.cadastrar_fornecedor(nome, cnpj, telefone, email, endereco)

    return jsonify({"mensagem": "Sucesso"}), 200



if __name__ == '__main__':
    app.run(debug=True)