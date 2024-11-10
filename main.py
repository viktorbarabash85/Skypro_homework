import os.path

from src.decorators import log
from src.external_api import api_convert_currency
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file
from src.widget import get_date, mask_account_card

# homwork_11_1
# Словарь для проверки функций filter_by_currency и transaction_descriptions
transactions = [
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

print("_" * 13)  # для разделения
print("Маскирует номер банковской карты")
print(get_mask_card_number(7000792289606361))
print("_" * 13)  # для разделения

print("Маскирует номер банковского счета")
print(get_mask_account(73654108430135874305))
print("_" * 13)  # для разделения

print("Маскирует информацию о карте или счете с применением функций из masks.py")
print(mask_account_card("Visa Platinum 7000792289606361"))
print("_" * 13)  # для разделения

print("Конвертирует строку с датой в формат 'ДД.ММ.ГГГГ'")
print(get_date("2024-03-11T02:26:18.671407"))
print("_" * 13)  # для разделения

print("Функция фильтрует список словарей по значению ключа state.")
print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED",
    )
)
print("_" * 13)  # для разделения

print("Функция сортирует список словарей по дате.")
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
print("_" * 13)  # для разделения

print("Функция принимает на список словарей, представляющих транзакции")
print("Возвращает итератор, который поочередно выдает транзакции,")
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
print("_" * 13)  # для разделения

print("Генератор принимает список словарей с транзакциями")
print("Возвращает описание каждой операции по очереди.")
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
print("_" * 13)  # для разделения

print("Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.")
print("Принимает начальное и конечное значения для генерации диапазона номеров.")
for card_number in card_number_generator(1, 5):
    print(card_number)
print("_" * 13)  # для разделения


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
print("_" * 13)  # для разделения

# homwork_12_1
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data", "operations.json")
transactions_json = read_json_file(file_path)

for transaction in transactions_json:
    rub_amount = api_convert_currency(transaction)
    print(f"Transaction amount in RUB: {rub_amount}")

print("_" * 13)  # для разделения
