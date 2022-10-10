from .pages.main_page import MainPage
import time


def test_go_to_link(browser):
    link = "https://github.com"
    main_page = MainPage(browser, link)
    main_page.open()
    time.sleep(6)
    main_page.should_be_login_link()
    main_page.go_to_login_page()
    time.sleep(5)
