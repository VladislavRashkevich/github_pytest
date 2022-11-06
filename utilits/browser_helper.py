import allure
from loguru import logger
from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ..config import WAIT_TIME
from .logger import LogConfig


class BrowserHelper():
    # Set required config for project logger
    LogConfig.set_logger_config()

    def __init__(self, browser, wait_time=WAIT_TIME, wait=WebDriverWait):
        self.browser = browser
        self.wait_time = wait_time
        self.wait = wait(self.browser, self.wait_time)

    @allure.step("Get visible element")
    def element_is_visible(self, locator):
        logger.info(f"Get visible {locator} element")
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            logger.exception(f"Timeout exception for element with locator - {locator}")

    @allure.step("Get all visible elements")
    def elements_are_visible(self, locator):
        logger.info(f"Get elements with locator - {locator}")
        try:
            element = self.wait.until(ec.visibility_of_all_elements_located(locator))
            return element
        except TimeoutException:
            logger.exception(f"Timeout exception for element with locator - {locator}")

    @allure.step("Get clickable element")
    def element_is_clickable(self, locator):
        logger.info(f"Element {locator} is clickable")
        try:
            element = self.wait.until(ec.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            logger.exception(f"Timeout exception for element with locator - {locator}")

    @allure.step("Send info in web-element")
    def send_keys_in_element(self, element, value):
        logger.info(f"Send information in {element}")
        element.send_keys(value)

    @allure.step("Verification is element present")
    def is_element_present(self, how, what):
        logger.info(f"Verification that element with locator {what} is present")
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            logger.exception("Element is not present")
            return False
        return True
