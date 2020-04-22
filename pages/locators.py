from selenium.webdriver.common.by import By


class Sites:
    MAIN_PAGE_SITE = "http://selenium1py.pythonanywhere.com/"
    PRODUCT_SITE_NEW_YEAR = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_SITE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span>a.btn.btn-default[href*='basket']")
    LANGUAGE_CHOICE = (By.CSS_SELECTOR, "div>.form-control[name='language']> option[selected]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form input[type='email']")
    REGISTER_PASS = (By.CSS_SELECTOR, "#register_form input[type='password']")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    PRODUCT_IN_MSG_ADDED = (By.CSS_SELECTOR, "div.alertinner>strong")
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, "div > h1")

    PRODUCT_PRICE_COLOR = (By.CSS_SELECTOR, "div>p.price_color")
    BASKET_PRICE_IN_MSG = (By.CSS_SELECTOR, "div.alertinner>p>strong")


class BasketPageLocators:
    BASKET_NOT_EMPTY_CSS = (By.CSS_SELECTOR, "#content_inner>div.basket-title")
    BASKET_EMPTY_TEXT_CSS = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_LANGUAGE_CSS = (By.CSS_SELECTOR, "#content_inner>p>a")
    BASKET_EMPTY_TEXT = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en-gb": "Your basket is empty.",
        "en": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
    }
