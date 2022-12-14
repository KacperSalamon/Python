from ast import arguments
from telnetlib import WILL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5) #we wait to be sure that all website element will upload


def checkCorrectData():
    username = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    username.send_keys("Admin")
    password = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    password.send_keys("admin123")
    password.send_keys(Keys.RETURN)
    
def backToLoginPage():
    infoBar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i")
    infoBar.click()
    logout = driver.find_element(By.CSS_SELECTOR, 'a[role="menuitem"]')
    logout.click()
    
def checkWrongData():
    wrongUsername = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    wrongUsername.send_keys("admin")
    wrongPassword = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    wrongPassword.send_keys("admin123")
    wrongPassword.send_keys(Keys.RETURN)
    #field validation let in me to page - this bug has been reported here https://github.com/MajkWazowski/Bug-Report/blob/main/Zg%C5%82oszenie%20b%C5%82%C4%99du%20-%20OrangeHRM.docx
    
def randomData():
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = upper_case.lower()
    number = "0123456789"
    special_characters = "!@#$%^&*_-\/?"
    concatPass = upper_case + lower_case + number + special_characters
    concatUsername = upper_case + lower_case
    lefForUsername = 5
    lenForPass = 10
    username = "".join(random.sample(concatUsername, lefForUsername))
    password = "".join(random.sample(concatPass, lenForPass))
    
    randomUsername = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    randomUsername.send_keys(username)
    randomPass = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    randomPass.send_keys(password)
    loginButton = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    loginButton.click()
    
invalidData = driver.find_element(By.CSS_SELECTOR, 'div[role="alert"]')

if invalidData == True:
    checkCorrectData()

def searchEmployees():
    employess = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input")
    employess.send_keys("0038")
    employessButton = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    employessButton.click()
    
def deleteUser():
    delete = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/button[1]")
    delete.click()
    yesDelete = driver.find_element(By.LINK_TEXT, "Yes, Delete")
    yesDelete.click()
    searchEmployees() #verifing that we can not search deleted user
    
def verifyUserTime():
    searchTime = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a")
    searchTime.click()
    inputUserTime = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]')
    inputUserTime.send_keys("Charlie Carter")
    clickButton = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    clickButton.click() 
    #Wrong field validation - we can not search user data with out choose page hints. Reported to DEV TEAM.
    
def verifyLeftBarSearch():
    leftBarSearch = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search"]')
    leftBarSearch.send_keys("My Info")
    leftBarSearch.send_keys(Keys.RETURN)#nothing change - we must choose from the search-list
    myInfo = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li/a")
    myInfo.click()
    
def addNickName():
    nickname = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input")
    nickname.send_keys("Test Boy")
    save = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button")
    driver.execute_script("arguments[0].scrollIntoView();", save)
    save.save_screenshot('nickName' + str(random.randint(0,101)) + '.png')
    
def dashBoardPage():
    dashBoard = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]")
    dashBoard.click()
    
def getCookies():
    cookies = driver.get_cookies()
    cookies_dict = {}
    for cookie in cookies:
        cookies_dict[cookie["name"]] = cookie["value"]
    print(cookies_dict)

def checkTime():
    time = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a")
    time.click()
    clock = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/button")
    clock.click()
    calendar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/i")
    calendar.click()
    chooseDay = driver.find_element(By.LINK_TEXT, "Today")
    chooseDay.click()
    hourInput = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/input")
    hourClick = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[1]/i")
    
    while hourInput.text != "20" :
        hourClick.click()
    
    minutesClick = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/i[1]")
    minutesInput = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/input")
    
    while minutesInput.text != "05" :
        minutesClick.click()
     
    comment = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/form/div[2]/div/div/div/div[2]/textarea")
    comment.send_keys("Extra work for client")
    outBtn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    outBtn.click()
    
def logOut():
    dropDownBar = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li")
    action = ActionChains(driver)
    action.move_to_element(dropDownBar).perform()
    finish = driver.find_element(By.LINK_TEXT, "Logout")
    finish.click()
    
def closePage():
    driver.close()  
