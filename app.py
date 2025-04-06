import sqlite3  


from flask import Flask, request, jsonify  
from flask_cors import CORS


app = Flask(__name__)
CORS(app)





@app.route("/")
def mensagem_inicial():
    # Esta função retorna uma formatada em HTML, usando a tag <h2>
    return "<h2>Seja Bem Vindo!</h2>"

# 🔹 Criamos uma função chamada init_db() para inicializar o banco de dados
# Ela cria a tabela "LIVROS" caso ainda não exista, garantindo que o sistema esteja pronto para uso
def init_db():
    # Abrimos uma conexão com o arquivo "database.db" (cria o arquivo caso ele ainda não exista)
    # O "with" garante que a conexão será encerrada de forma segura após o uso
    with sqlite3.connect("database.db") as conn:
        # Executamos o comando SQL que cria a tabela LIVROS com os campos necessários
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    titulo TEXT NOT NULL,                 
                    categoria TEXT NOT NULL,              
                    autor TEXT NOT NULL,                  
                    image_url TEXT NOT NULL               
                )
            """
        )  

# Chamamos a função init_db() para garantir que o banco esteja criado ao iniciar o servidor
init_db()

# 🔹 Criamos a rota "/doar" para permitir que um novo livro seja cadastrado via método POST
@app.route("/doar", methods=["POST"])
def doar():
    # Pegamos os dados enviados pelo cliente no formato JSON e exibimos no terminal para fins de teste
    dados = request.get_json()
    print(f" AQUI ESTÃO OS DADOS RETORNADOS DO CLIENTE {dados}")

    # Extraímos cada campo do JSON enviado
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    # Verificamos se algum dos campos obrigatórios está vazio
    if not titulo or not categoria or not autor or not image_url:
        # Se faltar algum dado, retornamos um erro 400 com uma mensagem explicando o problema
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    # Conectamos ao banco de dados usando a variável conn
    with sqlite3.connect("database.db") as conn:
        # Executamos um comando SQL para inserir os dados na tabela LIVROS
        conn.execute(f"""
                    INSERT INTO LIVROS (titulo,categoria,autor,image_url)
                    VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
        """)

        # Salvamos as mudanças com commit()
        conn.commit()

        # Retornamos uma mensagem confirmando o cadastro com status 201 (Created)
        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

# 🔹 Criamos a rota "/livros" para listar todos os livros cadastrados no banco
@app.route("/livros", methods=["GET"])
def listar_livros():
    # Conectamos ao banco de dados
    with sqlite3.connect("database.db") as conn:
        # Buscamos todos os registros da tabela LIVROS
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        # Criamos uma lista vazia para armazenar os livros formatados
        livros_formatados = []

        # Para cada livro encontrado, transformamos os dados em um dicionário
        for item in livros:
            dicionario_livros = {
                "id": item[0],            # ID do livro
                "titulo": item[1],        # Título
                "categoria": item[2],     # Categoria
                "autor": item[3],         # Autor
                "image_url": item[4]      # URL da imagem
            }
            # Adicionamos o dicionário à lista
            livros_formatados.append(dicionario_livros)

    # Retornamos todos os livros em formato JSON com status 200 (OK)
    return jsonify(livros_formatados)

# 🔹 Verificamos se este arquivo está sendo executado diretamente
# Isso evita que o servidor Flask rode se o arquivo for apenas importado
if __name__ == "__main__":
    # Iniciamos o servidor Flask em modo debug
    # O modo debug mostra erros detalhados e recarrega o servidor automaticamente ao salvar o arquivo
    app.run(debug=True)
