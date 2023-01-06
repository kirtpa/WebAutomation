import time

from selenium.webdriver.common.by import By

from WebAutomation.Src.PageObject.Locators import Locator

class Element(object):

    def __init__(self, driver):
        self.driver = driver

# home page locators defining
        self.userName = driver.find_element(By.XPATH, Locator.userName)
        self.password = driver.find_element(By.ID, Locator.passWord)

    def setUserName(self,Name):
        self.userName.clear()
        self.userName.send_keys(Name)
        time.sleep(30)

    def setpassword(self,value):
        self.password.clear()
        self.password.send_keys(value)
        time.sleep(30)

