import allure
from selenium.webdriver.support import expected_conditions as ec
from .base_page import BasePage
from .locators import RepositorySettingPageLocators


class RepositorySettingPage(BasePage):

    @allure.step('Delete repository')
    def delete_repository(self):
        delete_repository_button = self.wait.until(
            ec.element_to_be_clickable(RepositorySettingPageLocators.DELETE_REPOSITORY_BUTTON)
        )
        delete_repository_button.click()

        confirmation_string = self.wait.until(
            ec.visibility_of_element_located(RepositorySettingPageLocators.CONFIRMATION_STRING_TO_DELETE_REPOSITORY)
        )

        confirmation_field = self.wait.until(
            ec.visibility_of_element_located(RepositorySettingPageLocators.CONFIRMATION_FIELD_TO_DELETE_REPOSITORY)
        )
        confirmation_field.send_keys(confirmation_string.text)

        button_confirm = self.wait.until(
            ec.element_to_be_clickable(RepositorySettingPageLocators.CONFIRMATION_BUTTON_TO_DELETE_REPOSITORY)
        )
        button_confirm.click()

    @allure.step('Rename repository')
    def rename_repository(self, new_name_repository):
        rename_field = self.wait.until(
            ec.visibility_of_element_located(RepositorySettingPageLocators.RENAME_FIELD))
        rename_field.clear()
        rename_field.send_keys(new_name_repository)
        rename_button = self.wait.until(
            ec.element_to_be_clickable(RepositorySettingPageLocators.RENAME_BUTTON))
        rename_button.click()

    @allure.step('Verification message about empty repository')
    def should_be_message_repository_is_empty(self):
        empty_repository_message = self.wait.until(
            ec.visibility_of_element_located(RepositorySettingPageLocators.MESSAGE_REPOSITORY_EMPTY))
        message_text = empty_repository_message.text

        assert "doesn’t have any public repositories yet" in message_text, "Repository was been not deleted"

    @allure.step('Verification new name repository')
    def should_be_rename_repository(self, new_name_repository):
        assert new_name_repository in self.browser.current_url, "Repository did not rename"
