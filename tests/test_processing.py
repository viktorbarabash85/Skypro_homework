import pytest
from src.processing import filter_by_state

""" Тестирование правильности фильтрации списка словарей по заданному статусу state: CANCELED """
def test_filter_by_state_correct(filter_by_state_correct):
    # Применение фикстур. Тестирование корректности фильтрации списка словарей по заданному статусу state: CANCELED
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED"
    ) == filter_by_state_correct

""" Тестирование корректности функции при отсутствии словарей с заданным статусом state """
def test_filter_by_state_incorrect(filter_by_state_incorrect):
    # Применение фикстур. Тестирование корректности функции при отсутствии словарей с заданным статусом state
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED"
    ) == filter_by_state_incorrect

""" Тестирование правильности фильтрации списка словарей при отсутствии статуса state (по умолчанию 'EXECUTED') """
def test_filter_without_state_correct(filter_without_state_correct):
    # Применение фикстур. Тестирование корректности фильтрации списка словарей без заданного статуса state
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == filter_without_state_correct

@pytest.mark.parametrize('transactions, state, expected', [
    (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED",
        [
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    ),
    (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "INVALID_STATE",
        "Информация отсутствует или некорректно введен запрашиваемый статус"
    ),
])
def test_filter_by_state(transactions, state, expected):
    assert filter_by_state(transactions, state) == expected