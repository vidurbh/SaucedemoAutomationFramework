import selenium

from selenium.webdriver.common.by import By


class LoginPage:


    userNameId='user-name'
    passwordId='password'
    loginButtonId='login-button'
    errorMessageXPATH='//*[@class="error-message-container error"]/h3/text()'

    def __init__(self, driver) :
            self.driver=driver

    def login(self, username, password):
        self.driver.find_element("id", self.userNameId).send_keys(username)
        self.driver.find_element("id", self.passwordId).send_keys(password)
        self.driver.find_element("id", self.loginButtonId).click()



