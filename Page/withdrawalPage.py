from selenium.webdriver.common.keys import Keys
def WithDrawal(account_no, amount, description, btn, browser):
    browser.find_element_by_xpath("/html/body/div[3]/div/ul/li[9]/a").click()
    txtAccount_no = browser.find_element_by_name("accountno")
    txtAccount_no.send_keys(account_no)

    txtAmount = browser.find_element_by_name("ammount")
    txtAmount.send_keys(amount)

    txtDescription = browser.find_element_by_name("desc")
    txtDescription.send_keys(description)
    txtDescription.send_keys(Keys.TAB)
    if (btn != "none"):
        btnSubmit = browser.find_element_by_name(btn)
        btnSubmit.click()
    
