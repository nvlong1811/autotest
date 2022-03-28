import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from Page.giftPage import GiftPage
browser  = webdriver.Chrome(executable_path="./chromedriver.exe")
browser.get("https://trumtx79.xyz/")
otp = browser.find_element_by_name("phone")
otp.send_keys("0354735461")
btnSubmit = browser.find_element_by_xpath("/html/body/div[1]/div/section/div[2]/div[2]/div/div[2]/div/div/a")
btnSubmit.click()
sleep(5)
class GiftTest(unittest.TestCase):
    def test_LI_001(self):
        for x in range(6):
            GiftPage(x, browser)
            alert = browser.switch_to_alert()
            self.assertEqual("Sai mã xác minh, vui lòng kiếm tra lại. Hoặc tải lại trang web này để xin cấp mã mới nhé.",alert.text)
            sleep(2)
            alert.accept()
            sleep(2)
