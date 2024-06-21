from turtle import textinput
import pytest
from selenium import webdriver
import allure

from pageobjects.admin.home import HomePage
from pageobjects.admin.login import LoginPage
from pageobjects.admin.category import Category, CategoryPage
from pageobjects.admin.product import Product, ProductPage


def test_create_new_category(admin_browser):
    with allure.step("Open admin login page"):
        page = LoginPage(admin_browser)

    with allure.step("Login as admin"):
        page.login()

    with allure.step("Go to category page"):
        home_page = HomePage(admin_browser)
        home_page.go_to_category_page()

    with allure.step("Create new category"):
        category_page = CategoryPage(admin_browser)
        category_page.create_new_category(Category(title="devices", meta_tag="devices", seo_key="devices"))
    
    with allure.step("Check if alert is visible"):
        assert category_page.is_alert_visible(), "Alert didn't appear"


@pytest.mark.parametrize("test_input", [
    Product("Mice1", "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..", "Mice1", "Mice1", "Mice1"),
    Product("Mice2", "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, adipisci velit..", "Mice2", "Mice2", "Mice2"),
    Product("keyboard1", "Neque porro quisquam dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..", "keyboard1", "keyboard1", "keyboard1"),
    Product("keyboard2", "Neque est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..", "keyboard2", "keyboard2", "keyboard2")
])
def test_add_devices_to_category(admin_browser, test_input):
    with allure.step("Open admin login page"):
        page = LoginPage(admin_browser)

    with allure.step("Login as admin"):
        page.login()

    with allure.step("Go to product page"):
        home_page = HomePage(admin_browser)
        home_page.go_to_product_page()

    with allure.step("Create products and add them to the category"):
        product_page = ProductPage(admin_browser)
        product_page.create_new_product(test_input, "devices")
    
    with allure.step("Check if alert is visible"):
        assert product_page.is_alert_visible(), "Alert didn't appear"
