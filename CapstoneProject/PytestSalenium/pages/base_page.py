from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from utilities.config_reader import get_explicit_wait
from utilities.logger import get_logger
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, get_explicit_wait())
        self.logger = get_logger()

    def find(self, locator):
        self.logger.info(f"Finding element: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def click(self, locator):
        for _ in range(3):
            try:
                self.logger.info(f"Clicking element: {locator}")
                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )

                assert element.is_displayed(), f"{locator} not visible"
                assert element.is_enabled(), f"{locator} not enabled"

                element.click()
                time.sleep(1.2)
                return

            except StaleElementReferenceException:
                time.sleep(1)

        raise Exception(f"{locator} not clickable after retries")

    def type(self, locator, text):
        element = self.find(locator)

        assert element.is_displayed(), f"{locator} not visible for typing"

        element.clear()
        element.send_keys(text)

        self.logger.info(f"Typed '{text}' into {locator}")
        time.sleep(1.2)

    def get_text(self, locator):
        element = self.find(locator)
        return element.text
