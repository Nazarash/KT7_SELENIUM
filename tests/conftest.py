import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def admin_browser():
    options = webdriver.FirefoxOptions()
    options.set_capability("browserVersion", "124.0")
    options.set_capability("selenoid:options", {"enableVideo": True, "enableVNC": True,})

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub/",
        options=options,
    )

    driver.get("https://demo-opencart.ru/admin/index.php")

    yield driver
    # driver.quit()

@pytest.fixture
def user_browser():
    options = webdriver.FirefoxOptions()
    options.set_capability("browserVersion", "124.0")
    options.set_capability("selenoid:options", {"enableVideo": True, "enableVNC": True,})

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub/",
        options=options,
    )

    driver.get("https://demo-opencart.ru/index.php")

    yield driver
    # driver.quit()