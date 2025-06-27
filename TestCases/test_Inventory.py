import pytest
from PageObjects.LoginPage.loginPage import LoginPage
from PageObjects.InventoryPage.inventoryPage import InventoryPage
from Utilities.readProperties import readConfig
from Utilities.customerLogger import LogGen

class TestSorting:

    baseURL=readConfig.getURL()
    logger=LogGen.loggen()

    @pytest.fixture(autouse=True)
    def login_before_sorting(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        loginObj = LoginPage(self.driver)
        loginObj.login("standard_user", "secret_sauce")

    def test_sortByNameAZ(self):
        inventory = InventoryPage(self.driver)
        inventory.select_sort_option("Name (A to Z)")
        names = inventory.get_product_names()
        if names == sorted(names):
            self.driver.close()
            self.logger.info("Test Case Passed")
            assert True
        else:
            self.driver.close()
            self.logger.info("Test Case Failed")
            assert False

    def test_sortByNameZA(self):
        inventory = InventoryPage(self.driver)
        inventory.select_sort_option("Name (Z to A)")
        names = inventory.get_product_names()
        if names == sorted(names, reverse=True):
            self.driver.close()
            self.logger.info("Test Case Passed")
            assert True
        else:
            self.driver.close()
            self.logger.info("Test Case Failed")
            assert False



        
    def test_sortByPriceLowToHigh(self):
        inventory = InventoryPage(self.driver)
        inventory.select_sort_option("Price (low to high)")
        prices = inventory.get_product_prices()
        print("prices", prices)
        if prices == sorted(prices):
            self.logger.info("Test Case Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.close()
            assert False

    def test_sortByPriceHighToLow(self):
        inventory = InventoryPage(self.driver)
        inventory.select_sort_option("Price (high to low)")
        prices = inventory.get_product_prices()
        if prices == sorted(prices, reverse=True):
            self.logger.info("Test Case Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.close()
            assert False



