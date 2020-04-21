from selenium.webdriver.common.by import By


class Sites:
    MAIN_PAGE_SITE = "http://selenium1py.pythonanywhere.com/"
    # PRODUCT_SITE_NEW_YEAR = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_SITE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    PRODUCT_IN_MSG_ADDED = (By.CSS_SELECTOR, "div.alertinner>strong")
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, "div > h1")

    PRODUCT_PRICE_COLOR = (By.CSS_SELECTOR, "div>p.price_color")
    BASKET_PRICE_IN_MSG = (By.CSS_SELECTOR, "div.alertinner>p>strong")
