import requests
from bs4 import BeautifulSoup
import lxml

AMAZON_PRODUCT = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
ACCEPT_LANGUAGE = "es-419,es;q=0.9,en;q=0.8"

my_request = requests.get(url=AMAZON_PRODUCT, headers = {"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGUAGE})
response = my_request.text
soup = BeautifulSoup(response, "lxml")
price = float(soup.find(id="priceblock_ourprice").getText().split("$")[1])


# LIMIT_PRICE = 100
# if price <= LIMIT_PRICE:
#     #Send Mail
#     pass