from pages.base_page import Page
from pages.main_page import MainPage
from pages.signin_page import SigninPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(driver)
        self.signin_page = SigninPage(driver)
        self.main_page = MainPage(driver)
