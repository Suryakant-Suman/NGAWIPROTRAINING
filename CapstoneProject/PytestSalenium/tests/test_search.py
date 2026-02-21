import pytest
from pages.search_page import SearchPage
from utilities.data_reader import load_products


@pytest.mark.smoke
@pytest.mark.order(3)
@pytest.mark.parametrize("product_name", load_products())
def test_search_product(driver, product_name):

    search = SearchPage(driver)
    search.search_product(product_name)

    assert "Search" in driver.title
    assert product_name.lower() in driver.page_source.lower()