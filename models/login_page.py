from playwright.async_api import Page

from models.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.locator("//input[@data-testid='i0116']")
        self.password = page.locator("//input[@data-testid='i0118']")
        self.submit = page.locator("//button[@type='submit']")
        self.reset_password = page.get_by_role('button', name='Forgot Password')
        self.next_button = page.locator("//button[@type='submit']")
        self.stay_signed_no = page.locator("//button[@id='declineButton']")

    async def navigate(self):
        await self.page.goto("https://login.live.com", timeout=5000)

    async def fill_username(self, text):
        await self.username.fill(text)

    async def fill_password(self, text):
        await self.password.fill(text)

    async def submit_login(self):
        await self.submit.click()

    async def fill_form_field(self, field, value):
        if field == "username":
            await self.fill_username(value)
        elif field == "password":
            await self.fill_password(value)
        else:
            assert False

    async def click_button(self, action):
        if action == "submit":
            await self.submit_login()
        elif action == "forgot password":
            await self.reset_password.click()
        elif action == "next":
            await self.next_button.click()
        elif action == "stay signed no":
            await self.stay_signed_no.click()
        else:
            assert False

    async def is_error_message_displayed(self):
        return await self.page.wait_for_selector(".error-text", state="visible", timeout=5000)