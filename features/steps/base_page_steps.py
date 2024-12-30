from behave import given
from model.context_data import AdditionalContext


@given('the website "{website}" has been opened and cookie has been accepted')
def step_impl(context: AdditionalContext, website: str):
    context.pages.cookie_confirmation_popup.disable_popup(context.env, context.market)
    context.pages.base_page.open(website, context.market, context.env)
    current_url = context.driver.current_url
    if website not in current_url:
        raise Exception(f"There is wrong page opened. The '{website}' is not a part of URL: '{current_url}'")
