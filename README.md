[README.md times.md](https://github.com/user-attachments/files/23346392/README.md.times.md)
# API de time - WebAPI

Está é uma API RESTful desenvolvida para o gerenciamento de informações de time, utilizando **python** e **java**. A API permite criar, ler, atualizar e excluir time, com validação dos dados utilizando a biblioteca **Joi**.

Este é um projeto inicial de CRUD (Create, Read, Update, Delete),que será expandido no futuro. Este é apenas o escopo inical.

## Funcionalidades

- **GET /**: Retorna a lista completa de titulo.
- **GET /:sigla**: Retorna as informações de um time específico, identificado pela sigla
- **POST /**: Adiciona um novo time à lista.
- **PUT /:sigla**: Atualiza as informações de um time específico, identificado pela sigla.
- **DELETE /:sigla**: Remove um time específico pela sigla.

## Estrutura do Projeto

- **app.js**: Arquivo principal que configura o servidor Express e as rotas da API.
- **tabelatime.js**: Contém a lista de time (dados fictícios).
- **validacao.js**: Contém as validações Joi para os dados dos time.

## Endpoints

### 1. **GET /**

Retorna a lista completa de time disponíveis.

#### Exemplo de Resposta:

```json
[
  {
    "titulo": "Campeonato Brasileiro",
    "liga": "Serie A",
    "jogadores": 28,
    "clube": "Flamengo",
    "titulos_ganhos": 45,
    "fundacao": "15/11/1895",
    "pais": "Brasil"
  },
  {
    "titulo": "Libertadores",
    "liga": "Conmebol",
    "jogadores": 30,
    "clube": "Palmeiras",
    "titulos_ganhos": 35,
    "fundacao": "26/08/1914",
    "pais": "Brasil"
  }
]
```
### 2. **GET /:sigla**

Retorna as informações de um time específico, identifado pela sigla.

### Exemplo de Requisição:

`GET /Fla`

### Exemplo de Resposta:

```json
{
    {
  "titulo": "Campeonato Brasileiro",
  "liga": "Série A",
  "jogadores": 28,
  "clube": "Flamengo",
  "titulos_ganhos": 45,
  "fundacao": "15/11/1895",
  "pais": "Brasil"
}

}
```
### 3. **POST /**

Adiciona um novo time à lista.

#### Exemplo de Requisição:

`POST \`

**Content-Type:** application/json

```json
{
  "titulo": "Copa do Brasil",
  "liga": "Serie A",
  "jogadores": 27,
  "clube": "Corinthians",
  "titulos_ganhos": 30,
  "fundacao": "01/09/1910",
  "pais": "Brasil"
}
```

#### Exemplo de Resposta:

```json
{
    "titulo": "Copa do Brasil",
  "liga": "Serie A",
  "jogadores": 27,
  "clube": "Corinthians",
  "titulos_ganhos": 30,
  "fundacao": "01/09/1910",
  "pais": "Brasil"
}
```

### 4. **PUT /:sigla**

Atualiza as informações de um carro específico.

#### Exemplo de Requisição:

`PUT /COR`

**Content-Type:** application/json

```json
{
  "titulo_ganhos": 31
}
```

#### Exemplo de resposta:

```json
{
     "titulo": "Copa do Brasil",
  "liga": "Série A",
  "jogadores": 27,
  "clube": "Corinthians",
  "titulos_ganhos": 31,
  "fundacao": "01/09/1910",
  "pais": "Brasil"
}
```

### 5. **DELETE /:sigla**

Remove um time específico pela sigla.

#### Exemplo de Requisição:

`DELETE /COR`

#### Exemplo de Resposta:

```json
{
    "titulo": "Copa do Brasil",
  "liga": "Série A",
  "jogadores": 27,
  "clube": "Corinthians",
  "titulos_ganhos": 31,
  "fundacao": "01/09/1910",
  "pais": "Brasil"
}
```

## Como Rodar o Projeto

1. **Clone este repositório:**

  ```bash
  git clone https://github.com/ZkJon77/Times
  ```

2. **Instale as dependências:**

  Navegue até o diretório do projeto e execute o comando:

  ```bash
  npm install
  ```
3. **Inicie o servidor**
  Após a instalação das dependências, inicie o servidor:

  ```bash
  node ./app.js
  ```
4. **Acesse a API**

A API está disponível em [http://localhost:3000]

## Validações 

Os dados enviados para API são validados com **Joi** para garantir que todos os campos sejam fornecidos corretamente. As validações incluem:

- O nome do time deve ter pelo menos 3 caracteres.
- A Sigla deve ter exatamente 3 caracteres.
- A potência, titulos máximo ilimitado, consumo, valor de clube e preço de jogadores devem ser números válidos.
- Durante a atualização, pelo menos um campo precisa ser fornecido.

Dicas:
https://dillinger.io/ - Para ler a formatação na Web, antes de subir no Git
https://readme.so/pt/editor - Para fazer "Automatico" somente editando

## Autor

Desenvolvido por Jonatan Viana Gomes
