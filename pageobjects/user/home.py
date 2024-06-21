from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, name):
        search_input = self.driver.find_element(By.NAME, 'search')
        search_input.clear()
        search_input.send_keys(name)
        search_input.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
