from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from model.elements.baseElement import BaseElement
from model.errors.element import DropdownOptionAlreadySelectedError, DropdownOptionNotSelectedError


class Checkbox(BaseElement):

    def __init__(self, driver: WebDriver, selector: str, locator: str = By.XPATH):
        super(Checkbox, self).__init__(driver, selector, locator)

    def is_checked(self) -> bool:
        return self.element.is_selected()

    def check(self) -> None:
        if self.is_checked():
            raise DropdownOptionAlreadySelectedError(str(self), 'Element is already checked')
        self.element.click()

    def uncheck(self) -> None:
        if not self.is_checked():
            raise DropdownOptionNotSelectedError(str(self), 'Element is not checked')
        self.element.click()
