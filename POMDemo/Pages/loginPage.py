from POMDemo.Locators.locators import Locators
class LoginPage ():

    # create a constructor using def __init__(self) . This is default constructor and is called anytime class object is created.

    def __init__(self, driver):
        self.driver = driver
        # create locators in format <ObjectName_ObjectType_locator_type>

        self.username_textbox_xpath = Locators.username_textbox_xpath
        self.password_textbox_xpath = Locators.password_textbox_xpath
        self.login_button_xpath = Locators.login_button_xpath

    # create function or action methods
    def enter_username(self, username):
        self.driver.find_element_by_xpath ( self.username_textbox_xpath ).clear ()
        self.driver.find_element_by_xpath ( self.username_textbox_xpath ).send_keys (username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath ( self.password_textbox_xpath ).clear ()
        self.driver.find_element_by_xpath ( self.password_textbox_xpath ).send_keys ( password )

    def click_login(self):
        self.driver.find_element_by_xpath ( self.login_button_xpath ).submit()
