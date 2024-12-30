from behave import given, then
from model.context_data import AdditionalContext


@given('the website "{website}" has been opened')
def step_impl(context: AdditionalContext, website: str):
    context.pages.base_page.open(website)
    current_url = context.driver.current_url
    if website not in current_url:
        raise Exception(f"There is wrong page opened. The '{website}' is not a part of URL: '{current_url}'")


@then("the url ends with '{path}'")
def step_impl(context: AdditionalContext, path: str):
    current_url = context.driver.current_url
    assert context.driver.current_url.endswith(path), f'The {current_url=} not ends with {path=}'