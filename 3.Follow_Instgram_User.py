#New App Instgram

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstgramBot:

    def __init__(self,username , password) :
        '''
        Args:
            usernme:str 


        '''
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Firefox()

        self.login()



    def login(self):
        self.driver.get('{}/accounts/login/?source=auth_switcher'.format(self.base_url))
        time.sleep(10)
        
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()

        time.sleep(2)

    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url , user))
        

    def follow_user(self,user):
        self.nav_user(user)

        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0]  # ---> For Unfollow Write Following
        follow_button.click()


if __name__ == '__main__' :
    ig_bot = InstgramBot('My User Name' , 'My Pass Word')
    ig_bot.nav_user('sina___vakili')
    ig_bot.follow_user('sina___vakili')
