from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from model.elements.base_element import BaseElement


class Button(BaseElement):

    def __init__(self, driver: WebDriver, selector: str, locator: str = By.CSS_SELECTOR):
        super(Button, self).__init__(driver, selector, locator)
