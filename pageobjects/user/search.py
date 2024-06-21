from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_by_name(self, name):
        try:
            self.driver.find_element(By.XPATH, f"//h4/a[text()='{name}']")
            return True
        except NoSuchElementException:
            return False
