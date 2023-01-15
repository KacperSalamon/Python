from selenium import webdriver
from selenium.webdriver.common.by import By

def test_elements_have_id():
   
    driver = webdriver.Chrome()
 
    driver.get("https://www.mediamarkt.pl/")

    elements = driver.find_elements(By.XPATH, "//*")

    for element in elements:
        assert element.get_attribute("id") is not None

    driver.quit()
