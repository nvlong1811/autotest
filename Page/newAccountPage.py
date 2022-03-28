from selenium.webdriver.common.keys import Keys
def NewAccount(cusid, inideposit, btn, browser):
    browser.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
    txtCusid = browser.find_element_by_name("cusid")
    txtCusid.send_keys(cusid)

    txtIni = browser.find_element_by_name("inideposit")
    txtIni.send_keys(inideposit)

    txtIni.send_keys(Keys.TAB)
    if (btn != "none"):
        btnSubmit = browser.find_element_by_name(btn)
        btnSubmit.click()

