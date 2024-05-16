from behave import *
from behave.api.async_step import async_run_until_complete

from models.account_page import AccountPage
from models.base_page import BasePage
from models.login_page import LoginPage

import configparser

config = configparser.ConfigParser()
config.read('config/credential.ini')


@given('the login page is open')
@async_run_until_complete
async def open_login_url(context):
    login_page = LoginPage(context.page)
    await login_page.navigate()


@when('i fill "{field}" on Login page')
@async_run_until_complete
async def fill_login_page_field(context, field: str):
    """
    :param value:
    :param field:
    :type context: behave.runner.Context
    """

    login_page = LoginPage(context.page)
    await login_page.fill_form_field(field, config.get('Credentials', field))


@when('i click "{action}" button on the login page')
@async_run_until_complete
async def click_login_page_button(context, action: str):
    """
    :param action:
    :type context: behave.runner.Context
    """
    login_page = LoginPage(context.page)
    await login_page.click_button(action)


@then('the next page is "{title}" page')
@async_run_until_complete
async def is_next_page(context, title: str):
    """
    :param title:
    :type context: behave.runner.Context
    """
    base_page = BasePage(context.page)
    await base_page.is_title_contains(title)


@then('the welcome text on Account page contains the value "{user}"')
@async_run_until_complete
async def step_impl(context, user: str):
    """
    :param user:
    :type context: behave.runner.Context
    """
    account_page = AccountPage(context.page)
    assert await account_page.is_welcome_text_contains(user)