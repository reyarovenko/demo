from playwright.sync_api import expect


class LikeButtonPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto('https://www.qa-practice.com/elements/button/like_a_button')

    def click_button(self):
        button = self.page.locator('.a-button')
        button.click()

    def check_button_exists(self):
        button = self.page.locator('.a-button')
        expect(button).to_be_visible()

    def check_submitted_text(self):
        result = self.page.locator('#result-text')
        expect(result).to_have_text('Submitted')
