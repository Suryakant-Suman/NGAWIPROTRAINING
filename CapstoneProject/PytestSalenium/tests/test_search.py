import pytest
import csv
import os
from pages.search_page import SearchPage


def load_products():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "products.csv")

    with open(path, newline="") as f:
        return [row["product"] for row in csv.DictReader(f)]


@pytest.mark.smoke
@pytest.mark.order(3)
@pytest.mark.parametrize("product_name", load_products())
def test_search_product(driver, product_name):

    search = SearchPage(driver)
    search.search_product(product_name)

    assert "Search" in driver.title
    assert product_name.lower() in driver.page_source.lower()
