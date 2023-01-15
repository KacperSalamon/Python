from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.mediamarkt.pl/telefony-i-smartfony")

elements = driver.find_elements(By.CSS_SELECTOR, "[uid^='1973516']")

assert len(elements) >= 20

driver.quit()
