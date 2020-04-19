import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https:/google.co.uk")

driver.find_element_by_name("q").send_keys("Automation step by Step")
driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']//input[@name='btnK']").click()
driver.close()
driver.quit()