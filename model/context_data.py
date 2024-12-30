from behave.runner import Context

from model.webdriver.chrome_driver import Driver
from page_objects.base_page import BasePage
from page_objects.login_page import LoginPage


class Pages:
    def __init__(self, driver: Driver):
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)


class AdditionalContext(Context):
    driver: Driver
    pages: Pages
