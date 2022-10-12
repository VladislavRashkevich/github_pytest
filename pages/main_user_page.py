from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage
from .locators import MainUserPageLocators


class MainUserPage(BasePage):

    def go_to_page_for_create_new_repository(self):
        new_button = WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable(MainUserPageLocators.CREATE_NEW_REPOSITORY_BUTTON))
        new_button.click()

    # def get_all_repositories(self):
    #     elements = WebDriverWait(self.browser, 5).until(ec.presence_of_all_elements_located())
    #     return


    def go_to_repository_page(self):
        repository_link = self.browser.find_element(*MainUserPageLocators.REPOSITORY_LINK)
        repository_link.click()
        # link = self.browser.current_url + '/' + username + '/' + repository_name
        # self.browser.get(link)
