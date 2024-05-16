from behave import *
from behave.api.async_step import async_run_until_complete

from models.account_page import AccountPage


@when('i navigate to "{action}" from the account page')
@async_run_until_complete
async def click_account_page_button(context, action: str):
    """
    :param action:
    :type context: behave.runner.Context
    """
    account_page = AccountPage(context.page)
    await account_page.navigate_to(action)


@then('User logout')
@async_run_until_complete
async def logout(context):
    """
    :type context: behave.runner.Context
    """
    account_page = AccountPage(context.page)
    await account_page.logout()
