import pytest
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

@pytest.fixture
def wait(browser):
    wait = WebDriverWait(browser, timeout=15)
    return wait


def is_not_element_present(browser, how, what, timeout=4) -> bool:# ожидаем появление, поэтом тайм-аут
    try:
        WebDriverWait(browser, timeout).until(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return True  # элемента нет
    return False  # элемент есть


def is_element_present(browser, how, what) -> bool:# этот элемент есть
    try:
        browser.find_element(how, what)
    except NoSuchElementException:
        return False
    return True