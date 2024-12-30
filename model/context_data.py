from behave.runner import Context

from model.webdriver.chrome_driver import Driver


class AdditionalContext(Context):
    def __init__(self, context):
        super(AdditionalContext, self).__init__(context)
        self.driver = Driver()
