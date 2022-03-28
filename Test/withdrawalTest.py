import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from Page.loginPage import LogIn
from Page.withdrawalPage import WithDrawal
browser  = webdriver.Chrome(executable_path="./chromedriver.exe")
class WithDrawalTest(unittest.TestCase):
    LogIn("mngr332078", "upEjasy", "btnLogin", browser)
    def test_WD_001(self):
        WithDrawal("" , "" , "" , "none", browser)
        message = browser.find_element_by_id("message2")
        self.assertEqual('Account Number must not be blank', message.text)
        sleep(3)
    def test_WD_002(self):
        WithDrawal("aaaaaaaaa" , "" , "" , "none", browser)
        message = browser.find_element_by_id("message2")
        self.assertEqual('Characters are not allowed', message.text)
        sleep(3)
    def test_WD_003(self):
        WithDrawal("@@@@@@@@" , "" , "" , "none", browser)
        message = browser.find_element_by_id("message2")
        self.assertEqual('Special characters are not allowed', message.text)
        sleep(3)
    def test_WD_004(self):
        WithDrawal("      93539" , "" , "" , "none", browser)
        message = browser.find_element_by_id("message2")
        self.assertEqual('First character can not be space', message.text)
        sleep(3)
    def test_WD_005(self):
        WithDrawal("93539" , "" , "" , "none", browser)
        message = browser.find_element_by_id("message1")
        self.assertEqual('Amount field must not be blank', message.text)
        sleep(3)
    def test_WD_006(self):
        WithDrawal("93539" , "aaaaaa" , "" , "none", browser)
        message = browser.find_element_by_id("message1")
        self.assertEqual('Characters are not allowed', message.text)
        sleep(3)
    def test_WD_007(self):
        WithDrawal("93539" , "@@@@@@@@" , "" , "none", browser)
        message = browser.find_element_by_id("message1")
        self.assertEqual('Special characters are not allowed', message.text)
        sleep(3)
    def test_WD_008(self):
        WithDrawal("93539" , "     100" , "" , "none", browser)
        message = browser.find_element_by_id("message1")
        self.assertEqual('First character can not be space', message.text)
        sleep(3)
    def test_WD_009(self):
        WithDrawal("93539" , "100" , "" , "none", browser)
        message = browser.find_element_by_id("message17")
        self.assertEqual('Description can not be blank', message.text)
        sleep(3)
    def test_WD_010(self):
        WithDrawal("93539" , "100" , "long" , "AccSubmit", browser)
        message = browser.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p")
        self.assertEqual('Transaction details of Withdrawal for Account 93539', message.text)
        sleep(3)
    def test_WD_011(self):
        WithDrawal("93539" , "" , "" , "res", browser)
        message = browser.find_element_by_id("message2")
        self.assertEqual('', message.text)
        sleep(3)
    def test_WD_012(self):
        WithDrawal("93539" , "100" , "" , "res", browser)
        message = browser.find_element_by_id("message2")
        self.assertEqual('', message.text)
        sleep(3)
    def test_WD_013(self):
        WithDrawal("93539" , "100" , "Long" , "res", browser)
        message = browser.find_element_by_id("message2")
        self.assertEqual('', message.text)
        sleep(3)
        browser.close()