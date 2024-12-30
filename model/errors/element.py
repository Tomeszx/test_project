from model.errors.base import BaseError


class ElementNotVisibleError(BaseError):
    def __init__(self, element: str, url: str, *messages: str):
        base_msg = f"The {element} is not visible."
        super().__init__(base_msg, f'{url=}', *messages)


class ElementVisibleError(BaseError):
    def __init__(self, element: str, url: str, *messages: str):
        base_msg = f"The {element} should not be visible."
        super().__init__(base_msg, f'{url=}', *messages)


class ElementNotClickableError(BaseError):
    def __init__(self, element: str, url: str, *messages: str):
        base_msg = f"The {element=} is not clickable."
        super().__init__(base_msg, f'{url=}', *messages)


class ElementNotFoundError(BaseError):
    def __init__(self, element: str, url: str, *messages: str):
        base_msg = f"The {element=} was not found"
        super().__init__(base_msg, f'{url=}', *messages)


class DropdownOptionNotFoundError(BaseError):
    def __init__(self, element: str, *messages: str):
        base_msg = f"The {element=} was not found"
        super().__init__(base_msg, *messages)


class DropdownOptionAlreadySelectedError(BaseError):
    def __init__(self, element: str, *messages: str):
        base_msg = f"The {element=} was not found"
        super().__init__(base_msg, *messages)


class DropdownOptionNotSelectedError(BaseError):
    def __init__(self, element: str, *messages: str):
        base_msg = f"The {element=} was not found"
        super().__init__(base_msg, *messages)


class ElementPositionError(BaseError):
    def __init__(self, element: str, url: str, *messages: str):
        base_msg = f"The {element=} is in incorrect position{' '*8}"
        super().__init__(base_msg, f'{url=}', *messages)
