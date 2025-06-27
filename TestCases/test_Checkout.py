import pytest
from PageObjects.CartPage.cartPage import CartPage
from PageObjects.CheckoutPage.checkoutPage import CheckoutPage
from PageObjects.LoginPage.loginPage import LoginPage
from PageObjects.InventoryPage.inventoryPage import InventoryPage
from Utilities.readProperties import readConfig
from Utilities.customerLogger import LogGen
from selenium.webdriver.common.by import By


class TestCartCheckout:
    baseURL = readConfig.getURL()
    logger = LogGen.loggen()


    @pytest.fixture(autouse=True)
    def login_before_sorting(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        loginObj = LoginPage(self.driver)
        loginObj.login("standard_user", "secret_sauce")
    
    def testAddToCartAndValidateTotal(self):
        inventory = InventoryPage(self.driver)
        prices = inventory.addItemsToCart(count=2)
        expected_total = sum(prices)
        inventory.go_to_cart()
        cart = CartPage(self.driver)
        cart.clickCheckout()
        checkout = CheckoutPage(self.driver)
        checkout.fill_user_info("Test", "Test", "12345")

        item_total = checkout.get_item_total()
        print("Item Total", item_total)
        tax, total = checkout.get_tax_and_final_total()
        print("Tax and total", tax,total)

        assert round(item_total, 2) == round(expected_total, 2), f"Expected item total: {expected_total}, but got {item_total}"
        calculated_total = round(item_total + tax, 2)
        self.logger.info("Test Case Passed")
        self.driver.quit()
        assert round(total, 2) == calculated_total, f"Expected total: {calculated_total}, but got {total}"

        

    def test_checkoutMissingFirstName(self):
        
        inventory = InventoryPage(self.driver)
        inventory.addItemsToCart(1)
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.clickCheckout()

        checkout = CheckoutPage(self.driver)

        checkout.fill_user_info("", "Test", "12345")

        error = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        print("Error message is", error)

        if "First Name is required" in error:
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False


    def test_checkoutMissingLastName(self):
        
        inventory = InventoryPage(self.driver)
        inventory.addItemsToCart(1)
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.clickCheckout()

        checkout = CheckoutPage(self.driver)

        checkout.fill_user_info("Test", "", "12345")

        error = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        print("Error message is", error)

        if "Last Name is required" in error:
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False
    
    def test_checkoutMissingPostalCode(self):
        
        inventory = InventoryPage(self.driver)
        inventory.addItemsToCart(1)
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.clickCheckout()

        checkout = CheckoutPage(self.driver)

        checkout.fill_user_info("Test", "LastName", "")

        error = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        print("Error message is", error)

        if "Postal Code is required" in error:
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False
    
    def test_checkoutAllMandatoryFields(self):
        
        inventory = InventoryPage(self.driver)
        inventory.addItemsToCart(1)
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.clickCheckout()

        checkout = CheckoutPage(self.driver)

        checkout.fill_user_info("", "", "")

        currentURL = self.driver.current_url
        print("Current URL is", currentURL)

        if "checkout-step-two.html" not in currentURL:
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False
    
    def test_finishButtonCheckoutFlow(self, setup):
        self.driver = setup
        
        inventory = InventoryPage(self.driver)
        inventory.addItemsToCart(2)
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.clickCheckout()

        checkout = CheckoutPage(self.driver)
        checkout.fill_user_info("test", "Testing", "12345")

        checkout.click_finish()

        confirmation = checkout.get_confirmation_message()
        print("Confirmation message is", confirmation)
        if "Thank you for your order!" in confirmation:
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False    


    def test_remove_item_updates_total(self):
        inventory = InventoryPage(self.driver)
        inventory.addItemsToCart(2)
        inventory.removeItemsfromCart(2)
        inventory.go_to_cart()

        cart = CartPage(self.driver)
        cart.clickCheckout()

        checkout = CheckoutPage(self.driver)
        checkout.fill_user_info("Test", "User", "12345")

        item_total = checkout.get_item_total()
        if item_total == 0:
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False

    def test_checkoutCancelRedirectsToCart(self):

            inventory = InventoryPage(self.driver)
            inventory.addItemsToCart(2)
            inventory.go_to_cart()

            cart = CartPage(self.driver)
            cart.clickCheckout()

            checkout = CheckoutPage(self.driver)
            checkout.click_cancel()

            current_url = self.driver.current_url
            if "cart.html" in current_url:
                 self.logger.info("Test Case Passed")
                 self.driver.quit()
                 assert True
            else:
                 self.logger.info("Test Case Failed")
                 self.driver.quit()
                 assert False
