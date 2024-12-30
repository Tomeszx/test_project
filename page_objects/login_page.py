from model.elements.button import Button
from model.elements.element import Element
from model.elements.input import Input
from model.errors.element import ElementNotVisibleError
from model.webdriver.chrome_driver import Driver


class LoginPage:

    def __init__(self, driver: Driver):
        self.driver = driver
        self.username_input = Input(driver, '#username')
        self.password_input = Input(driver, '#password')
        self.login_button = Button(driver, '#submit')
        self.header_title = Element(driver, 'h1[class="post-title"]')
        self.error_message = Element(driver, '#error')

    def wait_for_page_content(self):
        self.login_button.wait_for_clickability(timeout=3, error_msg='The page was not fully loaded')

    def is_login_button_displayed(self) -> bool:
        return self.login_button.is_present_now()

    def fill_username_field(self, value: str) -> None:
        self.username_input.value = value

    def fill_password_field(self, value: str) -> None:
        self.password_input.value = value

    def click_login_button(self) -> None:
        self.login_button.click()

    def get_header_title(self) -> str:
        return self.header_title.text

    def is_logout_button_clickable(self) -> bool:
        return self.header_title.is_clickable(timeout=2)

    def get_error_message(self) -> str:
        if not self.error_message.is_visible(timeout=2):
            raise ElementNotVisibleError(str(self.error_message), self.driver.current_url)
        return self.error_message.text
