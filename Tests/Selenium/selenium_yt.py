from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")

search_box = driver.find_element_by_name("search_query")

search_box.send_keys("Selenium tutorial")

search_box.send_keys(Keys.RETURN)

results = driver.find_elements_by_css_selector(".yt-lockup-title > a")

assert len(results) > 0

driver.quit()
