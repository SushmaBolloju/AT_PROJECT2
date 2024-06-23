
'''
Project 2 : Selenium with python
___Testing login credentials___
Test Case ID: TC_PIM_01
Forgot password link validation on login page'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class Orange:

   def __init__(self, url):

       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(self.url)
       sleep(3)
       #Maximizing window
       self.driver.maximize_window()

   def quit(self):
       #Quiting function
       self.driver.quit()

   #Test case ID: TC_PIM_01
   def password_reset(self):
       self.boot()
       sleep(3)
       username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
       # Passing the username value
       username.send_keys("Admin")
       sleep(2)
       forgot_pwd=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
       forgot_pwd.click()
       sleep(3)
       username=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
       username.send_keys("Admin")
       sleep(5)
       reset=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
       reset.click()
       sleep(5)
       self.quit()

#Passing URL to the class Orange
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#calling the function
obj.password_reset()
