from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = "./Drivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.implicitly_wait(10)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.find_element(By.CSS_SELECTOR, "#promptContentChangeLanguage .title").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "bigCookie")))
for i in range(200):
    driver.find_element(By.ID, "bigCookie").click()

driver.quit()
