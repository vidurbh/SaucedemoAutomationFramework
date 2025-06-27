from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # def clickCheckout(self):
    #     print("Entered inside ClickCheckout")
    #     checkoutButton = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "checkout"))
    #     )
    #     checkoutButton.click()

    def clickCheckout(self):
        print("Entered inside ClickCheckout")
        print("Current URL:", self.driver.current_url)
        
        try:
            checkoutButton = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkoutButton.click()
        except Exception as e:
            print("Checkout button not found or not clickable:", e)
            self.driver.save_screenshot("./Logs/checkout_button_error.png")
            raise

   