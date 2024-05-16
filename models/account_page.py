from playwright.async_api import Page
from playwright.async_api import expect
import re
from models.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_text = page.locator("[id='welcome-text']")
        self.mail_button = page.locator("//a[@data-bi-id='home.cards.card.outlook.cold']")
        self.profile_button = page.locator("//div[@class='_8ZYZKvxC8bvw1xgQGSkvvA==']//img[1]")
        self.logout_button = page.locator("//a[contains(text(),'Sign out')]")
        self.close_notification_button = page.locator("//button[@title='Close']")

    async def profile_open(self):
        await self.profile_button.click()

    async def navigate_to(self, action):
        if action == "outlook":
            await self.mail_button.click()
        elif action == "account":
            await self.mail_button.click()
        else:
            assert False

    async def logout(self):
        await self.close_notification_button.click()
        await self.profile_open()
        await self.logout_button.click()
        await expect(self.page).to_have_url(re.compile(r"https://www.msn.com/"))
