import threading

from behave.model import Scenario
from behave.runner import Context
from model.context_data import AdditionalContext
from model.webdriver.chrome_driver import Driver
from retry import retry


@retry(TimeoutError, tries=3)
def process_clearing_browser_data(browser: Driver):
    thread = threading.Thread(
        target=browser.execute, args=(
            f'SEND_COMMAND_{browser.session_id}',
            dict(cmd='Storage.clearDataForOrigin', params={"origin": '*', "storageTypes": 'all'})
        )
    )
    thread.start()
    thread.join(timeout=6)
    if thread.is_alive():
        raise TimeoutError('The browser data was not properly cleared')



def before_all(context: Context):
    context = AdditionalContext(context)


def before_scenario(context: AdditionalContext, scenario: Scenario):
    process_clearing_browser_data(context.driver)


def after_all(context: AdditionalContext):
    context.driver.quit()
