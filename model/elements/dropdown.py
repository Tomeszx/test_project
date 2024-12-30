from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from model.elements.baseElement import BaseElement


class SelectDropdown(BaseElement):

    def __init__(self, driver: WebDriver, selector: str, locator: str = By.XPATH):
        super(SelectDropdown, self).__init__(driver, selector, locator)

    @property
    def option(self) -> str:
        return Select(self.element).first_selected_option.get_attribute('value')

    @option.setter
    def option(self, option: str) -> None:
        Select(self.element).select_by_value(option)

    @property
    def option_index(self) -> int:
        return int(Select(self.element).first_selected_option.get_attribute('index'))

    @option_index.setter
    def option_index(self, index: int) -> None:
        Select(self.element).select_by_index(index)
