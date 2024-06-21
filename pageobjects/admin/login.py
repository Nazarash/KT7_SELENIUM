from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        # Заполнение полей
        self.driver.find_element(By.NAME, 'username').send_keys("demo")
        self.driver.find_element(By.NAME, 'password').send_keys("demo")
        # Вход
        self.driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#modal-security > div > div > div.modal-header > button')))
        # Закрытие уведомления
        self.driver.find_element(By.CSS_SELECTOR, '#modal-security > div > div > div.modal-header > button').click()
