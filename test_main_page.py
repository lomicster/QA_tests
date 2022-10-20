import time
from pages.main_page import MainPage
import pytest


link = 'http://selenium1py.pythonanywhere.com/ru'


# class TestMainPage():
#     @pytest.mark.open_page
def test_guest_can_go_to_catalogue(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_catalogue()

    # @pytest.mark.view_products
    # def test2(browser):
    #     browser.get(link)
    #     time.sleep(5)

    # @pytest.mark.xfail
    # def test3(browser):
    #     browser.get(link)

