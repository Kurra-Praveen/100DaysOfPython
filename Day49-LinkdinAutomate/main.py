from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.speedtest.net/")
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
driver.find_element(By.XPATH, "//span[text()='Go']").click()
