# Тест фильтра по валюте.
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions: list[dict]) -> None:
    transaction_filter_by_currency = filter_by_currency(transactions, "USD")
    assert next(transaction_filter_by_currency) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(transaction_filter_by_currency) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    assert next(transaction_filter_by_currency) == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }


def test_transaction_descriptions(transactions: list[dict]) -> None:
    transaction_filter_by_currency = transaction_descriptions(transactions)
    assert next(transaction_filter_by_currency) == "Перевод организации"
    assert next(transaction_filter_by_currency) == "Перевод со счета на счет"
    assert next(transaction_filter_by_currency) == "Перевод со счета на счет"
    assert next(transaction_filter_by_currency) == "Перевод с карты на карту"
    assert next(transaction_filter_by_currency) == "Перевод организации"


def test_card_number_generator() -> None:
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
