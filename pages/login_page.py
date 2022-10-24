import time
import allure
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage
from .locators import LoginPageLocators
from ..utilits.exceptions import DdosVerificationError


class LoginPage(BasePage):

    @allure.step('User authentication')
    def authentication_user(self, username, password):
        """user authentication"""
        login_field = self.wait.until(
            ec.visibility_of_element_located(LoginPageLocators.LOGIN_FIELD))
        login_field.send_keys(username)

        password_field = self.wait.until(
            ec.visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        password_field.send_keys(password)

        self.get_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

        if "verified-device" in self.browser.current_url:
            with allure.step("Test failed due to DDoS protection"):
                self.browser.get_screenshot_as_file("screens/screen_shot_verified_device.png")
                raise DdosVerificationError
            # print("For authentication take number")
            # self.browser.get_screenshot_as_file("screens/screen_shot_verified_device.png")
            # time.sleep(30)


    @allure.step('Check login-form on page')
    def should_be_login_form(self):
        """Реализуем проверку на форму логина"""
        assert self.browser_helper.is_element_present(*LoginPageLocators.LOGIN_FORM), "There isnt login_form on page"

