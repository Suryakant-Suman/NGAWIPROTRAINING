import pytest
from pages.login_page import LoginPage
from utilities.data_reader import load_valid_users, load_invalid_users


@pytest.mark.smoke
@pytest.mark.order(2)
@pytest.mark.parametrize("user", load_valid_users())
def test_login(driver, user):

    login = LoginPage(driver)
    login.open_login()
    login.login(user["email"], user["password"])

    assert "My Account" in driver.title
    assert "Logout" in driver.page_source


# -------- Negative Test --------
@pytest.mark.negative
@pytest.mark.parametrize("user", load_invalid_users())
def test_login_invalid_email_format(driver, user):

    login = LoginPage(driver)
    login.open_login()
    login.login(user["email"], user["password"])

    assert "Warning" in driver.page_source or "Invalid" in driver.page_source