#New App Instgram

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstgramBot:

    def __init__(self,username , password) :
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        
        self.login()



    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(10)
        
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()




if __name__ == '__main__' :
    ig_bot = InstgramBot('My User name' , 'My Password')
