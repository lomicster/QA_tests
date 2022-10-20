import time
import pytest
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/ru'


class TestMainPage():

    @pytest.mark.open_page
    def test1(self, browser):
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get(link)

    @pytest.mark.view_products
    def test2(self, browser):
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get(link)
        browser .find_element(By.XPATH, "//ul[@id='browse']//ul//a").click()
        time.sleep(5)


    @pytest.mark.xfail
    def test2(self, browser):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get(link)
        browser.find_element(By.XPATH, "//ul[@id='browse']//ul//a").click()
