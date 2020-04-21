from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
import string


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_button_add_to_basket()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "button 'add to basket' don't  find"

    def should_be_basket_price_for_one_product(self):
        price_element = self.product_price()
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_MSG).text
        for i in basket_price:
            if i not in string.digits + ".,":
                basket_price = basket_price.replace(i, "")
        assert price_element.strip() == basket_price.strip(), "wrong price in basket and product"

    def should_be_product_in_msg_added(self):
        try:
            element_text = self.product_name()
            element = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_MSG_ADDED)
            product_name = element.text
        except NoSuchElementException:
            assert False, "No such element"
        assert element_text == product_name, "name of product is not the same in msg about added product"

    def add_to_basket(self):
        element = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        element.click()

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_NAME).text

    def product_price(self):
        element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_COLOR).text
        for i in element:
            if i not in string.digits + ".,":
                element = element.replace(i, "")
        return element
