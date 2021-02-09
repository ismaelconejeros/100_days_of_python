from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.common.exceptions import NoSuchElementException
import time

MY_EMAIL = ""
MY_PASS = ""

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=92000000&keywords=python%20developer&location=Worldwide")

login = driver.find_element_by_xpath("/html/body/header/nav/div/a[2]")
login.click()

time.sleep(3)

email = driver.find_element_by_id('username')
email.send_keys(MY_EMAIL)
password = driver.find_element_by_id('password')
password.send_keys(MY_PASS)
signin = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
signin.click()

time.sleep(3)

jobs_list = driver.find_elements_by_css_selector(".jobs-search-results__list li")
for i in jobs_list:
    i.click()
    apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
    apply_button.click()
    submit = driver.find_element_by_css_selector(".display-flex button")
    multi_q = True
    while multi_q:
        try:
            submit.click()
            time.sleep(3)
        except NoSuchElementException:
            pass


driver.close()