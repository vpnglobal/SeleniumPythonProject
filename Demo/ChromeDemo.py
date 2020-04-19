from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver.exe")

driver.get("https:/google.co.uk")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()
print("Completed")