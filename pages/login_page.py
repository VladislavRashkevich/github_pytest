from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
import time


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

        self.username = "VladislavTest"
        self.password = "SecondTestAcc123"

    @allure.step('authentication user')
    def authentication_user(self):
        """Аутентификация пользователя"""
        login_field = WebDriverWait(self.browser, 7).until(
            ec.visibility_of_element_located(LoginPageLocators.LOGIN_FIELD))
        login_field.send_keys(self.username)

        password_field = WebDriverWait(self.browser, 7).until(
            ec.visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        password_field.send_keys(self.password)

        self.get_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

        if "verified-device" in self.browser.current_url:
            print("For authentication take number")
            self.browser.get_screenshot_as_file("screens/screen_shot_verified_device.png")
            time.sleep(30)

    @allure.step('Check "login" in URL')
    def should_be_login_url(self):
        """Рнализуем проверку на корректный URL-адресс"""
        assert "login" in self.browser.current_url, "Login is not present in this URL"

    @allure.step('Check login-gorm on page')
    def should_be_login_form(self):
        """Реализуем проверку на форму логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There isnt login_form on page"

