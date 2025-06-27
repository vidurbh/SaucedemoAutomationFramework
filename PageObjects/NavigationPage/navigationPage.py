from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavigationPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        ).click()
