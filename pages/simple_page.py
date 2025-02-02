from playwright.sync_api import expect
from pages.base_page import BasePage


class SimplePage(BasePage):
    BUTTON = '#submit-id-submit'
    RESULT = '#result-text'
    url = 'https://www.qa-practice.com/elements/button/simple'

    def click_button(self):
        button = self.page.locator(self.BUTTON)
        button.click()

    def check_button_exists(self):
        button = self.page.locator(self.BUTTON)
        expect(button).to_be_visible()

    def check_result_text_is_(self, text):
        result = self.page.locator(self.RESULT)
        expect(result).to_have_text(text)
