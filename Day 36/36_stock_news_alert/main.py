import requests
from newsapi import NewsApiClient
from datetime import date, timedelta
import smtplib
import email.mime.text

STOCK = "BTC"

yesterday = str(date.today() - timedelta(days=1))
yesterday_2 = str(date.today() - timedelta(days=3))

#PRICE
API_KEY_STOCKS = "E1O0556ZE113BJG3"
ALPHAVENTAGE = 'https://www.alphavantage.co/query?'
PARAMETRES = {
    "function" : "DIGITAL_CURRENCY_DAILY",
    "symbol": STOCK,
    "market" : "USD",
    "apikey": API_KEY_STOCKS
}
my_request = requests.get(ALPHAVENTAGE, params=PARAMETRES)
data = my_request.json()
coin_open = float(data["Time Series (Digital Currency Daily)"][yesterday]["1a. open (USD)"])
coin_close = float(data["Time Series (Digital Currency Daily)"][yesterday]["4a. close (USD)"])
coin_volume = float(data["Time Series (Digital Currency Daily)"][yesterday]["5. volume"])

msg_price = f"{STOCK} Data {yesterday}\n\nOpen: {coin_open}\nClose: {coin_close}\nVolume: {coin_volume}.\n\n"

#NEWS
API_KEY_NEWS = "d4b9b1acbb1141e09ba4449f21822968"
newsapi = NewsApiClient(api_key=API_KEY_NEWS)
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param=yesterday_2,
                                      to=yesterday,
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
msg_urls = [f'{i+1} {all_articles["articles"][i]["title"]}\n{all_articles["articles"][i]["url"]}   -   ' for i in range(len(all_articles["articles"]))]

#MAIL
my_email = "test.for.smtplib90@gmail.com"
my_password = "smtplibtest01"
to_adress = "isma.conejeros@gmail.com"
msg_subject = f"BTC STATUS: {yesterday}"
msg_body1 = f"{msg_price} "
msg_body2 = "".join(msg_urls).encode('utf-8')
my_msg = f'Subject: {msg_body1}\n\n{msg_body2}'
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=to_adress, 
        msg=my_msg)