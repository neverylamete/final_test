import time
import pytest

from .pages.product_page import ProductPage
from .pages.locators import Sites
from .pages.locators import ProductPageLocators


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# @pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser, link):
    # open product page
    # link = Sites.NEW_YEAR_PRODUCT_SITE
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    page = ProductPage(browser, link)
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
    site_url = Sites.PRODUCT_SITE
    page = ProductPage(browser, site_url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_IN_MSG_ADDED), "fail 1 test"


def test_guest_cant_see_success_message(browser):
    site_url = Sites.PRODUCT_SITE
    page = ProductPage(browser, site_url)
    page.open()
    # page.add_to_basket()
    # page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_IN_MSG_ADDED), "fail 2 test"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    site_url = Sites.PRODUCT_SITE
    page = ProductPage(browser, site_url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    assert page.is_disappeared(*ProductPageLocators.PRODUCT_IN_MSG_ADDED), "fail 3 test"
