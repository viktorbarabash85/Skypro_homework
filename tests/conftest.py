import pytest


""" Фикстуры для тестирования правильности маскирования номера карты """
@pytest.fixture
def card_number_correct():
    return "1234 56** **** 3456"

@pytest.fixture
def card_number_incorrect():
    return "Некорректно введен номер карты"

""" Фикстуры для тестирования правильности маскирования номера счета """
@pytest.fixture
def account_number_correct():
    return "**4305"

@pytest.fixture
def account_number_incorrect():
    return "Некорректно введен номер счета"


""" Фикстуры для тестирования правильности маскирования информации о типе карте или счете """
@pytest.fixture
def card_info_correct():
    return "Visa Platinum 7000 79** **** 6361"

@pytest.fixture
def card_info_incorrect():
    return "Неизвестный тип карты"

""" Фикстуры для тестирования правильности конвертации строки с датой """
@pytest.fixture
def date_str_correct():
    return "11.03.2024"

@pytest.fixture
def date_str_incorrect():
    return "Некорректная дата"
