import pytest
from PageObjects.LoginPage.loginPage import LoginPage
from PageObjects.NavigationPage.navigationPage import NavigationPage
from Utilities.readProperties import readConfig
from Utilities.customerLogger import LogGen
from selenium.webdriver.common.by import By

class TestLogout:
    baseURL = readConfig.getURL()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def login_before_sorting(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        loginObj = LoginPage(self.driver)
        loginObj.login("standard_user", "secret_sauce")


    def test_logout_functionality(self):       
        nav = NavigationPage(self.driver)
        nav.logout()        
        loginButton=self.driver.find_element(By.ID, "login-button")
        print( loginButton.is_displayed())
        if loginButton.is_displayed():
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True

        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False

    

            
