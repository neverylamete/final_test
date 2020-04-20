from selenium.webdriver.common.by import By


class Sites:
    MAIN_PAGE_SITE = "http://selenium1py.pythonanywhere.com/"
    # LOGIN_PAGE_SITE = 1


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
