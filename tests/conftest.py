import pytest

"""
В test_masks.py для теста get_mask_card_number.
Фикстуры для тестирования правильности маскирования номера карты
"""
@pytest.fixture
def card_number_correct():
    return "1234 56** **** 3456"

@pytest.fixture
def card_number_incorrect():
    return "Некорректно введен номер карты"

"""
В test_masks.py для теста get_mask_account.
Фикстуры для тестирования правильности маскирования номера счета
"""
@pytest.fixture
def account_number_correct():
    return "**4305"

@pytest.fixture
def account_number_incorrect():
    return "Некорректно введен номер счета"

"""
В test_widget.py для теста mask_account_card.  
Фикстуры для тестирования правильности маскирования информации о типе карте или счете
"""
@pytest.fixture
def card_info_correct():
    return "Visa Platinum 7000 79** **** 6361"

@pytest.fixture
def card_info_incorrect():
    return "Неизвестный тип карты"

"""
В test_widget.py для теста get_date.
Фикстуры для тестирования правильности конвертации строки с датой
"""
@pytest.fixture
def date_str_correct():
    return "11.03.2024"

@pytest.fixture
def date_str_incorrect():
    return "Некорректная дата"

"""
В test_processinng.py для теста filter_by_state
Фикстуры для тестирования фильтрации списка словарей по заданному статусу state: CANCELED
"""
@pytest.fixture
def filter_by_state_correct():
    return(
        [
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    )

"""
В test_processinng.py для теста filter_by_state
Фикстуры для тестирования корректности функции при отсутствии словарей с заданным статусом state)
"""
@pytest.fixture
def filter_by_state_incorrect():
    return "Информация отсутствует или некорректно введен запрашиваемый статус"

"""
В test_processinng.py для теста filter_by_state
Фикстуры для тестирования фильтрации списка словарей без заданного статуса state (по умолчанию 'EXECUTED')
"""
@pytest.fixture
def filter_without_state_correct():
    return(
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]
    )
