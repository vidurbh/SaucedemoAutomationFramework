from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class InventoryPage:


    productContainerXPATH=''
    allProductListXPATH='//div[@class="inventory_container"]//div[@class="inventory_item"]'

    
    def __init__(self, driver) :
            self.driver=driver

    def select_sort_option(self, value):
        dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        Select(dropdown).select_by_visible_text(value)


    def get_product_names(self):
        name_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [name.text for name in name_elements]
    
    def get_product_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(price.text.replace("$", "")) for price in price_elements]
    
    def fetchProductList(self):
         products=self.driver.find_elements(By.XPATH,self.allProductListXPATH)
         return products
    

    def addItemsToCart(self, count=2):
        prices = []
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        add_buttons = self.driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        for i in range(count):
            prices.append(float(price_elements[i].text.replace("$", "")))
            add_buttons[i].click()
        return prices

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    
    def removeItemsfromCart(self,count=1):
        remove_buttons = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Remove']")))
        removed = 0
        for btn in remove_buttons:
            if removed >= count:
                break
            btn.click()
            removed += 1