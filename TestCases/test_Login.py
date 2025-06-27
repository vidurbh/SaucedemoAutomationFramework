import pytest
from Utilities.readProperties import readConfig
from PageObjects.LoginPage.loginPage import LoginPage
from TestData.testData import valid_users,invalid_users,locked_user
from Utilities.customerLogger import LogGen
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLogin:

    baseURL=readConfig.getURL()
    logger=LogGen.loggen()



    @pytest.mark.parametrize("username,password",valid_users)
    def test_loginWithValidCredentials(self,setup,username,password):
        self.driver=setup
        self.driver.get(self.baseURL)
        loginObject=LoginPage(self.driver)
        loginObject.login(username,password)
        if "inventory" in self.driver.current_url:
            self.logger.info("Test Case passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False
    
    
    @pytest.mark.parametrize("username,password", invalid_users)
    def test_LoginWithInvalidCredentials(self,setup,username,password):
        self.driver=setup
        self.driver.get(self.baseURL)
        loginObject=LoginPage(self.driver)
        loginObject.login(username,password)
        error_element=self.driver.find_element(By.CSS_SELECTOR,'[data-test="error"]')
        error_message = error_element.text
        print('error message is', error_message)
        if username=="":
            if "required" in error_message:
                self.logger.info("Test Case Passed")
                self.driver.quit()
                assert True
            else:
                self.logger.info("Test Case Failed")
                self.driver.quit()
                assert False
        elif "password do not match" in error_message:
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False
       

    def test_LoginWithLockedUser(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        loginObject=LoginPage(self.driver)
        loginObject.login("locked_out_user", "secret_sauce" )
        error_element=self.driver.find_element(By.CSS_SELECTOR,'[data-test="error"]')
        error_message = error_element.text
        if "locked out" in error_message:
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False

   