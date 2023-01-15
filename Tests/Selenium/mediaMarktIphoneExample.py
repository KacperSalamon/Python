from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.mediamarkt.pl/")

product_link = driver.find_element_by_link_text("Apple Iphone 13")
product_link.click()

add_to_cart_button = driver.find_element_by_css_selector("button[data-test='add-to-cart-button']")
add_to_cart_button.click()

cart_badge = driver.find_element_by_css_selector("span[data-test='cart-badge']")
product_count = int(cart_badge.text)

while product_count < 100:
    add_to_cart_button.click()
    product_count = int(cart_badge.text)

driver.quit()

#above code is JUST EXAMPLE and It will be not working on this form. If you want to work it, need to search correct XPATH, CSS_SELECTOR etc.
