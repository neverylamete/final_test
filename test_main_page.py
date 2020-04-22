import pytest
import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

from .pages.locators import Sites
from .pages.locators import MainPageLocators


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = Sites.MAIN_PAGE_SITE
        page = MainPage(browser, link)
        page.open()  # открываем страницу
        page.should_be_login_link()
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        page = LoginPage(page.browser, page.browser.current_url)
        page.should_be_login_page()
        # time.sleep(5)

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = Sites.MAIN_PAGE_SITE
        page = MainPage(browser, link)
        page.open()  # открываем страницу
        page.should_be_basket_link()
        page.go_to_basket_page()
        page = BasketPage(page.browser, page.browser.current_url)
        page.should_be_basket_empty()
        page.should_be_basket_empty_text()
        # time.sleep(5)
