from behave import *
from behave.api.async_step import async_run_until_complete

from models.account_page import AccountPage
from models.base_page import BasePage
from models.login_page import LoginPage
from models.mail_page import MailPage


@when('i click on button "{action}" on the mail page')
@async_run_until_complete
async def click_mail_page_button(context, action: str):
    """
    :param action:
    :type context: behave.runner.Context
    """
    mail_page = MailPage(context.page)
    await mail_page.click_button(action)


@when('upload a attachment')
@async_run_until_complete
async def click_mail_page_button(context):
    """
    :type context: behave.runner.Context
    """
    mail_page = MailPage(context.page)
    await mail_page.upload_attachment()


@when('navigate to mailbox')
@async_run_until_complete
async def click_mail_page_button(context):
    """
    :type context: behave.runner.Context
    """
    mail_page = MailPage(context.page)
    await mail_page.navigate()


@when('i fill "{field}" on mail page with "{value}"')
@async_run_until_complete
async def fill_mail_page(context, field: str, value: str):
    """
    :type context: behave.runner.Context
    :param value:
    :param field:
    """
    mail_page = MailPage(context.page)
    await mail_page.fill_mail_field(field, value)


@then('Mail inbox contains new mail with subject text "{value}"')
@async_run_until_complete
async def is_email_send(context, value: str):
    mail_page = MailPage(context.page)
    await mail_page.is_mail_delivered(value)


@then('i open first mail')
@async_run_until_complete
async def open_first_mail(context):
    mail_page = MailPage(context.page)
    await mail_page.open_first_mail(context)


@then('i check if attachment is visible in the mail')
@async_run_until_complete
async def is_attachment_visible(context):
    mail_page = MailPage(context.page)
    await mail_page.check_attachment()
