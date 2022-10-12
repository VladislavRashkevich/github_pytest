from .base_page import BasePage
from .locators import RepositoryPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class RepositoryPage(BasePage):

    def go_to_repository_setting(self):
        setting_tab = WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable(RepositoryPageLocators.SETTING_REPOSITORY_TAB))
        setting_tab.click()




