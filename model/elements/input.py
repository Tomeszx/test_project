from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from model.elements.base_element import BaseElement


class Input(BaseElement):

    def __init__(self, driver: WebDriver, selector: str, locator: str = By.CSS_SELECTOR):
        super(Input, self).__init__(driver, selector, locator)

    @property
    def value(self) -> str:
        return self.get_attribute('value')

    @value.setter
    def value(self, value: str) -> None:
        self.element.send_keys(value)

    @value.deleter
    def value(self) -> None:
        self.element.clear()
