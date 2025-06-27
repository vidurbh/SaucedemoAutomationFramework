import pytest
from PageObjects.LoginPage.loginPage import LoginPage
from Utilities.customerLogger import LogGen
from Utilities.readProperties import readConfig
from PageObjects.InventoryPage.inventoryPage import InventoryPage
from selenium.webdriver.common.by import By


class TestProductVisibility:

    baseURL=readConfig.getURL()
    logger=LogGen.loggen()

    @pytest.fixture(autouse=True)
    def login_before_sorting(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        loginObj = LoginPage(self.driver)
        loginObj.login("standard_user", "secret_sauce")

    def test_productVisibilityAfterLogin(self):
        inventory=InventoryPage(self.driver)
        prdouctList=inventory.fetchProductList()
        print("length of prdouctList", len(prdouctList))
        if len(prdouctList)>0 :
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False

    def test_productDetailsVisibility(self):
        inventory=InventoryPage(self.driver)
        prdouctList=inventory.fetchProductList()
        print("length of prdouctList", len(prdouctList))
        for product in prdouctList:
            name=product.find_element(By.CLASS_NAME,'inventory_item_name ').text
            print("name", name)
            assert name.strip() != "", "Product name missing"

            price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
            print("price", price)
            assert "$" in price, "Product price missing or invalid"

            img = product.find_element(By.CLASS_NAME, "inventory_item_img").find_element(By.TAG_NAME, "img")
            assert img.get_attribute("src") != "", "Product image is missing"


