from contextlib import contextmanager
from typing import Generator
from selenium.webdriver.common.by import By
from model.elements.baseElement import BaseElement
from model.webdriver.chrome_driver import Driver


class Iframe(BaseElement):
    def __init__(self, driver: Driver, selector: str, locator: str = By.XPATH):
        super(Iframe, self).__init__(driver, selector, locator)

    @contextmanager
    def switch_to(self) -> Generator[None, None, None]:
        """Context manager to wait for an iframe to be visible, switch to it, and then automatically switch back."""
        self._check_if_with_statement_is_used()
        self.driver.switch_to.frame(self.element)
        try:
            yield None
        finally:
            self.driver.switch_to.parent_frame()
