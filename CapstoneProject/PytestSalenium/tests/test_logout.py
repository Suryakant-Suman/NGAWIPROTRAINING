import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from utilities.data_reader import load_valid_users


@pytest.mark.smoke
@pytest.mark.order(6)
def test_logout(driver):

    user = load_valid_users()[0]

    login = LoginPage(driver)
    login.open_login()
    login.login(user["email"], user["password"])

    account = AccountPage(driver)
    account.logout()

    assert "Account Logout" in driver.page_source