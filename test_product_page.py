import time
import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.locators import Sites
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param(
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                       marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# @pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    # open product page
    site_url = Sites.PRODUCT_SITE_NEW_YEAR
    # site_url=link
    page = ProductPage(browser, site_url)
    page.open()
    # assets
    page.should_be_product_page()
    # click add to basket
    page.add_to_basket()
    # solve the alert windows
    page.solve_quiz_and_get_code()
    page.should_be_product_in_msg_added()
    page.should_be_basket_price_for_one_product()
    # time.sleep(50)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    site_url = Sites.PRODUCT_SITE_NEW_YEAR
    page = ProductPage(browser, site_url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_IN_MSG_ADDED), "fail 1 test, fail successful"


def test_guest_cant_see_success_message(browser):
    site_url = Sites.PRODUCT_SITE_NEW_YEAR
    page = ProductPage(browser, site_url)
    page.open()
    # page.add_to_basket()
    # page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_IN_MSG_ADDED), "fail 2 test"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    site_url = Sites.PRODUCT_SITE_NEW_YEAR
    page = ProductPage(browser, site_url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    assert page.is_disappeared(*ProductPageLocators.PRODUCT_IN_MSG_ADDED), "fail 3 test, fail successful"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = Sites.PRODUCT_SITE
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_be_basket_link()
    page.go_to_basket_page()
    page = BasketPage(page.browser, page.browser.current_url)
    page.should_be_basket_empty()
    page.should_be_basket_empty_text()
    # time.sleep(5)


@pytest.mark.smoke
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = Sites.MAIN_PAGE_SITE
        page = MainPage(browser, link)
        page.open()  # открываем страницу
        page.should_be_login_link()
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        page = LoginPage(page.browser, page.browser.current_url)
        page.register_new_user(str(time.time()) + "@fakemail.org", "selenium1py")
        page.should_be_authorized_user()
        yield
        print(1)

    def test_user_cant_see_success_message(self, browser):
        site_url = Sites.PRODUCT_SITE
        page = ProductPage(browser, site_url)
        page.open()
        # page.add_to_basket()
        # page.solve_quiz_and_get_code()

        assert page.is_not_element_present(*ProductPageLocators.PRODUCT_IN_MSG_ADDED), "fail 2 test"

    def test_user_can_add_product_to_basket(self, browser):
        # open product page
        site_url = Sites.PRODUCT_SITE
        # site_url=link
        page = ProductPage(browser, site_url)
        page.open()
        # assets
        page.should_be_product_page()
        # click add to basket
        page.add_to_basket()
        # solve the alert windows
        # page.solve_quiz_and_get_code()
        page.should_be_product_in_msg_added()
        page.should_be_basket_price_for_one_product()
        time.sleep(50)
