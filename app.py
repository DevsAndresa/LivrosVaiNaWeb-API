import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa o CORS para habilitar o compartilhamento de recursos entre origens

# Criamos a aplicação Flask
app = Flask(__name__)

# Habilita CORS para toda a aplicação, permitindo todas as origens
CORS(app)

@app.route("/")
def home():
    return "<h2>Bem-vindo à API Livros Vai Na Web!</h2>"

# Função para inicializar o banco de dados SQLite
def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS LIVROS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                image_url TEXT NOT NULL 
            )
        """)

init_db()

@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()
    print(f"Dados recebidos do cliente: {dados}")  # Log para depuração

    # Validação dos dados recebidos
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    # Verifica se todos os campos obrigatórios estão presentes
    if not titulo or not categoria or not autor or not image_url:
        missing_fields = []
        if not titulo:
            missing_fields.append("titulo")
        if not categoria:
            missing_fields.append("categoria")
        if not autor:
            missing_fields.append("autor")
        if not image_url:
            missing_fields.append("image_url")
        
        return jsonify({"erro": f"Os seguintes campos estão ausentes: {', '.join(missing_fields)}"}), 400  

    try:
        # Inserção no banco de dados
        with sqlite3.connect("database.db") as conn:
            conn.execute("""
                INSERT INTO LIVROS (titulo, categoria, autor, image_url) 
                VALUES (?, ?, ?, ?)
            """, (titulo, categoria, autor, image_url))
            conn.commit()
        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados no banco: {e}")
        return jsonify({"erro": "Erro ao cadastrar livro, tente novamente mais tarde."}), 500

@app.route("/livros", methods=["GET"])
def listar_livros():
    try:
        with sqlite3.connect("database.db") as conn:
            livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []
        for item in livros:
            dicionario = {
                "id": item[0], 
                "titulo": item[1], 
                "categoria": item[2], 
                "autor": item[3], 
                "image_url": item[4]
            }
            livros_formatados.append(dicionario)

        return jsonify(livros_formatados), 200
    except sqlite3.Error as e:
        print(f"Erro ao listar livros: {e}")
        return jsonify({"erro": "Erro ao listar livros, tente novamente mais tarde."}), 500

if __name__ == "__main__":
    app.run(debug=True)
