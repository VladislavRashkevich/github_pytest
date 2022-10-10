from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, 'login')]")
                            #// a[contains( @ href, 'login')]
