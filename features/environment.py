from behave.model import Scenario
from model.context_data import AdditionalContext, Pages
from model.webdriver.chrome_driver import Driver


def before_scenario(context: AdditionalContext, _: Scenario):
    context.driver = Driver()
    context.pages = Pages(context.driver)


def after_scenario(context: AdditionalContext, _: Scenario):
    context.driver.quit()
