import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
# Login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

# Navigate to Admin page
admin_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]")))

# Click on the admin page link
admin_link.click()
time.sleep(5)

main_menu_items_text = []
main_menu_items = driver.find_elements(By.XPATH , '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li')
for item in main_menu_items :
    print(item.text)
    main_menu_items_text.append(item.text)
main_menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
for option_text in main_menu_options:
    assert option_text in main_menu_items_text

# # Close the browser
driver.quit()
