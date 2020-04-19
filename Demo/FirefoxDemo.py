import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = "../drivers/geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)

driver.get("https:/google.co.uk")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").send_keys(Keys.RETURN)

time.sleep(2)

print(driver.title)

driver.close()
driver.quit()