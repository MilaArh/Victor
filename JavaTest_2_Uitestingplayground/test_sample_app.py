import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

def test_sample_app(driver, random_user_name):
    driver.get("http://uitestingplayground.com/sampleapp")

    driver.find_element(By.CSS_SELECTOR, '[name="UserName"]').send_keys(random_user_name)
    driver.find_element(By.CSS_SELECTOR, '[name="Password"]').send_keys('pwd')
    driver.find_element(By.ID, 'login').click()

    assert driver.find_element(By.CLASS_NAME, 'text-success').text.startswith('Welcome')


def test_dynamic_table(driver):
    driver.get("http://uitestingplayground.com/dynamictable")
    cpu = driver.find_element(By.XPATH, '//*[text() = "Chrome"]/..').text
    res = [x for x in cpu.split(' ') if '%' in x][0]
    assert driver.find_element(By.CLASS_NAME, 'bg-warning').text.endswith(res)

def test_dynamic_table_2(driver):
    driver.get("http://uitestingplayground.com/dynamictable")

    a = driver.find_element(By.XPATH, "//*[text()='Chrome']/../*[contains(text(),'%')]")
    # print(add_to_cart.text)
    b = driver.find_element(By.CLASS_NAME, "bg-warning")
    # print(d.text.endswith(add_to_cart.text))
    # assert b.text.endswith(a.text), 'данные не совпадают'
    assert a.text in b.text, 'данные не совпадают'


@pytest.mark.xfail
def test_shadow_dom(driver):
    driver.get("http://uitestingplayground.com/shadowdom")

    shadow_host = driver.find_element(By.TAG_NAME, 'guid-generator')
    shadow_root = shadow_host.shadow_root

    shadow_content = shadow_root.find_element(By.ID, 'buttonGenerate')
    shadow_content.click()

    shadow_content = shadow_root.find_element(By.ID, 'buttonCopy')
    shadow_content.click()

    a = shadow_root.find_element(By.ID, 'editField').get_attribute('value')

    input_field = shadow_root.find_element(By.ID, 'editField')
    input_field.clear()
    input_field.send_keys(Keys.CONTROL + 'v')
    b = shadow_root.find_element(By.ID, 'editField').get_attribute('value')

    assert a == b, 'Не копирует в буфер обмена'


def test_shadow_dom_2(driver):
    driver.get("http://uitestingplayground.com/shadowdom")

    shadow_host = driver.find_element(By.TAG_NAME, 'guid-generator')
    shadow_root = shadow_host.shadow_root

    shadow_content = shadow_root.find_element(By.ID, 'buttonGenerate')
    shadow_content.click()

    shadow_content = shadow_root.find_element(By.ID, 'buttonCopy')
    shadow_content.click()

    # Находим элемент поля ввода
    input_element = shadow_root.find_element(By.ID, 'editField')

    # Копируем текст из поля ввода
    copied_text = input_element.get_attribute("value")
    time.sleep(5)
    # Выделяем текст в поле ввода
    input_element.send_keys(Keys.CONTROL + 'a')
    time.sleep(5)
    # Копируем текст в буфер обмена
    input_element.send_keys(Keys.CONTROL + 'c')
    shadow_root.find_element(By.ID, 'editField').clear()
    time.sleep(5)
    # Вводим текст в поле ввода
    input_element.send_keys(Keys.CONTROL + 'v')
    copied_text_2 = input_element.get_attribute("value")
    time.sleep(5)

    # # Проверяем, скопирован ли текст из поля ввода
    # if copied_text_2 == copied_text:
    #     print("Текст успешно скопирован из поля ввода")
    # else:
    #     print("Текст не скопирован из поля ввода")

    assert copied_text_2 == copied_text, "Текст не скопирован из поля ввода"

def test_shadow_dom_3(driver):
    driver.get("http://uitestingplayground.com/shadowdom")

    shadow_host = driver.find_element(By.TAG_NAME, 'guid-generator')
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

    shadow_content = shadow_root.find_element(By.ID, 'buttonGenerate')
    shadow_content.click()

    shadow_content = shadow_root.find_element(By.ID, 'buttonCopy')
    shadow_content.click()

    # Находим элемент поля ввода
    input_element = shadow_root.find_element(By.ID, 'editField')

    # Копируем текст из поля ввода
    copied_text = input_element.get_attribute("value")
    time.sleep(2)

    # Выделяем текст в поле ввода
    input_element.send_keys(Keys.CONTROL + 'a')
    time.sleep(2)

    # Копируем текст в буфер обмена
    input_element.send_keys(Keys.CONTROL + 'x')
    time.sleep(2)

    # Вставляем скопированный текст в поле ввода
    input_element.send_keys(Keys.CONTROL + 'v')
    time.sleep(2)

    # Получаем текст после вставки
    copied_text_2 = input_element.get_attribute("value")

    # Проверяем, скопирован ли текст из поля ввода
    assert copied_text_2 == copied_text, "Текст не скопирован из поля ввода"


def test_shadow_dom_4(driver):
    driver.get("http://uitestingplayground.com/shadowdom")

    shadow_host = driver.find_element(By.TAG_NAME, 'guid-generator')
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

    shadow_content = shadow_root.find_element(By.ID, 'buttonGenerate')
    shadow_content.click()

    shadow_content = shadow_root.find_element(By.ID, 'buttonCopy')
    shadow_content.click()

    # Находим элемент поля ввода
    input_element = shadow_root.find_element(By.ID, 'editField')

    copied_text = input_element.get_attribute("value")
    time.sleep(2)

    # Чтения содержимого буфера обмена
    clipboard_content = pyperclip.paste()


    # Проверяем, скопирован ли текст из поля ввода
    assert copied_text == clipboard_content, "Текст не скопирован из поля ввода"


def test_scrollbars(driver):
    driver.get("http://uitestingplayground.com/scrollbars")

    button = driver.find_element(By.ID, 'hidingButton')
    action = ActionChains(driver)
    action.scroll_to_element(button).click().perform()

    assert button.is_displayed(), 'Кнопка не отображается'


def test_scrollbars_2(driver):
    """ниже java script"""
    driver.get("http://uitestingplayground.com/scrollbars")

    button = driver.find_element(By.ID, 'hidingButton')

    driver.execute_script('arguments[0].scrollIntoView(true);', button)

    assert button.is_displayed(), 'Кнопка не отображается'
