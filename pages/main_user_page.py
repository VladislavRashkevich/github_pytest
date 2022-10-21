from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage
from .locators import MainUserPageLocators
import allure


class MainUserPage(BasePage):

    @allure.step('Open page to create new repository')
    def go_to_page_for_create_new_repository(self):
        new_button = WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable(MainUserPageLocators.CREATE_NEW_REPOSITORY_BUTTON))
        new_button.click()

    @allure.step('Open repository page')
    def go_to_repository_page(self):
        repository_link = self.browser.find_element(*MainUserPageLocators.REPOSITORY_LINK)
        repository_link.click()

