from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Product:
    def __init__(self, name, description, meta_tag, model, seo_key):
        self.name = name
        self.description = description
        self.meta_tag = meta_tag
        self.model = model
        self.seo_key = seo_key


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def create_new_product(self, product, category):
        # Нажать добавить
        self.driver.find_element(By.CSS_SELECTOR, '#content > div.page-header > div > div > a').click()

        # Заполнение форм
        self.driver.find_element(By.ID, 'input-name1').send_keys(product.name)
        self.driver.find_element(By.ID, 'input-meta-title1').send_keys(product.meta_tag)

        # Переход на вкладку data
        self.driver.find_element(By.CSS_SELECTOR, '#form-product > ul > li:nth-child(2) > a').click()
        # Заполнение формы
        self.driver.find_element(By.ID, 'input-model').send_keys(product.model)

        # Переход на вкладку seo
        self.driver.find_element(By.CSS_SELECTOR, '#form-product > ul > li:nth-child(10) > a').click()
        # Заполнение формы
        self.driver.find_element(By.NAME, 'product_seo_url[0][1]').send_keys(product.seo_key)

        # Переход на вкладку links
        self.driver.find_element(By.CSS_SELECTOR, '#form-product > ul > li:nth-child(3) > a').click()
        self.driver.find_element(By.ID, 'input-category').send_keys(category)

        # Сохранить
        self.driver.find_element(By.CSS_SELECTOR, '#content > div.page-header > div > div > button').click()
        
    def delete_product_by_name(self, name):
        # Заполнение формы
        self.driver.find_element(By.ID, 'input-name').send_keys(name)
        # Фильтрация
        self.driver.find_element(By.ID, 'button-filter').click()

        # Поставить налочку
        checkbox = self.driver.find_element(By.CSS_SELECTOR, '#form-product > div.table-responsive > table > tbody')
        checkbox.find_element(By.XPATH, f"//td[contains(text(), '{name}')]/preceding-sibling::td/input").click()

        # Удалить
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def is_alert_visible(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, '#content > div.container-fluid > div.alert.alert-danger.alert-dismissible')
            return True
        except:
            return False
