import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
time.sleep(5)
driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.quit()



