from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup


GOOGLE_FORM_URL = "https://forms.gle/nLCM4J2fUZXinRBC7"
ESTONIA_RENTS_URL = "https://www.kv.ee/?act=search.simple&deal_type=2&dt_select=2&county=1&search_type=new&parish=1061&price_max=450"

class Rents:
    def __init__(self):
        self.adresses = []
        self.prices = []
        self.urls = []

    def find_data(self):
        my_request = requests.get(url=ESTONIA_RENTS_URL)
        soup = BeautifulSoup(my_request.text, "html.parser")
        all_rents = soup.find_all(name="tr", class_="object-type-apartment object-item")
        for i in all_rents:
            self.adresses.append(i.find(name="a", class_="object-title-a text-truncate").getText().replace("  ", ""))
            self.prices.append(i.find(name="p", class_="object-price-value").getText().split()[0])
            self.urls.append(i.find(name="a", class_="object-title-a text-truncate").get("href"))


rents = Rents()
rents.find_data()

web = driver.get(GOOGLE_FORM_URL)
for i in range(len(rents.adresses)):
    time.sleep(3)
    adress = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    adress.send_keys(rents.adresses[i])
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(rents.prices[i])
    url = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url.send_keys(rents.urls[i])
    send_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    send_button.click()
    time.sleep(2)
    web = driver.get(GOOGLE_FORM_URL)
driver.quit()
