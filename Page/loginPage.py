def LogIn(username, password, btn, browser):
    browser.get("http://www.demo.guru99.com/V4/")

    txtUser = browser.find_element_by_name("uid")
    txtUser.send_keys(username)

    txtPass = browser.find_element_by_name("password")
    txtPass.send_keys(password)

    btnSubmit = browser.find_element_by_name(btn)
    btnSubmit.click()
    
