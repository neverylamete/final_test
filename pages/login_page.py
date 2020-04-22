from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "LoginPage assert, url don't contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form don't find"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form don't find"

    def register_new_user(self, email, password):
        element = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        element.send_keys(email)
        element = self.browser.find_elements(*LoginPageLocators.REGISTER_PASS)
        for it in element:
            it.send_keys(password)
        element = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        element.click()

