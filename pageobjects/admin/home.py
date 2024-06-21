from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_category_page(self):
        self.driver.find_element(By.CSS_SELECTOR, '#menu-catalog > a').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#collapse1 > li:nth-child(1) > a')))
        self.driver.find_element(By.CSS_SELECTOR, '#collapse1 > li:nth-child(1) > a').click()

    def go_to_product_page(self):
        self.driver.find_element(By.CSS_SELECTOR, '#menu-catalog > a').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) > a')))
        self.driver.find_element(By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) > a').click()
