from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException

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

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Element not present in page"