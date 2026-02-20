import pytest
import csv
import os
from pages.login_page import LoginPage


def load_users():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "users.csv")

    with open(path, newline="") as f:
        return list(csv.DictReader(f))


@pytest.mark.smoke
@pytest.mark.order(2)
@pytest.mark.parametrize("user", load_users())
def test_login(driver, user):

    login = LoginPage(driver)

    login.open_login()
    login.login(user["email"], user["password"])

    assert "My Account" in driver.title
    assert "Logout" in driver.page_source
