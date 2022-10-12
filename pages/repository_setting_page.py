from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage
from .locators import RepositorySettingPageLocators

class RepositorySettingPage(BasePage):

    def rename_repository(self, new_name_repository):
        rename_field = WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(RepositorySettingPageLocators.RENAME_FIELD))
        rename_field.clear()
        rename_field.send_keys(new_name_repository)
        rename_button = WebDriverWait(self.browser, 7).until(ec.element_to_be_clickable(RepositorySettingPageLocators.RENAME_BUTTON))
        rename_button.click()

    def should_be_rename_repository(self, new_name_repository):
        assert new_name_repository in self.browser.current_url, "Repository did not rename"


    def delete_repository(self):
        pass
