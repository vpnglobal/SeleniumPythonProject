# Ixplicit waits it will poll the DOM or document object model for a specific duration to locate om element 500ms until timeout
from selenium import webdriver

driver = webdriver.Chrome("../drivers/chromedriver.exe")
#implicity wait by default it is set to 0 seconds
driver.implicitly_wait(10)
driver.get("https:/google.co.uk")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
driver.maximize_window()
driver.close()
driver.quit()
print("Test Completed")