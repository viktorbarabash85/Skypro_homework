import pytest


@pytest.fixture
def card_number_correct() -> str:
    """
    В test_masks.py для теста get_mask_card_number.
    Фикстуры для тестирования корректности маскирования номера карты
    """
    return "1234 56** **** 3456"


@pytest.fixture
def card_number_incorrect() -> str:
    """
    В test_masks.py для теста get_mask_card_number.
    Фикстуры для тестирования некорректности маскирования номера карты
    """
    return "Некорректно введен номер карты"


@pytest.fixture
def account_number_correct() -> str:
    """
    В test_masks.py для теста get_mask_account.
    Фикстуры для тестирования корректности маскирования номера счета
    """
    return "**4305"


@pytest.fixture
def account_number_incorrect() -> str:
    """
    В test_masks.py для теста get_mask_account.
    Фикстуры для тестирования некорректности маскирования номера счета
    """
    return "Некорректно введен номер счета"


@pytest.fixture
def card_info_correct() -> str:
    """
    В test_widget.py для теста mask_account_card
    Фикстуры для тестирования корректности маскирования информации о типе карте или счете
    """
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def card_info_incorrect() -> str:
    """
    В test_widget.py для теста mask_account_card.
    Фикстуры для тестирования некорректности маскирования информации о типе карте или счете
    """
    return "Неизвестный тип карты"


@pytest.fixture
def date_str_correct() -> str:
    """
    В test_widget.py для теста get_date.
    Фикстуры для тестирования корректности конвертации строки с датой
    """
    return "11.03.2024"


@pytest.fixture
def date_str_incorrect() -> str:
    """
    В test_widget.py для теста get_date.
    Фикстуры для тестирования некорректности конвертации строки с датой
    """
    return "Введен некорректный или нестандартный формат даты"


@pytest.fixture
def filter_by_state_correct() -> list:
    """
    В test_processinng.py для теста filter_by_state
    Фикстуры для тестирования фильтрации списка словарей по заданному статусу state: CANCELED
    """
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def filter_by_state_incorrect() -> str:
    """
    В test_processinng.py для теста filter_by_state
    Фикстуры для тестирования корректности функции при отсутствии словарей с заданным статусом state).
    """
    return "Информация отсутствует или некорректно введен запрашиваемый статус"


@pytest.fixture
def filter_without_state_correct() -> list:
    """
    В test_processinng.py для теста filter_by_state
    Фикстуры для тестирования фильтрации списка словарей без заданного статуса state (по умолчанию 'EXECUTED')
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_true_correct() -> list:
    """
    В test_processinng.py для теста sort_by_date
    Фикстуры для тестирования сортировки списка словарей по датам в порядке убывания
    (по умолчанию — убывание: True)
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_false_correct() -> list:
    """
    В test_processinng.py для теста sort_by_date
    Фикстуры для тестирования сортировки списка словарей по датам в порядке возрастания
    (по умолчанию — убывание: True)
    """
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def sort_by_date_incorrect() -> str:
    """
    В test_processinng.py для теста sort_by_date
    Фикстуры для тестирования сортировки списка словарей при некорректно введенной дате
    """
    return "Введен некорректный или нестандартный формат даты"


@pytest.fixture
def transactions() -> list[dict]:
    """
    Фикстура transactions
    """
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
