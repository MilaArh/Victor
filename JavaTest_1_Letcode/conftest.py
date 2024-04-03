import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
import time


@pytest.fixture()
def my_options():
    opt = Options()
    # opt.add_argument('--headless') #скрыть окна браузера
    opt.add_argument('--window-size=1920,1080')
    return opt

@pytest.fixture()
def browser(my_options) -> WebDriver:
    browser = webdriver.Chrome(options=my_options)

    yield browser

    time.sleep(2)
    browser.quit()

