from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Category:
    def __init__(self, title, meta_tag, seo_key):
        self.title = title
        self.meta_tag = meta_tag
        self.seo_key = seo_key

class CategoryPage:
    def __init__(self, driver):
        self.driver = driver

    def create_new_category(self, category):
        # Нажать добавить
        self.driver.find_element(By.CSS_SELECTOR, '#content > div.page-header > div > div > a.btn.btn-primary').click()

        # Заполнение форм
        self.driver.find_element(By.ID, 'input-name1').send_keys(category.title)
        self.driver.find_element(By.ID, 'input-meta-title1').send_keys(category.meta_tag)

        # Переход на вкладку seo
        self.driver.find_element(By.CSS_SELECTOR, '#form-category > ul > li:nth-child(3) > a').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'category_seo_url[0][1]')))
        # Заполнение формы
        self.driver.find_element(By.NAME, 'category_seo_url[0][1]').send_keys(category.seo_key)

        # Сохранить
        self.driver.find_element(By.CSS_SELECTOR, '#content > div.page-header > div > div > button').click()

    def is_alert_visible(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, '#content > div.container-fluid > div.alert.alert-danger.alert-dismissible')
            return True
        except:
            return False

        