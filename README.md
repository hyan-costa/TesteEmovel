# Projeto avaliativo

## Rodando a Aplicação

1. Clone o repositório 
2. Crie o ambiente virtual: `python3 -m venv venv`
3. Ative o ambiente virtual: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Adicione as variaveis de ambiente no .env_example e depois renomeie o arquivo para .env: 
6. Inicie o servico no conatiner com postgreSQL: ` cd docker/ && docker compose --env-file ../.env up -d && cd -`
7. Execute a aplicação: `cd app && flask run`

## Rodando os Testes

1. Certifique-se de que a aplicação está parada
2. Execute os testes: `pytest app/tests`


## Documentação da API

## 1. Criar Cliente
- **URL:** `/customers`
- **Método:** `POST`
- **Parâmetros:**
  - `name` (string): Nome do cliente.
  - `email` (string): Endereço de e-mail do cliente.
- **Exemplo de Uso:**
  ```bash
  curl -X POST -d "name=NomeDoCliente&email=email@dominio.com" http://seu-domino/customers
  

## 2.Obter Cliente


*   **URL:** `/customers/<int:customer_id>`
*   **Método:** `GET`
*   **Parâmetros:**
    *   `customer_id` (int): ID do cliente.

## Aprovar Tíquete do Cliente

- **URL:** `/customers/<int:customer_id>/approve_ticket/<int:ticket_id>`
- **Método:** `POST`
- **Parâmetros:**
  - `customer_id` (int): ID do cliente.
  - `ticket_id` (int): ID do tíquete a ser aprovado.
- **Exemplo de Uso:**
  ```bash
  curl -X POST http://seu-domino/customers/1/approve_ticket/123
  
## 3.Fechar Tíquete por Cliente

- **URL:** `/customers/<int:customer_id>/close_ticket/<int:ticket_id>`
- **Método:** `POST`
- **Parâmetros:**
  - `customer_id` (int): ID do cliente.
  - `ticket_id` (int): ID do tíquete a ser fechado.
- **Exemplo de Uso:**
  ```bash
  curl -X POST http://seu-domino/customers/1/close_ticket/123


## 4. Obter Suporte

- **URL:** `/supports/<int:support_id>`
- **Método:** `GET`
- **Parâmetros:**
  - `support_id` (int): ID do suporte.
- **Exemplo de Uso:**
  ```bash
  curl http://seu-domino/supports/1
  

 ## 5. Criar Suporte

- **URL:** `/supports`
- **Método:** `POST`
- **Parâmetros:**
  - `name` (string): Nome do suporte.
  - `email` (string): Endereço de e-mail do suporte.
  - `ranking` (int): Classificação do suporte.
- **Exemplo de Uso:**
  ```bash
  curl -X POST -d "name=NomeDoSuporte&email=email@dominio.com&ranking=5" http://seu-domino/supports 

## 6. Aceitar Tíquete

- **URL:** `/supports/<int:support_id>/accept_ticket/<int:ticket_id>`
- **Método:** `POST`
- **Parâmetros:**
  - `support_id` (int): ID do suporte.
  - `ticket_id` (int): ID do tíquete a ser aceito.
- **Exemplo de Uso:**
  ```bash
  curl -X POST http://seu-domino/supports/1/accept_ticket/123
  

## 7. Fechar Tíquete por Suporte

- **URL:** `/supports/<int:support_id>/close_ticket/<int:ticket_id>`
- **Método:** `POST`
- **Parâmetros:**
  - `support_id` (int): ID do suporte.
  - `ticket_id` (int): ID do tíquete a ser fechado.
- **Exemplo de Uso:**
  ```bash
  curl -X POST http://seu-domino/supports/1/close_ticket/123
  


## 8. Obter Tíquete

- **URL:** `/tickets/<int:ticket_id>`
- **Método:** `GET`
- **Parâmetros:**
  - `ticket_id` (int): ID do tíquete.
- **Exemplo de Uso:**
  ```bash
  curl http://seu-domino/tickets/123
  


## 9. Criar Tíquete

- **URL:** `/tickets`
- **Método:** `POST`
- **Parâmetros:**
  - `title` (string): Título do tíquete.
  - `description` (string): Descrição do tíquete.
- **Exemplo de Uso:**
  ```bash
  curl -X POST -d "title=TítuloDoTíquete&description=DescriçãoDoTíquete" http://seu-domino/tickets
