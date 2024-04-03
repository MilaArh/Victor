from selenium.webdriver.common.by import By
from selenium import webdriver

def test_input_fields(browser):
    browser.get("https://letcode.in/edit")
    #Ввести имя в поле ввода

    browser.find_element(By.ID, "fullName").send_keys('Mila')
    # Вывести текст элемента
    print("\n текст элемента содержит:", browser.find_element(By.ID, "fullName").text)

    # Добавить текст в поле ввода с последующей табуляцией
    browser.find_element(By.ID, "join").send_keys('very \t')

    # Проверка значения атрибута
    assert browser.find_element(By.ID, "getMe").get_attribute("value") == "ortonikc", "поле input не содержит ожидаемое слово"

    # Отчистка поля ввода
    browser.find_element(By.ID, "clearMe").clear()
    # Проверка отчистки поля ввода
    assert browser.find_element(By.ID, "clearMe").get_attribute("value") == "", "поле input не пустое"

    # Атрибут disabled блокирует элемент HTML формы, то есть делает его неактивным
    # Проверка возможности редактирования поля вода
    assert browser.find_element(By.ID, "clearMe").get_attribute("disabled") is None, "поле не доступно для редактирования"
    # Проверка закрыта возможность редактирования поля вода 1 вариант
    assert browser.find_element(By.ID, "noEdit").get_attribute("disabled") is not None, "поле доступно для редактирования"
    # Проверка закрыта возможность редактирования поля вода 2 вариант
    assert browser.find_element(By.ID, "noEdit").get_attribute("disabled") == "true", "поле доступно для редактирования"
    element = browser.find_element(By.ID, "noEdit")

    if element.is_enabled():
        print("Элемент доступен для взаимодействия")
    else:
        print("Элемент неактивен или заблокирован")
    #  Атрибут readonly доступно только для чтения: его можно выделить и прочитать, но редактировать невозможно
    # Проверка поле ввода доступно только для чтения
    # assert browser.find_element(By.ID, "dontwrite").get_attribute("readonly") == "true", "поле доступно для редактирования"
    assert browser.find_element(By.ID, "dontwrite").is_enabled(), "поле доступно для редактирования"
