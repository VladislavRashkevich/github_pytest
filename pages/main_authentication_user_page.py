from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage
from .locators import MainAuthenticationUserPageLocators


class MainAuthenticationUserPage(BasePage):

    def go_to_page_for_create_new_repository(self):
        new_button = WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable(MainAuthenticationUserPageLocators.CREATE_NEW_REPOSITORY_BUTTON))
        new_button.click()

