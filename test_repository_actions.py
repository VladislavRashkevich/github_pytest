from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.main_authentication_user_page import MainAuthenticationUserPage
from .pages.new_repository_page import NewRepositoryPage
import pytest
import time


@pytest.mark.prob_test
class TestUserCanCreateRepository:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://github.com/login"
        login_page = LoginPage(browser, link)
        login_page.open()
        username = "VladislavTest"
        password = "SecondTestAcc123"
        login_page.authentication_user(username, password)
        time.sleep(15)
        self.link = browser.current_url

    def test_user_can_create_new_repository(self, browser):
        page = MainAuthenticationUserPage(browser, self.link)
        page.go_to_page_for_create_new_repository()
        create_new_repository_page = NewRepositoryPage(browser, browser.current_url)
        name_new_repository = "test_rep"
        create_new_repository_page.create_new_repository(name_new_repository)
        create_new_repository_page.new_repository_was_created(name_new_repository)



