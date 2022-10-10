from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def authentication_user(self, username, password):
        """Аутентификация пользователя"""
        login_field = self.get_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(username)
        password_field = self.get_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        self.get_element(*LoginPageLocators.SIGN_IN_BUTTON).click()


    def should_be_login_url(self):
        """Рнализуем проверку на корректный URL-адресс"""
        assert "login" in self.browser.current_url, "Login is not present in this URL"

    def should_be_login_form(self):
        """Реализуем проверку на форму логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There isnt login_form on page"

