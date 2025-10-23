from selenium.webdriver.common.by import By

from pages.base_page import Page


class SigninPage(Page):
    EMAIL_FIELD_NAME = (By.ID, 'email-2')
    PASSWORD_FIELD_NAME = (By.ID, 'field')
    SUBMIT_BUTTON_NAME = (By.XPATH, "//a[@wized='loginButton']")

    def open_signin_page(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def signin_successfully(self, email, password):
        self.input_text(email, *self.EMAIL_FIELD_NAME)
        self.input_text(password, *self.PASSWORD_FIELD_NAME)
        self.wait_until_clickable_then_click(*self.SUBMIT_BUTTON_NAME)
