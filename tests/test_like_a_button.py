from playwright.sync_api import Page
from pages.like_a_button import LikeButtonPage


def test_like_a_button_exists(page: Page):
    like_a_button = LikeButtonPage(page)
    like_a_button.open()
    like_a_button.check_button_exists()


def test_like_a_button_exists_click(page: Page):
    like_a_button = LikeButtonPage(page)
    like_a_button.open()
    like_a_button.click_button()
    like_a_button.check_result_text_is_('Submitted')
