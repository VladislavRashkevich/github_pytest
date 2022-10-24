import allure
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


@pytest.mark.first
@allure.severity(allure.severity_level.CRITICAL)
@allure.story('Регистрация пользователя со стартовой страницы')
def test_guest_can_authentication_from_start_page(browser):
    link = "https://github.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.authentication_user()
    login_page.should_be_authorized_user()
