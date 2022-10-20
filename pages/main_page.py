from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_catalogue(self):
        self.browser.find_element(*MainPageLocators.CATALOGUE_LINK).click()
