# Projeto avaliativo

## Rodando a Aplicação

1. Clone o repositório 
2. Instale as dependências: `pip install -r requirements.txt`
2. Adicione as variaveis de ambiente no .env_example e depois renomeie o arquivo para .env: 
2. Inicie o servico no conatiner com postgreSQL: ` cd docker/ && docker compose --env-file ../.env up -d && cd -`
3. Execute a aplicação: `python app/app.py`

## Rodando os Testes

1. Certifique-se de que a aplicação está parada
2. Execute os testes: `pytest app/tests`
