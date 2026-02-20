from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    # -------- LOGIN LOCATORS --------
    my_account = (By.LINK_TEXT, "My Account")
    login_link = (By.LINK_TEXT, "Login")

    email = (By.ID, "input-email")
    password = (By.ID, "input-password")
    login_btn = (By.XPATH, "//input[@value='Login']")

    login_error = (By.CSS_SELECTOR, ".alert-danger")

    # -------- REGISTER LOCATORS --------
    continue_register = (By.LINK_TEXT, "Continue")

    firstname = (By.ID, "input-firstname")
    lastname = (By.ID, "input-lastname")
    reg_email = (By.ID, "input-email")
    telephone = (By.ID, "input-telephone")
    reg_password = (By.ID, "input-password")
    confirm_password = (By.ID, "input-confirm")

    newsletter_no = (By.XPATH, "//input[@name='newsletter' and @value='0']")
    privacy_policy = (By.NAME, "agree")
    register_btn = (By.XPATH, "//input[@value='Continue']")

    success_continue = (By.LINK_TEXT, "Continue")

    # ----------------------------------

    def open_login(self):
        self.click(self.my_account)
        self.click(self.login_link)

    def login(self, user, pwd):

        # Try login first
        self.type(self.email, user)
        self.type(self.password, pwd)
        self.click(self.login_btn)

        # If login failed → register
        if "No match for E-Mail Address and/or Password" in self.driver.page_source:

            # Go to register page
            self.click(self.my_account)
            self.click(self.login_link)
            self.click(self.continue_register)

            # Fill registration form
            self.type(self.firstname, "Auto")
            self.type(self.lastname, "User")
            self.type(self.reg_email, user)
            self.type(self.telephone, "9999999999")
            self.type(self.reg_password, pwd)
            self.type(self.confirm_password, pwd)

            self.click(self.newsletter_no)
            self.click(self.privacy_policy)
            self.click(self.register_btn)

            # After successful registration click Continue
            if "Your Account Has Been Created!" in self.driver.page_source:
                self.click(self.success_continue)

            # STOP HERE — user is already logged in

