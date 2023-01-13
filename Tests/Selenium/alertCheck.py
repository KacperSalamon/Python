from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com/alerts")

alert_button = driver.find_element(By.ID, "alert_button")
alert_button.click()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()

alert_message = driver.find_element(By.ID, "alert_message")
assert alert_message.text == "Alert accepted!"

driver.quit()
