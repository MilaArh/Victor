from selenium.webdriver.common.by import By


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
    # Проверка закрыта возможность редактирования поля вода 3 вариант
    assert browser.find_element(By.ID, "noEdit").is_enabled() is False, "поле доступно для редактирования"

    element = browser.find_element(By.ID, "noEdit")

    if element.is_enabled():
        print("Элемент доступен для взаимодействия")
    else:
        print("Элемент неактивен или заблокирован")

        # Метод is_enabled() в Selenium WebDriver используется для проверки,
        # доступен ли элемент для взаимодействия на веб-странице.
        # Этот метод возвращает булево значение: True, если элемент доступен для взаимодействия (активен),
        # и False, если элемент неактивен или заблокирован.
        # Метод is_enabled() в Selenium возвращает True для лементов с атрибутом readonly


    # Проверка
    def tell_me(name, e):
        print(f"{name} is_enabled: {e.is_enabled()}")
        print(f"{name} is_displayed: {e.is_displayed()}")
        print(f"{name} is_selected: {e.is_displayed()}")
        print(f"{name} disabled: {e.get_attribute("disabled")}")
        print(f"{name} readonly: {e.get_attribute("readonly")}\n")

    tell_me("noEdit", browser.find_element(By.ID, "noEdit"))
    tell_me("dontwrite", browser.find_element(By.ID, "dontwrite"))

    #  Атрибут readonly доступно только для чтения: его можно выделить и прочитать, но редактировать невозможно
    # Проверка поле ввода доступно только для чтения
    assert browser.find_element(By.ID, "dontwrite").get_attribute("readonly") == "true", "поле доступно для редактирования"
    assert browser.find_element(By.ID, "dontwrite").get_attribute("readonly") is not None, "поле доступно для редактирования"
    assert browser.find_element(By.ID, "dontwrite").is_displayed() is True, "содержание поля скрыто"

    element = browser.find_element(By.ID, "dontwrite")

    if element.is_displayed():
        print("Элемент с атрибутом readonly видим") #True
    else:
        print("Элемент с атрибутом readonly не видим") #False

