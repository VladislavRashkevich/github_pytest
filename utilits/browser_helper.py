from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ..config import WAIT_TIME

class BrowserHelper():

    def __init__(self, browser, wait_time=WAIT_TIME, wait=WebDriverWait):
        self.browser = browser
        self.wait_time = wait_time
        self.wait = wait(self.browser, self.wait_time)

    def element_is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def send_keys_in_element(self, element, value):
        element.send_keys(value)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True