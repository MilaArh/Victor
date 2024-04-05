import time

import pytest
from faker import Faker
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture()
def my_options():
    opt = Options()
    # opt.add_argument('--headless')  # скрыть окна браузера
    opt.add_argument('--window-size=1920,1080')
    return opt


@pytest.fixture()
def driver(my_options) -> WebDriver:
    driver = webdriver.Chrome(options=my_options)

    yield driver

    time.sleep(2)
    driver.quit()


@pytest.fixture
def random_user_name():
    faker = Faker()
    return faker.user_name()
