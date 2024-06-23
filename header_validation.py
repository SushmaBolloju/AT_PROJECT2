'''
Project 2 : Selenium with python
___Testing login credentials___
Test Case ID: TC_PIM_02
Header validation on login page'''

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

   def login(self):
       self.boot()
       sleep(3)
       username = self.driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
       # Passing the username value
       username.send_keys("Admin")
       password = self.driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
       # Passing the password
       password.send_keys("admin123")
       login_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
       # Clicking on the login button
       login_button.click()

   # Test case ID: TC_PIM_02
   def admin_page_header_validation(self):
        sleep(5)
        # Navigate to Admin page
        admin_link = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]")
        # Click on the admin page link
        admin_link.click()

        print(self.driver.title)
        # Validate the title of the page
        assert "OrangeHRM" == self.driver.title
        sleep(5)

        top_menu_items = self.driver.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li')

        menu_items_text = []
        for item in top_menu_items:
            print(item.text)
            menu_items_text.append(item.text)
        #changed Corporate Banking to Corporate Branding in validation, since page is having Corporate Branding item only.
        options = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Branding",
                   "Configuration"]
        for option_text in options:
            assert option_text in menu_items_text

        sleep(5)
        self.quit()

#Passing URL to the class Orange
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#calling the function
obj.login()
obj.admin_page_header_validation()