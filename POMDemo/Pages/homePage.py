from POMDemo.Locators.locators import Locators

class HomePage():

    def __init__(self,driver):

        self.driver = driver
        self.welcome_link_xpath = Locators.welcome_link_xpath
        self.logout_button_xpath = Locators.logout_button_xpath

    def click_welcome(self):
        self.driver.find_element_by_xpath ( self.welcome_link_xpath).click ()

    def click_logpout(self):
        self.driver.find_element_by_xpath (self.logout_button_xpath).click ()