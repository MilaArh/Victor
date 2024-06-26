from selenium.common import NoSuchElementException
from Lesson2.Homework2.data import *
from Lesson2.Homework2.locators import *
from .conftest import is_not_element_present, is_element_present
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support import expected_conditions as EC




# Перенесли логин в conftest
# Авторизация
def test_correct_login(browser):
    browser.get(MAIN_PAGE)
    browser.find_element(*USER_NAME).send_keys(LOGIN)
    browser.find_element(*PASSWORD).send_keys(PASSWORD_LOG)
    browser.find_element(*SUBMIT).click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'не выполнен переход на страницу магазина'


def test_wrong_login(browser):
    browser.get(MAIN_PAGE)
    browser.find_element(*USER_NAME).send_keys(LOGIN_INVALID)
    browser.find_element(*PASSWORD).send_keys(PASSWORD_INVALID)
    browser.find_element(*SUBMIT).click()
    assert browser.current_url == 'https://www.saucedemo.com/', 'пользователь не остался на странице регистрации'


@pytest.mark.xfail  # игнорируем, предположим что user/user верные, программистами допущена ошибка,мы знаем что тест пока падает, ждем исправлений и  ставим спец пометку
def test_wrong_login_no_enter_xfail(browser):
    browser.get(MAIN_PAGE)
    browser.find_element(*USER_NAME).send_keys(LOGIN_INVALID)
    browser.find_element(*PASSWORD).send_keys(PASSWORD_INVALID)
    browser.find_element(*SUBMIT).click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'не выполнен переход на страницу магазина'


def test_login_error(browser):
    browser.get(MAIN_PAGE)
    browser.find_element(*USER_NAME).send_keys(LOGIN_INVALID)
    browser.find_element(*PASSWORD).send_keys(PASSWORD_INVALID)
    browser.find_element(*SUBMIT).click()

    error_v = browser.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error_v.text.startswith('Epic sadface'), 'Текст сообщения об ошибке не начинается с Epic sadface'


# Корзина
def test_add_to_cart_from_catalog(browser, login):
    """ Добавление товара в корзину через каталог """

    add_to_cart = browser.find_element(*ADD_TO_CART)
    add_to_cart.click()
    browser.get(MAIN_PAGE_CART)
    assert is_element_present(browser, By.CLASS_NAME, 'inventory_item_name'), 'товар не добавлен в корзину'
    # element_in_cart = browser.find_element(By.CLASS_NAME, 'inventory_item_name')
    # assert element_in_cart.text.startswith('Sauce Labs Backpack'), 'товар не добавлен в корзину'


def test_delete_from_cart(browser, login):
    """Удаление товара из корзины через корзину """

    add_to_cart = browser.find_element(*ADD_TO_CART)
    add_to_cart.click()

    browser.get(MAIN_PAGE_CART)
    browser.find_element(By.ID, 'remove-sauce-labs-backpack').click()

    elements_in_cart = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert len(elements_in_cart) == 0, 'товар остается в корзине'


def test_add_to_cart_from_cart_assert_text(browser, login):
    """ Добавление товара в корзину из карточки товара """
    # login(browser)

    browser.get("https://www.saucedemo.com/inventory-item.html?id=4")

    add_to_cart = browser.find_element(*ADD_TO_CART_ITEM)
    add_to_cart.click()

    browser.get(MAIN_PAGE_CART)

    element_in_cart = browser.find_element(By.CLASS_NAME, 'inventory_item_name')
    assert element_in_cart.text.startswith('Sauce Labs Backpack'), 'товар не добавлен в корзину'


def test_delete_from_cart_assert_len(browser, login):
    """Удаление товара из корзины через корзину """
    # login(browser)

    browser.get("https://www.saucedemo.com/inventory-item.html?id=4")
    browser.find_element(*ADD_TO_CART_ITEM).click()
    browser.find_element(*REMOVE_ITEM).click()

    browser.get(MAIN_PAGE_CART)

    elements_in_cart = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert len(elements_in_cart) == 0, 'товар остается в корзине'


# Карточка товара
def test_go_to_cart_click_img(browser, login):
    """ Успешный переход к карточке товара после клика на картинку товара """

    # login(browser)
    browser.find_element(*IMG_CART).click()

    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', 'не выполнен переход на карточку товара'


def test_go_to_cart_click_name(browser, login):
    """Успешный переход к карточке товара после клика на название товара """

    # login(browser)

    browser.find_element(*NAME_CART).click()

    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', 'не выполнен переход на карточку товара'


# Оформление заказа
def test_placing_an_order(browser, login):
    """Оформление заказа используя корректные данные"""

    # login(browser)
    browser.find_element(*ADD_TO_CART).click()
    browser.find_element(*BASKET).click()
    browser.find_element(*CHECKOUT).click()
    browser.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys('Мила')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').send_keys('Арх')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Zip/Postal Code"]').send_keys('411113')
    browser.find_element(*CONTINUE).click()
    browser.find_element(*FINISH).click()

    assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html', 'заказ не оформлен'


# Фильтр
def test_filter_a_to_z(browser, login):
    """Проверка работоспособности фильтра (A to Z)"""

    # login(browser)

    select = Select(browser.find_element(*SELECT))
    select.select_by_value('az')

    items = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    current_list = [item.text for item in items]
    sorted_list = sorted(current_list)
    assert current_list == sorted_list, 'Названия товаров не отсортированы по алфавиту A-Z'


def test_filter_z_to_a(browser, login):
    """Проверка работоспособности фильтра (Z to A)"""

    # login(browser)

    select = Select(browser.find_element(*SELECT))
    select.select_by_value('za')

    items = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    current_list = [item.text for item in items]
    sorted_list = list(reversed(sorted(current_list)))
    assert current_list == sorted_list, 'Названия товаров не отсортированы по алфавиту Z-A'


def test_filter_high_to_low(browser, login):
    """Проверка работоспособности фильтра (high to low)"""

    # login(browser)

    select = Select(browser.find_element(*SELECT))
    select.select_by_value('hilo')

    items = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    current_list = [float(item.text[1:]) for item in items]
    sorted_list = list(reversed(sorted(current_list)))
    assert current_list == sorted_list, 'Названия товаров не отсортированы по стоимости от high до low'


def test_filter_low_to_high(browser, login):
    """Проверка работоспособности фильтра (low to high)"""

    # login(browser)

    select = Select(browser.find_element(*SELECT))
    select.select_by_value('lohi')

    items = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    current_list = [float(item.text[1:]) for item in items]
    sorted_list = sorted(current_list)
    assert current_list == sorted_list, 'Названия товаров не отсортированы по стоимости от low до high'


# Бургер меню
def test_burger_menu_logout(browser, wait, login):
    """Выход из системы"""

    # login(browser)
    browser.find_element(*BURGER_MENU).click()

    wait.until(EC.element_to_be_clickable(LOGOUT)).click()

    assert browser.current_url == 'https://www.saucedemo.com/', 'выход из системы не осуществлен'


def test_burger_menu_about(browser, wait, login):
    """Проверка работоспособности кнопки "About" в меню"""

    # login(browser)
    browser.find_element(*BURGER_MENU).click()

    wait.until(EC.element_to_be_clickable(ABOUT)).click()

    assert browser.current_url == 'https://saucelabs.com/', 'кнопки "About" в меню работает не корректно'


def test_burger_menu_reset(browser, wait, login):
    """Проверка работоспособности кнопки "Reset App State"""

    # login(browser)
    browser.find_element(*ADD_TO_CART).click()
    browser.find_element(*BURGER_MENU).click()
    wait.until(EC.element_to_be_clickable(RESET_APP_STATE)).click()
    try:
        browser.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert False, "Товар не удален из корзины"
    except NoSuchElementException:
        assert True


def test_burger_menu_reset1(browser, wait, login):
    """Проверка работоспособности кнопки "Reset App State"""

    # login(browser)
    browser.find_element(*ADD_TO_CART).click()
    browser.find_element(*BURGER_MENU).click()
    wait.until(EC.element_to_be_clickable(RESET_APP_STATE)).click()

    assert is_not_element_present(browser, By.CLASS_NAME, "shopping_cart_badge"), 'Товар остался в корзине'



