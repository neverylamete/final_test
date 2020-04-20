import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage

from .pages.locators import Sites
from .pages.locators import MainPageLocators

SITE_LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    link = Sites.MAIN_PAGE_SITE
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_link()
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
    page = LoginPage(page.browser, page.browser.current_url)
    page.should_be_login_page()
    # time.sleep(5)
