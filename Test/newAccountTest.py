import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from Page.loginPage import LogIn
from Page.newAccountPage import NewAccount
browser  = webdriver.Chrome(executable_path="./chromedriver.exe")
class NewAccountTest(unittest.TestCase):
    LogIn("mngr332078", "upEjasy", "btnLogin", browser)
    def test_NC_001(self):
        NewAccount("" , "",  "none", browser)
        message = browser.find_element_by_id("message14")
        self.assertEqual('Customer ID is required', message.text)
        sleep(3)
    def test_NC_002(self):
        NewAccount("aaaaaaaaa" , ""  , "none", browser)
        message = browser.find_element_by_id("message14")
        self.assertEqual('Characters are not allowed', message.text)
        sleep(3)
    def test_NC_003(self):
        NewAccount("@@@@@@@@" , "", "none", browser)
        message = browser.find_element_by_id("message14")
        self.assertEqual('Special characters are not allowed', message.text)
        sleep(3)
    def test_NC_004(self):
        NewAccount("93  539" , "" , "none", browser)
        message = browser.find_element_by_id("message14")
        self.assertEqual('Characters are not allowed', message.text)
        sleep(3)
    def test_NC_005(self):
        NewAccount("     93539" ,"" , "none", browser)
        message = browser.find_element_by_id("message14")
        self.assertEqual('First character can not have space', message.text)
        sleep(3)
    def test_NC_006(self):
        NewAccount("93539" , "", "none", browser)
        message = browser.find_element_by_id("message19")
        self.assertEqual('Initial Deposit must not be blank', message.text)
        sleep(3)
    def test_NC_007(self):
        NewAccount("93539" , "aaaaa", "none", browser)
        message = browser.find_element_by_id("message19")
        self.assertEqual('Characters are not allowed', message.text)
        sleep(3)
    def test_NC_008(self):
        NewAccount("93539" , "@@@@@@@" , "none", browser)
        message = browser.find_element_by_id("message19")
        self.assertEqual('Special characters are not allowed', message.text)
        sleep(3)
    def test_NC_009(self):
        NewAccount("93539" , "100 000" , "none", browser)
        message = browser.find_element_by_id("message19")
        self.assertEqual('Characters are not allowed', message.text)
        sleep(3)
    def test_NC_010(self):
        NewAccount("93539" , "   100000" , "none", browser)
        message = browser.find_element_by_id("message19")
        self.assertEqual('First character can not have space', message.text)
        sleep(3)

        browser.close()