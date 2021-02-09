from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.common.exceptions import NoSuchElementException
import time

MY_EMAIL = "isma.conejeros@gmail.com    "
MY_PASS = "C0n3j3r051"
PHONE = "56954405745"

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

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        
        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
