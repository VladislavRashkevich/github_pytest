from selenium.webdriver.common.by import By
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



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

    def open(self):
        self.browser.get(self.url)

    def get_element(self, how, what):
        return self.browser.find_element(how, what)

    def go_to_login_page(self):
        login_link = WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable(BasePageLocators.LOGIN_LINK))
        login_link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User was not authorized"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present in page"
