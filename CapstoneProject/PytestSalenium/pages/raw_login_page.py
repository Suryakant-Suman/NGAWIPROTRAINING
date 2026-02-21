from selenium.webdriver.common.by import By


class RawLoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.find_element(By.LINK_TEXT, "My Account").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()

    def enter_email(self, email):
        field = self.driver.find_element(By.ID, "input-email")
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = self.driver.find_element(By.ID, "input-password")
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def get_warning_message(self):
        return self.driver.page_source