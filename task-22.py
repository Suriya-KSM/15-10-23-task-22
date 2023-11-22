from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

#Fetching followers and following from the guvi instagram account.
class Guvi_insta:
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def Login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)

            #Fetching followers
            followers=self.driver.find_element(by=By.XPATH, value='.//*[contains(text(), "followers")]/span')
            follower_count=followers.text

            #Fetching followings
            following=self.driver.find_element(by=By.XPATH, value='.//*[contains(text(), "following")]/span')
            following_count=following.text

            #Printing those values
            print("Total number of followers Guvi Have = ", follower_count)
            print("Total number of following Guvi have = ", following_count)

        #Exception handling
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        
        #closing the browser when the task done
        finally:
            self.driver.close()

#declating URL
URL = "https://www.instagram.com/guviofficial/"

#creating object for the main class
obj = Guvi_insta(URL)

#calling the function using the object for the class
obj.Login()