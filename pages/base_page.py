import allure
from test_first_task.config import WAIT_TIME
from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_first_task.utilits.browser_helper import BrowserHelper


class BasePage():
    def __init__(self, browser, url, timeout=WAIT_TIME, browser_helper=BrowserHelper):
        self.url = url
        self.browser = browser
        self.timeout = timeout
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.browser_helper = browser_helper(self.browser)

    @allure.step("Open page")
    def open(self):
        self.browser.get(self.url)

    def get_element(self, how, what):
        return self.browser.find_element(how, what)

    @allure.step("Open login page")
    def go_to_login_page(self):
        login_link = self.wait.until(ec.element_to_be_clickable(BasePageLocators.LOGIN_LINK))
        login_link.click()

    @allure.step("User authorization check")
    def should_be_authorized_user(self):
        assert self.browser_helper.is_element_present(*BasePageLocators.USER_ICON), "User was not authorized"

    @allure.step("Checking for a link to the login page")
    def should_be_login_link(self):
        assert self.browser_helper.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present in page"
