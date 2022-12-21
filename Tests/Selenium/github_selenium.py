from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://github.com/")
driver.maximize_window()
driver.get_screenshot_as_png()

def login():
    signIn = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a")
    signIn.click()
    inputName = driver.find_element(By.ID, "login_field")
    inputName.send_keys("kacpersalamon1707@gmail.com")
    inputPass = driver.find_element(By.ID, "password")
    inputPass.send_keys("********") #Sorry but I can't show you my password, but in this line you should in brackets the correct password
    login = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    login.accessible_name
    time.sleep(2)
    
def details():
    myFace = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[7]/details/summary")
    myFace.click()
    myRepo = driver.find_element(By.CSS_SELECTOR, 'a[role="menuitem"]')
    myRepo.click()
    time.sleep(2)
    
def setNewSuggestList():
    suggestList = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div[2]/div/div[2]/turbo-frame/div/div[2]/ul/li[3]/div[2]/div[1]/div[2]/details/summary/svg")
    suggestList.click()
    inspiration = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div[2]/div/div[2]/turbo-frame/div/div[2]/ul/li[3]/div[2]/div[1]/div[2]/details/details-menu/div/div/div/div/div/div/form/div/div[3]/label/input")
    inspiration.click()

def editProfile():
    edit = driver.find_element(By.CSS_SELECTOR, 'button[name="button"]')
    edit.click()
    name = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div[2]/div/div[1]/div/div[2]/div[3]/div[1]/form/div[1]/input")
    name.send_keys("Kacper Salamon")
    copyName = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div[2]/div/div[1]/div/div[2]/div[3]/div[1]/form/div[1]/input")
    copyName.send_keys(Keys.CONTROL, "a")
    copyName.send_keys(Keys.CONTROL, "c")
    bio = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div[2]/div/div[1]/div/div[2]/div[3]/div[1]/form/div[2]/text-expander/textarea")
    bio.send_keys("Hello my name is " + copyName + " and I learn Selenium/Python :)")
    time = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    time.click()
    save = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    save.click()
    
def emoji():
    setStatus = driver.find_element(By.CLASS_NAME, "g-emoji")
    setStatus.click()
    time.sleep(1) #we sleep time because the class name & element will not change in HTML, so I slept for 1s and setStatus will be click again BUT already in Box
    setStatus.click() 
    filterEmoji = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/details/details-dialog/form/div[2]/emoji-picker/tab-container/div/div[1]/input")
    filterEmoji.send_keys("Snake")
    snakeEmoji = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/details/details-dialog/form/div[2]/emoji-picker/tab-container/div/div[12]/fuzzy-list/ul/li[1]/button/g-emoji")
    snakeEmoji.double_click()
    confirmStatus = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/details/details-dialog/form/div[3]/button[1]")
    confirmStatus.click()

def pythonRepo():
    element1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[3]/div[3]/div[1]/div[9]")
    element2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[3]/div[3]/div[1]/div[8]")
    action = ActionChains(driver)
    action.drag_and_drop(element1, element2) #this action will not work - we couldn't drag and drop ONE script/file to another inside
    
#to be continue :)

