import pytest
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utilities.data_reader import load_products


@pytest.mark.smoke
@pytest.mark.order(5)
@pytest.mark.parametrize("product_name", load_products())
def test_update_and_remove_cart(driver, product_name):

    search = SearchPage(driver)
    search.search_product(product_name)
    search.open_first_product()

    product = ProductPage(driver)
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open_cart()
    cart.update_quantity("2")
    cart.remove_item()

    assert "Shopping Cart" in driver.title
    assert "Your shopping cart is empty" in driver.page_source