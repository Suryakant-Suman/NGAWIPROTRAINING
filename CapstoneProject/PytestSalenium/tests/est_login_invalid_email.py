import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.data_reader import load_invalid_users
from utilities.logger import get_logger

logger = get_logger()


@pytest.mark.negative
@pytest.mark.parametrize("user", load_invalid_users())
def test_login_invalid_email(driver, user):

    logger.info("========== START Invalid Login Test ==========")

    # Open login page manually (no LoginPage.login())
    logger.info("Opening Login page")
    driver.find_element(By.LINK_TEXT, "My Account").click()
    driver.find_element(By.LINK_TEXT, "Login").click()

    # Wait for email field to ensure page fully loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-email"))
    )

    logger.info(f"Entering invalid email: {user['email']}")
    email = driver.find_element(By.ID, "input-email")
    email.clear()
    email.send_keys(user["email"])

    logger.info("Entering password")
    password = driver.find_element(By.ID, "input-password")
    password.clear()
    password.send_keys(user["password"])

    logger.info("Clicking Login button")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    # Wait for warning message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    warning_text = driver.find_element(By.CLASS_NAME, "alert-danger").text
    logger.info(f"Warning message displayed: invalid email format ")

    assert "No match" in warning_text

    logger.info("RESULT: Invalid login validation successful")
    logger.info("========== END TEST ==========\n")