#Instgram Bot Tutorial

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstgramBot:

    def __init__(self,username , password) :
        
        #Input Username and Password To App
        
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Firefox()

        self.login()


        #Open Firefox And Login To The Instagram 
    def login(self):
        self.driver.get('{}/accounts/login/?source=auth_switcher'.format(self.base_url))
        time.sleep(7)
        
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()
        time.sleep(2)

        print('Login Is Done')


    def like_photo(self,hashtag):
        driver = self.driver
        driver.get("{}/explore/tags/{}".format(self.base_url,hashtag))
        time.sleep(2)

        pic_hrefs = []
        for i in range(1, 2):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p/' in elem.get_attribute('href')]

                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]

                print('Check: pic href length ' + str(len(pic_hrefs)))
            
            except Exception:
                continue
        
        # Liking photos
        unique_photos = len(pic_hrefs)

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
            like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]')
            like_button().click()
            time.sleep(2)

            print ('I still have ' , str(unique_photos) , ' To like.')
            
            unique_photos -= 1

    #This Is User And Password Part
if __name__ == '__main__' :
    ig_bot = InstgramBot('username' , 'password')
    ig_bot.like_photo('TractorClub')

