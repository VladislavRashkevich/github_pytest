from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure

class BasePage():
    def __init__(self, browser, url):
        self.url = url
        self.browser = browser

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    @allure.step("Open page")
    def open(self):
        self.browser.get(self.url)

    def get_element(self, how, what):
        return self.browser.find_element(how, what)

    @allure.step("Open login page")
    def go_to_login_page(self):
        login_link = WebDriverWait(self.browser, 8).until(ec.element_to_be_clickable(BasePageLocators.LOGIN_LINK))
        login_link.click()

    @allure.step("icon user is authentication")
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User was not authorized"

    @allure.step("login-link on the page")
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present in page"
