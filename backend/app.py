from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': '127.0.0.1',
    'user': 'developer',
    'password': '@Pinheiro10',
    'database': 'dbteste',
    'port': '3306',
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# Rota para cadastro de usuário
@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    usuario = request.form.get('usuario')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    endereco = request.form.get('endereco')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    cep = request.form.get('cep')
    justificativa = request.form.get('justificativa')

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Usuario (Nome, Tipo, Endereco, Cidade, Estado, CEP, Email, Telefone, Justificativa)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (usuario, "Doador", endereco, cidade, estado, cep, email, telefone, justificativa))
        conn.commit()
        return redirect(url_for('success'))
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Rota para cadastro de tinta
@app.route('/cadastrar_tinta', methods=['POST'])
def cadastrar_tinta():
    nome = request.form.get('nome')
    tipo = request.form.get('tipo')
    cor = request.form.get('cor')
    acabamento = request.form.get('acabamento')
    quantidade = request.form.get('quantidade')
    validade = request.form.get('validade')
    foto = request.form.get('foto')
    condicao = request.form.get('condicao')

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Tinta (nome,tipo, cor, acabamento, quantidade, validade, foto, condicao)
            VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
        """, (nome,tipo, cor, acabamento, quantidade, validade, foto, condicao))
        conn.commit()
        return redirect(url_for('success'))
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Rota de sucesso
@app.route('/success')
def success():
    return "Cadastro realizado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
