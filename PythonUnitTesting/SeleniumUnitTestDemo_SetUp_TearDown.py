import unittest
from selenium import webdriver

class MyTestCase (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.co.uk")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x,"Automation step by step - Google Search")

    def test_search_2(self):
        self.driver.get ("https://www.google.co.uk")
        self.driver.find_element_by_name ("q").send_keys("Vinay Mundra")
        self.driver.find_element_by_name ("btnK").click ()
        x = self.driver.title
        print(x)
        self.assertEqual (x, "Vinay Mundra - Google Search" )

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

# if __name__ == '__main__':
#     unittest.main ()
