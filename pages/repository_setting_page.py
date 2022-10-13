from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage
from .locators import RepositorySettingPageLocators

class RepositorySettingPage(BasePage):

    def delete_repository(self):
        delete_repository_button = WebDriverWait(self.browser, 7).until(
            ec.element_to_be_clickable(RepositorySettingPageLocators.DELETE_REPOSITORY_BUTTON)
        )
        delete_repository_button.click()

        string_to_confirm = WebDriverWait(self.browser, 5).until(
            ec.visibility_of_element_located(RepositorySettingPageLocators.STRING_TO_CONFIRM_FOR_DELETE_REPOSITORY)
        )

        field_to_confirm =  WebDriverWait(self.browser, 5).until(
            ec.visibility_of_element_located(RepositorySettingPageLocators.FIELD_TO_CONFIRM_FOR_DELETE_REPOSITORY)
        )
        field_to_confirm.send_keys(string_to_confirm.text)

        button_confirm = WebDriverWait(self.browser, 7).until(
            ec.element_to_be_clickable(RepositorySettingPageLocators.BUTTON_TO_CONFIRM_FOR_DELETE_REPOSITORY)
        )
        button_confirm.click()


    def rename_repository(self, new_name_repository):
        rename_field = WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(RepositorySettingPageLocators.RENAME_FIELD))
        rename_field.clear()
        rename_field.send_keys(new_name_repository)
        rename_button = WebDriverWait(self.browser, 7).until(ec.element_to_be_clickable(RepositorySettingPageLocators.RENAME_BUTTON))
        rename_button.click()

    def should_be_message_repository_is_empty(self):
        empty_repository_message = WebDriverWait(self.browser, 5).until(
            ec.visibility_of_element_located(RepositorySettingPageLocators.MESSAGE_REPOSITORY_EMPTY))
        message_text = empty_repository_message.text

        assert "doesn’t have any public repositories yet" in message_text, "Repository was been not deleted"

    def should_be_rename_repository(self, new_name_repository):
        assert new_name_repository in self.browser.current_url, "Repository did not rename"



