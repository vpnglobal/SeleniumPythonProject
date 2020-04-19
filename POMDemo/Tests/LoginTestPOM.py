from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append ( os.path.join ( os.path.dirname ( __file__ ), "..", ".." ) )
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage
import HtmlTestRunner


class LoginTests ( unittest.TestCase ):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome (
            executable_path="C:/Users/Vinay/PycharmProjects/Selenium/drivers/chromedriver.exe" )
        cls.driver.implicitly_wait ( 10 )
        cls.driver.maximize_window ()

    def test_login_valid(self):
        driver = self.driver
        driver.get ( "https://opensource-demo.orangehrmlive.com/" )
        # create a object of login page
        login = LoginPage ( driver )
        login.enter_username ( "Admin" )
        login.enter_password ( "admin123" )
        login.click_login ()

        homepage = HomePage ( driver )
        homepage.click_welcome ()
        homepage.click_logpout ()
        time.sleep ( 2 )

    @classmethod
    def tearDownClass(cls):
        cls.driver.close ()
        cls.driver.quit ()
        print ( "Login Sucessfull" )


if __name__ == '__main__':
    unittest.main ( testRunner=HtmlTestRunner.HTMLTestRunner (
        output="C:/Users/Vinay/PycharmProjects/Selenium/POMDemo/reports" ) )

# self.driver.find_element_by_xpath ( '//input[@id="txtUsername"]' ).send_keys ( "admin" )
# self.driver.find_element_by_xpath ( '//input[@id="txtPassword"]' ).send_keys ( "admin123" )
# self.driver.find_element_by_xpath ( '//input[@id="btnLogin"]' ).click ()
# self.driver.find_element_by_xpath ( '//a[@id="welcome"]' ).click ()
# self.driver.find_element_by_xpath ( '//a[contains(text(),"Logout")]' ).click ()
