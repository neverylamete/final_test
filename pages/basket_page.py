from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_text(self):
        element = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT_CSS)
        select = self.browser.find_element(*BasePageLocators.LANGUAGE_CHOICE)
        text = select.get_attribute("value")
        # print(BasketPageLocators.BASKET_EMPTY_TEXT[text])
        # print(element.text.strip())
        # print(BasketPageLocators.BASKET_EMPTY_TEXT[text] in element.text.strip())
        assert BasketPageLocators.BASKET_EMPTY_TEXT[text] in element.text.strip(), \
            "basket is not empty or text is another"

    def should_be_basket_not_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_NOT_EMPTY_CSS), "basket is empty"

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY_CSS), "basket is not empty"
