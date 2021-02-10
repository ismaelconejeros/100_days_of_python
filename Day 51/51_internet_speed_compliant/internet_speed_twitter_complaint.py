from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 199.50
        self.up = 56.24
        self.get_internet_speed()

    def get_internet_speed(self):
        driver.get("https://www.speedtest.net/")
        time.sleep(5)
        button_go = driver.find_element_by_css_selector(".start-button a")
        button_go.click()
        time.sleep(45)
        dismiss = driver.find_element_by_link_text("Back to test results")
        dismiss.click()
        speed_data_object = driver.find_element_by_class_name("result-container-data")
        speed_data = speed_data_object.text.split("\n")
        self.down = float(speed_data[3])
        self.up = float(speed_data[5])
        driver.quit()

    def tweet_at_provider(self):
        driver.get("https://twitter.com/")
        time.sleep(5)
        login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login.click()
        time.sleep(5)
        email = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASSWORD)
        login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span')
        login.click()
        time.sleep(5)
        new_tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        new_tweet.click()
        text = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        text.send_keys(f"PYTHON BOT TEST - DOWNLOAD_SPEED: {self.down} - UPLOAD_SPEED: {self.up}")
        send_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span')
        send_button.click()


app = InternetSpeedTwitterBot()

if app.down < PROMISED_DOWN:
    app.tweet_at_provider()