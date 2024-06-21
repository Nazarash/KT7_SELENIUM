
from selenium import webdriver

from pageobjects.admin.category import Category, CategoryPage
from pageobjects.admin.home import HomePage
from pageobjects.admin.login import LoginPage

options = webdriver.FirefoxOptions()
options.set_capability("browserVersion", "124.0")
options.set_capability("selenoid:options", {"enableVideo": True, "enableVNC": True,})

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub/",
    options=options,
)

driver.get("https://demo.opencart.com/admin")

# page = LoginPage(driver)

# page.login()

# home_page = HomePage(driver)
# home_page.go_to_category_page()

# category_page = CategoryPage(driver)
# category_page.create_new_category(Category(title="devices", meta_tag="devices", seo_key="devices"))

# print(category_page.is_alert_visible())