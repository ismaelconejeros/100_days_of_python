from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.python.org/")

events_xpath = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div')
events = events_xpath.text.split("\n")[2:]

events_dict = {}
for i in range(len(events)):
    if i%2 == 0:
        events_dict[i//2] = {
            "time" : events[i],
            "name" : events[i+1]
        }

print(events_dict)

driver.close()