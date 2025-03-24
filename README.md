# API Livros Vai Na Web

## Sobre o Projeto
A API **Livros Vai Na Web** é um sistema simples para cadastro e listagem de livros, permitindo que os usuários doem livros com informações como título, categoria, autor e uma URL de imagem. A API foi desenvolvida utilizando **Flask** e **SQLite**.

## Tecnologias Utilizadas
- **Python 3**
- **Flask** (Framework Web)
- **SQLite** (Banco de Dados)

## Instalação e Configuração
### 1. Clone o repositório
```bash
git clone https://github.com/DevsAndresa/LivrosVainaWeb.git
```
### 2. Acesse o diretório do projeto
```bash
cd LivrosVainaWeb
```
### 3. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```
### 4. Instale as dependências
```bash
pip install flask
```
### 5. Execute a aplicação
```bash
python app.py
```
A API estará rodando em **http://127.0.0.1:5000**.

## Endpoints

### 1. **Cadastrar um livro**
**POST /doar**
- Adiciona um novo livro ao banco de dados.
- **Formato da requisição (JSON):**
  ```json
  {
    "titulo": "Nome do Livro",
    "categoria": "Categoria do Livro",
    "autor": "Nome do Autor",
    "image_url": "URL da imagem do livro"
  }
  ```
- **Resposta de sucesso:**
  ```json
  {
    "mensagem": "Livro cadastrado com sucesso"
  }
  ```

### 2. **Listar todos os livros**
**GET /livros**
- Retorna uma lista de todos os livros cadastrados.
- **Resposta esperada:**
  ```json
  [
    {
      "id": 1,
      "titulo": "Nome do Livro",
      "categoria": "Categoria",
      "autor": "Nome do Autor",
      "image_url": "URL da imagem"
    }
  ]
  ```

## Estrutura do Banco de Dados
A API utiliza um banco de dados SQLite com uma tabela chamada **LIVROS**, contendo as seguintes colunas:
- `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `titulo` (TEXT, NOT NULL)
- `categoria` (TEXT, NOT NULL)
- `autor` (TEXT, NOT NULL)
- `image_url` (TEXT, NOT NULL)

## Considerações Finais
Esta API foi criada como parte do projeto **Livros Vai Na Web**. Fique à vontade para contribuir e sugerir melhorias!




