from flask import Flask, request, jsonify
from flask_cors import CORS
from banco import cadastrar, login

app = Flask(__name__)
CORS(app)

@app.route('/api/cadastrar', methods=['POST'])
def cadastro():
    dados = request.get_json()
    email = dados.get('email')
    usuario = dados.get('usuario')
    senha = dados.get('senha')
    cadastrar(email, usuario, senha)

    return jsonify({"mensagem": "Sucesso!"}), 201

@app.route('/api/login', methods=['POST'])
def logar():
    dados = request.get_json()
    email = dados.get('email')
    senha = dados.get('senha')
    res = login(email, senha)
    if res:
        return jsonify({"mensagem": "Logado"}), 200

    return jsonify({"mensagem": "Login inválido"}), 401


if __name__ == '__main__':
    app.run(debug=True)