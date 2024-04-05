import pytest
from registration_system import RegistrationSystem

# Фикстура для инициализации системы перед каждым тестом
@pytest.fixture
def init_system():
    system = RegistrationSystem()
    yield system
    system.delete_all_users()  # постусловие: очистка базы данных после теста

    '''
    Тестовый кейс №: 001
    Название: Регистрация пользователя без предусловий и постусловий
    Описание: Проверка функционала регистрации нового пользователя.
    Шаги:
    1.1 Создать объект класса RegistrationSystem.
    1.2 Вызвать метод register с параметрами: "Алекс", "alex@example.com", "+1234567890".
    1.3 Вызвать метод view_all_users и проверить наличие пользователя с данным email в системе.
    Ожидаемый результат:
    Пользователь с email "alex@example.com" присутствует в системе.
    '''

def test_registration_without_pre_post_conditions():
    # Шаги тест кейса 001
    system = RegistrationSystem()
    system.register("Алекс", "alex@example.com", "+1234567890")
    users = system.view_all_users()
    assert "alex@example.com" in users  # Ожидаемый результат

    '''
    Тестовый кейс №: 002
    Название: Регистрация пользователя с предусловиями и постусловиями
    Описание: Проверка функционала регистрации нового пользователя с учетом начального состояния системы и восстановления исходного состояния после теста.
    Предусловие:
    Система инициализирована, база данных пуста.
    Шаги:
    2.1 Создать объект класса RegistrationSystem.
    2.2 Вызвать метод register с параметрами: "Алекс", "alex@example.com", "+1234567890".
    2.3 Вызвать метод view_all_users и проверить наличие пользователя с данным email в системе.
    Ожидаемый результат:
    Пользователь с email "alex@example.com" присутствует в системе.
    Постусловие:
    Удалить всех пользователей из системы, вызвав метод delete_all_users.
    '''
def test_registration_with_pre_post_conditions(init_system):
    # Шаги тест кейса 002
    init_system.register("Алекс", "alex@example.com", "+1234567890")
    users = init_system.view_all_users()
    assert "alex@example.com" in users  # Ожидаемый результат