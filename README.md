# Stock Price Alert System

Este projeto implementa um sistema de alerta de preço de ações que monitora as variações de preço das ações da IBM e envia um e-mail com notícias relevantes caso haja uma variação superior a 5%.

## Funcionalidades

- Monitoramento das variações percentuais no preço das ações da IBM.
- Utilização da API Alpha Vantage para obter dados históricos de preço das ações.
- Utilização da API News API para obter notícias relacionadas à IBM.
- Envio de e-mails automáticos com notícias relevantes em caso de variação de preço superior a 5%.

## Pré-requisitos

- Python 3.12
- Bibliotecas Python: `requests`, `smtplib`
- Conta na Alpha Vantage (para a chave de API) e na News API (para a chave de API).

## Configuração e Execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/stock-price-alert.git
   cd stock-price-alert


2. Instale as dependências:
   pip install requests

3.Configure as chaves de API:

  Obtenha uma chave de API da Alpha Vantage em Alpha Vantage API.
  Obtenha uma chave de API da News API em News API.

4.Insira suas chaves de API no arquivo main.py:
  api_key_alpha_vantage = "sua_chave_api_alpha_vantage"
  api_key_news_api = "sua_chave_api_news_api"

5.Execute o script principal:
  python main.py

Detalhes do Código
Monitoramento de Variações de Preço
O script main.py realiza as seguintes etapas:

Obtém os preços de fechamento das ações da IBM nos últimos dois dias úteis.
Calcula a diferença percentual entre os preços de fechamento desses dias.
Se a diferença percentual for maior ou igual a 5%, utiliza a API News API para buscar as três primeiras notícias relacionadas à IBM naquele dia.
Envia um e-mail contendo as notícias encontradas.






