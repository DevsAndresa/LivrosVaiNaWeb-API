# 📚 API Livros Vai Na Web

## 📖 Sobre o Projeto  
A API **Livros Vai Na Web** é um sistema simples para cadastro e listagem de livros, permitindo que os usuários doem livros informando **título**, **categoria**, **autor** e uma **URL da imagem** do livro.  
Desenvolvida com **Flask** e **SQLite**, essa API pode ser facilmente integrada com um frontend, como React.

---

## 🚀 Tecnologias Utilizadas  
- Python 3  
- Flask (Framework Web)  
- SQLite (Banco de Dados)

---

## ⚙️ Instalação e Configuração  

1. Clone o repositório:  
`git clone https://github.com/DevsAndresa/LivrosVaiNaWeb-API`

2. Acesse o diretório do projeto:  
`cd LivrosVainaWeb`

3. Crie um ambiente virtual (opcional, mas recomendado):  
- Linux/Mac: `source venv/bin/activate`  
- Windows: `venv\Scripts\activate`

4. Instale as dependências:  
`pip install -r requirements.txt`  
Se não existir o arquivo `requirements.txt`, crie com:  
`pip freeze > requirements.txt`

5. Execute a aplicação:  
`python app.py`  
A API estará rodando em: **http://127.0.0.1:5000**

---

## 📂 Estrutura de Arquivos

```
LivrosVaiNaWeb/
│
├── app.py                # Arquivo principal da aplicação Flask
├── database.db           # Banco de dados SQLite
├── requirements.txt      # Lista de dependências
└── README.md             # Documentação do projeto
```

---

## 📮 Endpoints da API

### 1. Cadastrar um livro  
**POST /doar**  
Adiciona um novo livro ao banco de dados.

**Formato da requisição (JSON):**

```json
{
  "titulo": "Nome do Livro",
  "categoria": "Categoria do Livro",
  "autor": "Nome do Autor",
  "image_url": "URL da imagem do livro"
}
```

**Resposta de sucesso:**

```json
{
  "mensagem": "Livro cadastrado com sucesso"
}
```

---

### 2. Listar todos os livros  
**GET /livros**  
Retorna todos os livros cadastrados.

**Exemplo de resposta:**

```json
[
  {
    "id": 1,
    "titulo": "Dom Casmurro",
    "categoria": "Romance",
    "autor": "Machado de Assis",
    "image_url": "https://m.media-amazon.com/images/I/41AYWyc6qmL._SY445_SX342_.jpg"
  }
]
```

---

## 🗃️ Estrutura do Banco de Dados

A API utiliza um banco de dados SQLite com a tabela **LIVROS**, contendo os seguintes campos:

- id (INTEGER, PRIMARY KEY, AUTOINCREMENT)  
- titulo (TEXT, NOT NULL)  
- categoria (TEXT, NOT NULL)  
- autor (TEXT, NOT NULL)  
- image_url (TEXT, NOT NULL)

---

## 🧪 Testando com Postman ou Insomnia

Você pode testar os endpoints usando o Postman, Insomnia ou qualquer ferramenta de requisição HTTP.

- Certifique-se de que a API está rodando em `http://127.0.0.1:5000`
- Use o método POST para `/doar` com o corpo JSON
- Use o método GET para `/livros` e veja a lista de livros cadastrados

---

## 🤝 Como Contribuir

1. Faça um fork do repositório  
2. Crie uma branch com sua feature (`git checkout -b minha-feature`)  
3. Commit suas alterações (`git commit -m 'feat: nova funcionalidade'`)  
4. Faça push para sua branch (`git push origin minha-feature`)  
5. Abra um Pull Request

---

## 🌐 Integração com Frontend

Esta API pode ser facilmente integrada com aplicações em **React** ou outras tecnologias frontend para exibir os livros cadastrados, suas imagens, categorias e autores.

---


## ✨ Considerações Finais

Este projeto foi desenvolvido como parte da formação **Full Stack - Vai Na Web**.  
Fique à vontade para colaborar, testar, sugerir e melhorar! 🚀
