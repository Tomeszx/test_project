from model.errors.base import BaseError


class NoResultsFound(BaseError):
    def __init__(self, url: str):
        message = f"No results found under the {url=}"
        super().__init__(message)


class PageNotFoundError(BaseError):
    def __init__(self, url: str):
        message = f"Page not found was displayed under the {url=}"
        super().__init__(message)


class InternalServerError(BaseError):
    def __init__(self, url: str):
        message = f"Internal Server Error was displayed under the {url=}"
        super().__init__(message)
