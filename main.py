import requests
import smtplib
from datetime import datetime, timedelta



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

api_key = "JV6CHHBV6F00E36J"
symbol = "IBM"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(url)
response.raise_for_status()
data =response.json()



def get_previous_business_days(n):
    business_days = []
    date = datetime.now() - timedelta(1)
    while len(business_days) < n:
        if date.weekday() < 5:  # 0 é segunda-feira, 6 é domingo
            business_days.append(date.strftime('%Y-%m-%d'))
        date -= timedelta(1)
    return business_days

# Pegue as datas dos últimos dois dias úteis
last_two_business_days = get_previous_business_days(2)

# Pegue o preço de fechamento do último dia útil
last_business_day = last_two_business_days[0]
second_last_business_day = last_two_business_days[1]

try:
    close_price_last = float(data['Time Series (Daily)'][last_business_day]['4. close'])
    print(f"O preço de fechamento do último dia útil ({last_business_day}) para {symbol} foi: ${close_price_last}")
except KeyError:
    close_price_last = None
    print(f"Dados para {last_business_day} não estão disponíveis. Tente novamente mais tarde.")

# Pegue o preço de fechamento do penúltimo dia útil
try:
    close_price_second_last = float(data['Time Series (Daily)'][second_last_business_day]['4. close'])
    print(f"O preço de fechamento do penúltimo dia útil ({second_last_business_day}) para {symbol} foi: ${close_price_second_last}")
except KeyError:
    close_price_last = None
    print(f"Dados para {second_last_business_day} não estão disponíveis. Tente novamente mais tarde.")
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
if close_price_last is not None and close_price_second_last is not None:
    positive_difference = abs(close_price_last - close_price_second_last)
    print(f"A diferença positiva entre os preços de fechamento é: ${positive_difference}")
    percentage_difference = (positive_difference / close_price_second_last) * 100
    print(f"A diferença em porcentagem é: {percentage_difference:.2f}%")

    #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

    #TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

        ## STEP 2: https://newsapi.org/ 
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    api_noticia = "aa0bc3fbc6a64efb8b042c2296b7bc1c"
    query = "IBM"

    fonte = "https://newsapi.org/v2/everything"

    params = {
        'q': query,
        'sortBy': 'publishedAt',
        'pageSize': 3,
        'apiKey': api_noticia}


    #TODO 9. - Send each article as a separate message via Twilio. 

    response2= requests.get(fonte, params=params)

    data2 = response2.json()


    def diferença_grande():
        if data2['status'] == 'ok':
            articles = data2['articles']
            news_content = ""
            for i, article in enumerate(articles, 1):
                title = article['title']
                description = article['description']
                url = article['url']
                published_at = article['publishedAt']
                news_content += f"Notícia {i}:\n"
                news_content +=f"  Título: {title}\n"
                news_content +=f"  Descrição: {description}\n"
                news_content +=f"  URL: {url}\n"
                news_content +=f"  Publicado em: {published_at}\n\n"
                return news_content
        else:
            print("Erro ao buscar notícias:", data2['message'])
            return ""

    if 'percentage_difference' in locals() and percentage_difference >= 5:
        news_content = diferença_grande()
        if news_content:
            mensagem = f"suas ações da ibm tiveram um aumento considerável, aqui está o motivo:\n\n{news_content} "
            my_email = "gustavohqpasciano@gmail.com"
            password = "sepf rmmm gopd osoz"
            
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection. starttls()
                connection.login(user = my_email, password=password)
                connection.sendmail(from_addr= my_email, to_addrs= my_email,msg = f"Subject:Alerta de Ação\n\n{mensagem}".encode('utf-8'))
        else:
            print( "A sua ação não variou consideravelmente")
            mensagem2 = " As suas ações não variaram muito"
            my_email = "gustavohqpasciano@gmail.com"
            password = "sepf rmmm gopd osoz"
        
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection. starttls()
                connection.login(user = my_email, password=password)
                connection.sendmail(from_addr= my_email, to_addrs= my_email,msg = f"Subject:Alerta de Ação\n\n{mensagem2}".encode('utf-8') )
            
else:
    print("Não foi possível calcular a diferença devido à falta de dados.")