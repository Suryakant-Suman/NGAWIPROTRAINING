from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config_reader import get_explicit_wait
from utilities.logger import get_logger


logger = get_logger()


def assert_element_present(driver, locator):
    logger.info(f"Checking presence of element: {locator}")
    element = WebDriverWait(driver, get_explicit_wait()).until(
        EC.presence_of_element_located(locator)
    )
    assert element is not None, f"Element {locator} not present"
    return element


def assert_element_visible(driver, locator):
    logger.info(f"Checking visibility of element: {locator}")
    element = WebDriverWait(driver, get_explicit_wait()).until(
        EC.visibility_of_element_located(locator)
    )
    assert element.is_displayed(), f"Element {locator} not visible"
    return element


def assert_element_clickable(driver, locator):
    logger.info(f"Checking clickability of element: {locator}")
    element = WebDriverWait(driver, get_explicit_wait()).until(
        EC.element_to_be_clickable(locator)
    )
    assert element.is_enabled(), f"Element {locator} not clickable"
    return element


def assert_text_present(driver, text):
    logger.info(f"Checking text presence: '{text}'")
    assert text.lower() in driver.page_source.lower(), \
        f"Text '{text}' not found on page"


def assert_title_contains(driver, text):
    logger.info(f"Checking title contains: '{text}'")
    assert text.lower() in driver.title.lower(), \
        f"Title does not contain '{text}'. Actual: {driver.title}"


def assert_url_contains(driver, text):
    logger.info(f"Checking URL contains: '{text}'")
    assert text.lower() in driver.current_url.lower(), \
        f"URL does not contain '{text}'. Actual: {driver.current_url}"
