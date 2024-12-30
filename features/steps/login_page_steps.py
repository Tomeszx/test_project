from behave import given, when, then
from model.context_data import AdditionalContext


@given('the login page is fully loaded')
def step_impl(context: AdditionalContext):
    context.pages.login_page.wait_for_page_content()


@when("i fill username field with '{value}'")
def step_impl(context: AdditionalContext, value: str):
    context.pages.login_page.fill_username_field(value)


@when("i fill password field with '{value}'")
def step_impl(context: AdditionalContext, value: str):
    context.pages.login_page.fill_password_field(value)


@when("i click to login button")
def step_impl(context: AdditionalContext):
    context.pages.login_page.click_login_button()


@then("the user is still on login page")
def step_impl(context: AdditionalContext):
    is_login_page = context.pages.login_page.is_login_button_displayed()
    assert is_login_page, 'The login page was not displayed'


@then("the header title is '{expected_value}'")
def step_impl(context: AdditionalContext, expected_value: str):
    title = context.pages.login_page.get_header_title()
    assert title == expected_value, f'The success title was not displayed. Instead it is {title=}'


@then("the logout button is clickable")
def step_impl(context: AdditionalContext):
    is_clickable = context.pages.login_page.is_logout_button_clickable()
    assert is_clickable, 'The logout button is not clickable'


@then("the login error message is displayed with '{expected_value}'")
def step_impl(context: AdditionalContext, expected_value: str):
    error_msg = context.pages.login_page.get_error_message()
    assert error_msg == expected_value, f'Wrong error message was displayed {error_msg=}'
