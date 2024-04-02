from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

DRIVER_PATH = "./Drivers/chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://www.python.org/")

all_elements = driver.find_elements(By.XPATH, "(//div[@class='shrubbery'])[2]//ul[@class='menu']//li")
dates = []
for each_elemnt in all_elements:
    event_date = {}
    time = each_elemnt.find_element(By.TAG_NAME, 'time').text
    event = each_elemnt.find_element(By.TAG_NAME, 'a').text
    event_date[time] = event
    dates.append(event_date)
print(dates)
driver.quit()
