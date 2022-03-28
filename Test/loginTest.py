import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from Page.loginPage import LogIn
browser  = webdriver.Chrome(executable_path="./chromedriver.exe")
class LoginTest(unittest.TestCase):
    def test_LI_001(self):
        LogIn("mngr332078", "upEjasy", "btnLogin", browser)
        self.assertEqual('Guru99 Bank Manager HomePage', browser.title)
        sleep(2)
    def test_LI_002(self):
        LogIn("fake", "fake", "btnLogin", browser)
        alert = browser.switch_to_alert()
        self.assertEqual('User or Password is not valid',alert.text)
        sleep(2)
        alert.accept()
    def test_LI_003(self):
        LogIn("fake", "upEjasy", "btnLogin", browser)
        alert = browser.switch_to_alert()
        self.assertEqual('User or Password is not valid', alert.text)
        sleep(2)
        alert.accept()
        # browser.close()
    def test_LI_004(self):
        LogIn("mngr332078", "fake", "btnLogin", browser)
        alert = browser.switch_to_alert()
        self.assertEqual('User or Password is not valid', alert.text)
        sleep(2)
        alert.accept()
    def test_LI_005(self):
        LogIn("fake", "fake", "btnLogin", browser)
        alert = browser.switch_to_alert()
        self.assertEqual('User or Password is not valid', alert.text)
        sleep(2)
        alert.accept()
    def test_LI_006(self):
        LogIn("", "", "btnLogin", browser)
        alert = browser.switch_to_alert()
        self.assertEqual('User or Password is not valid', alert.text)
        sleep(2)
        alert.accept()
    def test_LI_007(self):
        LogIn("mngr332078", "", "btnLogin", browser)
        message = browser.find_element_by_id("message18")
        self.assertEqual('Password must not be blank', message.text)
        sleep(2)
    def test_LI_008(self):
        LogIn("", "upEjasy", "btnLogin", browser)
        alert = browser.switch_to_alert()
        self.assertEqual('User or Password is not valid', alert.text)
        sleep(2)
        alert.accept()
    def test_LI_009(self):
        LogIn("mngr332078", "upEjasy", "btnReset", browser)
        txtUser = browser.find_element_by_name("uid").get_attribute('value')
        self.assertEqual('', txtUser )
        sleep(2)
    def test_LI_010(self):
        LogIn("", "", "btnReset", browser)
        txtUser = browser.find_element_by_name("uid").get_attribute('value')
        self.assertEqual('', txtUser )
        sleep(2)
    def test_LI_011(self):
        LogIn("", "upEjasy", "btnReset", browser)
        txtUser = browser.find_element_by_name("uid").get_attribute('value')
        self.assertEqual('', txtUser )
        sleep(2)
    def test_LI_012(self):
        LogIn("mngr332078", "", "btnReset", browser)
        txtUser = browser.find_element_by_name("password").get_attribute('value')
        self.assertEqual('', txtUser )
        sleep(2)
        browser.close()