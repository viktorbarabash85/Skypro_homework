# **Проект "homework_11_1"**

## Содержание
- [Описание](#описание)
- [Требования к окружению](#требования-к-окружению)
- [Установка проекта](#установка-проекта)
- [Установка зависимостей из `requirements.txt`](#установка-зависимостей-из-requirementstxt)
- [Запуск функций в файле `main.py` в корне проекта](#запуск-функций-в-файле-mainpy-в-корне-проекта)
- [Тестирование](#тестирование)
___
- [Пример работы функций в модуле `masks.py`:](#пример-работы-функций-в-модуле-maskspy)
  - [Функция `get_mask_card_number`](#функция-get_mask_card_number)
  - [Функция `get_mask_account`](#функция-get_mask_account)
- [Пример работы функций в модуле `widget.py`:](#пример-работы-функций-в-модуле-widgetpy)
  - [Функция `mask_account_card`](#функция-mask_account_card)
  - [Функция `get_date`](#функция-get_date)
- [Пример работы функций в модуле `processing.py`:](#пример-работы-функций-в-модуле-processingpy)
  - [Функция `filter_by_state`](#функция-filter_by_state)
  - [Функция `sort_by_date`](#функция-sort_by_date)
- [Пример работы функций в модуле `generators.py`:](#пример-работы-функций-в-модуле-generatorspy)
  - [Функция `filter_by_currency`](#функция-filter_by_currency)
  - [Функция `transaction_descriptions`](#функция-transaction_descriptions)
  - [Функция `card_number_generator`](#функция-card_number_generator)



___

## Описание

Проект "homework_11_1" является продолжением работы над виджетом банковских операций клиента, 
функционал которого уже частично реализован в предыдущих проектах: "9_1_homework", "9_2_homework", "homework_10_1" 
и "homework_10_2". 

В модуле `processing.py` функция [filter_by_state](#функция-filter_by_state), которая принимает список словарей 
и опционально значение для ключа 
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению.

В том же модуле функция [sort_by_date](#функция-sort_by_date), которая принимает список словарей и необязательный 
параметр, задающий порядок 
сортировки (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате (date).

___

## Требования к окружению

- Версия Python: 
```
Python 3.8+
```
- Версия Pycharm:
```
pycharm-community-2024.2.2
 ```

___

## Установка проекта

1. Клонируйте репозиторий:
```bash
git clone git@github.com:viktorbarabash85/homework_10_1.git
```
2. Перейти в директорию проекта:
```bash
 cd homework_10_1
```
3. (Если требуется) Активируйте виртуальное окружение:
```bash
source .venv/bin/activate  # или .venv\Scripts\activate для Windows
```

___

## Установка зависимостей из `requirements.txt`
```bash
pip install -r requirements.txt
```

___

## Запуск функций в файле `main.py` в корне проекта
В командной строке выполните команду:
```bash
main.py
```
___

## Тестирование

Тесты написаны ко всем функциям проекта в модулях: `test_masks.py`, `test_widjet.py`, `test_processing.py`,
`test_generators.py`. 
Все тесты расположены в папке `tests\`.

Для их запуска необходимо установить `pytest`, выполнив команду:
```bash
# Установка через Poetry
poetry add --group dev pytest
```
Запустите тестирование выполнив команду:
```bash
pytest
```
Проект покрыт тестами на `100%`.
В репозитории есть папка `html.cov` с отчетом покрытия тестами в формате `index.html`




___

## Пример работы функций в модуле `masks.py`:

___
### Функция `get_mask_card_number`
<details><summary> Пример работы функции: </summary>

```bash
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
```
</details>

___
### Функция `get_mask_account`
<details><summary> Пример работы функции: </summary>

```bash
73654108430135874305  # входной аргумент
**4305  # выход функции
```
</details>

___

## Пример работы функций в модуле `widget.py`:

___
### Функция `mask_account_card`
<details><summary> Пример работы функции: </summary>

```bash
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```
</details>

<details><summary> Примеры входных данных для проверки функции: </summary>

```bash
Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305
```
</details>

___
### Функция `get_date`
<details><summary> Пример работы функции: </summary>

```bash
# Пример для карты
"2024-03-11T02:26:18.671407"  # входной аргумент
"11.03.2024"  # выход функции в формате "ДД.ММ.ГГГГ"
```
</details>








___

## Пример работы функций в модуле `processing.py`:

___

### Функция `filter_by_state`
<details><summary> Пример работы функции: </summary>

```bash
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
</details>

<details><summary> Пример входных данных для проверки функции: </summary>

```bash
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
</details>


___

### Функция `sort_by_date`
<details><summary> Пример работы функции: </summary>

```bash
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
</details>

<details><summary> Пример входных данных для проверки функции </summary>

```bash
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
</details>

___

## Пример работы функций в модуле `generators.py`:

___

### Функция `filter_by_currency`
<details><summary> Пример использования функции: </summary>

```bash
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
</details>

___

### Функция `transaction_descriptions`
<details><summary> Пример использования функции: </summary>

```bash
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
</details>


___

<details><summary> Пример входных данных для проверки функций 
filter_by_currency и transaction_descriptions: </summary>

```bash
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
```
</details>

___

### Функция `card_number_generator`
<details><summary> Пример использования функции: </summary>

```bash
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```
</details>




