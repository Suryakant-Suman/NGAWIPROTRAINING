import pytest
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.account_page import AccountPage
from utilities.data_reader import load_valid_users, load_products


MASTER = load_valid_users()[0]


@pytest.mark.flow
@pytest.mark.order(7)
@pytest.mark.parametrize("product_name", load_products())
def test_full_ecommerce_flow(driver, product_name):

    # LOGIN
    login = LoginPage(driver)
    login.open_login()
    login.login(MASTER["email"], MASTER["password"])

    # SEARCH
    search = SearchPage(driver)
    search.search_product(product_name)
    search.open_first_product()

    # ADD TO CART
    product = ProductPage(driver)
    product.add_to_cart()

    # CART UPDATE + REMOVE
    cart = CartPage(driver)
    cart.open_cart()
    cart.update_quantity("2")
    cart.remove_item()

    # LOGOUT
    account = AccountPage(driver)
    account.logout()

    assert "Account Logout" in driver.page_source