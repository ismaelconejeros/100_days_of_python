from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
import time

TARGET_ACCOUNT = ""
USERNAME = "@gmail.com"
PASSWORD = ""

class InstaFollower:
    def __init__(self):
        self.website = driver.get("https://www.instagram.com/")
        time.sleep(3)

    def login(self):
        email = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(USERNAME)
        password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        button.click()
        time.sleep(3)
        try:
            notifications_no = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            notifications_no.click()
        except:
            pass

    def find_followers(self, TARGET_ACCOUNT_funct):
        input_account = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        input_account.send_keys(TARGET_ACCOUNT_funct)
        time.sleep(3)
        first_result = driver.find_element_by_xpath(f'//a[@href="/{TARGET_ACCOUNT_funct}/"]')
        first_result.click()
        time.sleep(3)
        account_followers = driver.find_element_by_xpath(f'//a[@href="/{TARGET_ACCOUNT_funct}/followers/"]')
        account_followers.click()
        time.sleep(3)

    def follow(self):
        for i in range(1,100):
            try:
                time.sleep(3)
                follow_button = driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/ul/div/li[{i}]/div/div[3]/button')
                follow_button.click()
                scroll = driver.execute_script("window.scrollTo(0, 10)")
            except:
                pass

app = InstaFollower()
app.login()
app.find_followers(TARGET_ACCOUNT)
app.follow()