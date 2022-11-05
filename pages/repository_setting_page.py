import allure
from .base_page import BasePage
from .locators import RepositorySettingPageLocators


class RepositorySettingPage(BasePage):

    locators = RepositorySettingPageLocators

    @allure.step('Delete repository')
    def delete_repository(self):
        delete_repository_button = self.browser_helper.element_is_clickable(self.locators.DELETE_REPOSITORY_BUTTON)
        delete_repository_button.click()

        confirmation_string = self.browser_helper.element_is_visible(self.locators.CONFIRMATION_STRING_TO_DELETE_REPOSITORY)

        confirmation_field = self.browser_helper.element_is_visible(self.locators.CONFIRMATION_FIELD_TO_DELETE_REPOSITORY)
        # confirmation_field.send_keys(confirmation_string.text)
        self.browser_helper.send_keys_in_element(confirmation_field, confirmation_string.text)

        button_confirm = self.browser_helper.element_is_clickable(self.locators.CONFIRMATION_BUTTON_TO_DELETE_REPOSITORY)
        button_confirm.click()

    @allure.step('Rename repository')
    def rename_repository(self, new_name_repository):
        rename_field = self.browser_helper.element_is_visible(self.locators.RENAME_FIELD)
        rename_field.clear()
        self.browser_helper.send_keys_in_element(rename_field, new_name_repository)

        rename_button = self.browser_helper.element_is_clickable(self.locators.RENAME_BUTTON)
        rename_button.click()

    @allure.step('Verification message about empty repository')
    def should_be_message_repository_is_empty(self):
        empty_repository_message = self.browser_helper.element_is_visible(self.locators.MESSAGE_REPOSITORY_EMPTY)
        message_text = empty_repository_message.text

        assert "doesn’t have any public repositories yet" in message_text, "Repository was been not deleted"

    @allure.step('Verification new name repository')
    def should_be_rename_repository(self, new_name_repository):
        assert new_name_repository in self.browser.current_url, "Repository did not rename"
