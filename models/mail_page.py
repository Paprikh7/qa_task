import os

from playwright.async_api import Page
from playwright.async_api import expect

from models.account_page import AccountPage
from models.base_page import BasePage


class MailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.new_mail_button = page.locator("(//span[@class='flexContainer-158'])[1]")
        self.to_button = page.locator("//div[text()='To']")
        self.my_contacts_button = page.locator("//button[text()='My Contacts']")
        self.add_address_button = page.locator("//i[@data-icon-name='Add']")
        self.add_person_save_button = page.locator("(//button[contains(@class,'ms-Button ms-Button--primary')])[2]")
        self.attachment_button = page.locator("(//button[@data-ktp-execute-target='ktp-m-a-f']//span)[1]")
        self.attachment_from_pc_button = page.locator("//span[text()='Browse this computer']")
        self.subject_input = page.locator("//input[contains(@class,'ms-TextField-field ADopl')]")
        self.mail_input = page.locator("//div[contains(@class,'___1mtnehv fwg0e2s')]")
        self.send_mail_button = page.locator("(//span[@class='ms-Button-label label-161'])[2]")
        self.mail_panel = page.locator("(//div[@class='FiPRo']//div)[1]")
        self.mail = page.locator("(//div[@class='jGG6V gDC9O'])")
        self.image_attachment = page.locator("//div[@aria-label='image attachments']")

    async def navigate(self):
        await self.page.goto("https://outlook.live.com/mail/", timeout=5000)

    async def fill_subject(self, text):
        await self.subject_input.fill(text)

    async def fill_mail(self, text):
        await self.mail_input.fill(text)

    async def fill_mail_field(self, field, value):
        if field == "subject":
            await self.fill_subject(value)
        elif field == "user mail":
            await self.fill_mail(value)
        else:
            assert False

    async def upload_attachment(self):
        async with self.page.expect_file_chooser() as fc_info:
            await self.attachment_from_pc_button.click()
        current_working_dir = os.getcwd()
        file_path = os.path.join(current_working_dir, 'attachments/attachment.jpg')
        file_chooser = await fc_info.value
        await file_chooser.set_files(file_path)

        await self.page.wait_for_timeout(2000)

    async def click_button(self, action):
        if action == "new mail":
            await self.new_mail_button.click()
        elif action == "address book":
            await self.to_button.click()
        elif action == "my contacts":
            await self.my_contacts_button.click()
        elif action == "add person":
            await self.add_address_button.click()
        elif action == "save added person":
            await self.add_person_save_button.click()
        elif action == "add attachment":
            await self.attachment_button.click()
        elif action == "send mail":
            await self.send_mail_button.click()
        else:
            assert False

    async def is_mail_delivered(self, value: str):
        await expect(self.mail_panel).to_contain_text(value, timeout=10000)

    async def open_first_mail(self, context):
        account_page = AccountPage(context.page)
        await expect(account_page.close_notification_button).to_be_visible()
        await self.mail.nth(0).click()

    async def check_attachment(self):
        await expect(self.image_attachment).to_be_visible()