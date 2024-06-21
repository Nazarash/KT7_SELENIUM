import pytest
import allure
from pageobjects.user.home import HomePage
from pageobjects.user.search import SearchPage

@pytest.mark.parametrize("name, search, product", [
    ("test1", "MacBook", "MacBook"),
    ("test2", "iPhone", "iPhone"),
    ("test3", "HTC Touch", "HTC Touch HD"),
    ("test4", "Palm", "Palm Treo Pro"),
])
def test_added_products_appear_in_search(user_browser, name, search, product):
    with allure.step(f"Open home page and search for product: {search}"):
        home_page = HomePage(user_browser)
        home_page.search_product(search)

    with allure.step(f"Check if product '{product}' appears in search results"):
        search_page = SearchPage(user_browser)
        assert search_page.get_product_by_name(product) is not None, f"Product {product} not found in search results"
