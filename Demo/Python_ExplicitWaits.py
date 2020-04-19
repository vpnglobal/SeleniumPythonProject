# explicit waits wiats for a certain condition to occur before proceding to next step
# need to import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../drivers/chromedriver.exe")
#driver.implicitly_wait(10)
driver.get("https:/google.co.uk")
driver.find_element_by_name("q").send_keys("Automation step by step")
wait = WebDriverWait(driver, 10)
try:
    element = wait.until(EC.element_to_be_clickable((By.NAME,"btnK1")))
    print("Element is clickable")
except:
    print("Element is not clickable")
    driver.maximize_window()
    driver.close()
    driver.quit()
    print ("Test Completed")
    exit(1)


