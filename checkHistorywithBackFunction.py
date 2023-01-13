from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com/page1")

driver.get("https://example.com/page2")

driver.back()

assert driver.current_url == "https://example.com/page1"

driver.forward()

assert driver.current_url == "https://example.com/page2"

driver.quit()
