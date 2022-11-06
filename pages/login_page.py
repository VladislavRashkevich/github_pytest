import time
import allure
from loguru import logger
from .base_page import BasePage
from .locators import LoginPageLocators
from ..utilits.exceptions import DdosVerificationError


class LoginPage(BasePage):

    locators = LoginPageLocators

    @allure.step('User authentication')
    def authentication_user(self, username, password):
        """user authentication"""
        login_field = self.browser_helper.element_is_visible(self.locators.LOGIN_FIELD)
        self.browser_helper.send_keys_in_element(login_field, username)

        password_field = self.browser_helper.element_is_visible(self.locators.PASSWORD_FIELD)
        self.browser_helper.send_keys_in_element(password_field, password)

        self.browser_helper.element_is_clickable(self.locators.SIGN_IN_BUTTON).click()

        if "verified-device" in self.browser.current_url:
            time.sleep(20)
            with allure.step("Test failed due to DDoS protection"):

                # allure.attach(self.browser.get_screenshot_as_png(), name="Bug screenshot", attachment_type=allure.attachment_type.PNG)
                logger.error("Test failed due to DDoS protection")
                raise DdosVerificationError
            # print("For authentication take number")
            # self.browser.get_screenshot_as_file("screens/screen_shot_verified_device.png")
            # time.sleep(30)

    @allure.step('Verification login-form on page')
    def should_be_login_form(self):
        """Verification a login form exists"""
        assert self.browser_helper.is_element_present(*LoginPageLocators.LOGIN_FORM_WEB_ELEMENT), "There isnt login_form on page"


