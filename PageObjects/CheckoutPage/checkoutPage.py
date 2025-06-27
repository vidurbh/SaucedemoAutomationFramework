from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_user_info(self, fname, lname, pincode):
        firstName=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"first-name")))
        firstName.send_keys(fname)
        self.driver.find_element(By.ID, "last-name").send_keys(lname)
        self.driver.find_element(By.ID, "postal-code").send_keys(pincode)
        self.driver.find_element(By.ID, "continue").click()

        # print("⏳ Waiting for checkout page URL...")
        # WebDriverWait(self.driver, 10).until(
        #     EC.url_contains("checkout-step-one.html")
        # )

        # print("✅ URL confirmed, waiting for form...")
        # firstName = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "first-name"))
        # )
        # firstName.send_keys(fname)

        # self.driver.find_element(By.ID, "last-name").send_keys(lname)
        # self.driver.find_element(By.ID, "postal-code").send_keys(pincode)

    def get_item_total(self):
        item_total_text= self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        return float(item_total_text.split("$")[1])

    def get_tax_and_final_total(self):
        tax = self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        taxValue = float(tax.replace("Tax: $", "").strip())
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        totalValue = float(total.replace("Total: $", "").strip())

        return taxValue, totalValue
    

    def click_finish(self):
        finishButton=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"finish")))
        finishButton.click()

    def get_confirmation_message(self):
        confirmationMessage= self.driver.find_element(By.CLASS_NAME, "complete-header").text

        return confirmationMessage
    
    def click_cancel(self):
        self.driver.find_element(By.ID, "cancel").click()


    
    
