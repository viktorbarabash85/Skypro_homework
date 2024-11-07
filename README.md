># <p style="color:DarkSeaGreen"> Проект "homework_12_2" </p>
___
>## Содержание
- [Описание проекта](#p-stylecolorrosybrown-описание-проекта--p)
- [Требования к окружению](#p-stylecolorrosybrown-требования-к-окружению--p)
- [Установка проекта](#p-stylecolorrosybrown-установка-проекта--p)
- [Установка зависимостей из `requirements.txt`](#p-stylecolorrosybrown-установка-зависимостей-из-requirementstxt--p)
- [Запуск функций в файле `main.py` в корне проекта](#p-stylecolorrosybrown-запуск-функций-в-файле-mainpy-в-корне-проекта--p)
- [Тестирование](#p-stylecolorrosybrown-тестирование--p)
- [JSON-файл]
- [Логгирование](#p-stylecolorrosybrown-логгирование--p)



___
- [Пример работы функций в модуле `masks.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-maskspy--p)
  - [Функция `get_mask_card_number`](#функция-get_mask_card_number)
  - [Функция `get_mask_account`](#функция-get_mask_account)
- [Пример работы функций в модуле `widget.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-widgetpy--p)
  - [Функция `mask_account_card`](#функция-mask_account_card)
  - [Функция `get_date`](#функция-get_date)
- [Пример работы функций в модуле `processing.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-processingpy--p)
  - [Функция `filter_by_state`](#функция-filter_by_state)
  - [Функция `sort_by_date`](#функция-sort_by_date)
- [Пример работы функций в модуле `generators.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-generatorspy--p)
  - [Функция `filter_by_currency`](#функция-filter_by_currency)
  - [Функция `transaction_descriptions`](#функция-transaction_descriptions)
  - [Функция `card_number_generator`](#функция-card_number_generator)
- [Пример работы функций в модуле `decorators.py`:](#p-stylecolorsteelblue-пример-работы-функций-в-модуле-decoratorspy--p)
  - [Функция декоратор `log`](#функция-декоратор-log)
- [JSON-файл. Пример работы функций в модулях `utils` и `external_api`:](#p-stylecolorsteelblue-json-файл-пример-работы-функций-в-модулях-utils-и-external_api--p)
  - [Функция  `read_json_file`](#функция-read_json_file)
  - [Функция  `api_convert_currency`](#функция-api_convert_currency)
>___




## <p style="color:RosyBrown"> Описание проекта [⮭](#содержание) </p>

Проект "homework_12_2" является продолжением работы над виджетом банковских операций клиента, 
функционал которого уже частично реализован в предыдущих проектах: 
`homework_9_1`, `homework_9_2`, `homework_10_1`, `homework_10_2`, `homework_11_1`, `homework_11_2` и `homework_12_1`. 
В качестве входных данных для многих функций теперь можно использовать данные, полученные из JSON-файла.

В модуле `processing.py` функция [filter_by_state](#функция-filter_by_state), которая принимает список словарей 
и опционально значение для ключа 
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению.

В том же модуле функция [sort_by_date](#функция-sort_by_date), которая принимает список словарей и необязательный 
параметр, задающий порядок 
сортировки (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате (date).


___

## <p style="color:RosyBrown"> Требования к окружению [⮭](#содержание)  </p>

- Версия Python: 
```
Python 3.8+
```
- Версия Pycharm:
```
pycharm-community-2024.2.2
 ```

___

## <p style="color:RosyBrown"> Установка проекта [⮭](#содержание)  </p>

1. Клонируйте репозиторий:
```bash
git clone git@github.com:viktorbarabash85/homework_10_1.git
```
2. Перейти в директорию проекта:
```bash
 cd homework_11_2
```
3. (Если требуется) Активируйте виртуальное окружение:
```bash
source .venv/bin/activate  # или .venv\Scripts\activate для Windows
```

___

## <p style="color:RosyBrown"> Установка зависимостей из `requirements.txt` [⮭](#содержание)  </p>
```bash
pip install -r requirements.txt
```

___

## <p style="color:RosyBrown"> Запуск функций в файле `main.py` в корне проекта [⮭](#содержание)  </p>
В командной строке выполните команду:
```bash
main.py
```
___

## <p style="color:RosyBrown"> Тестирование [⮭](#содержание)  </p>

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

## <p style="color:RosyBrown"> JSON-файл [⮭](#содержание)  </p>
<details><summary>  Описание обработки JSON-файла:
 </summary>

1. Файл с банковскими операциями размещен в директории `data` в корне проекта.
2. Создан модуль `utils` в пакете `src`.
3. Реализована функция чтения JSON-файла в модуле `utils`.
4. Функция чтения JSON-файла принимает путь к файлу JSON в качестве аргумента.
5. Функция чтения JSON-файла возвращает список словарей с данными о финансовых транзакциях.
6. Если JSON-файл пустой, содержит не-список или не найден, возвращается пустой список.
</details>















___

## <p style="color:RosyBrown"> Логгирование [⮭](#содержание)  </p>
<details><summary>  Описание логгирования:
 </summary>

1. Созданы логеры для перечисленных модулей: 
- `masks`
- `utils`
2. Реализована запись логов в файл. Логи записываться в папку `logs` в корне проекта. 
Файлы логов имеют расширение `.log`.
3. Формат записи лога в файл включает:
- `метку времени`, 
- `название модуля`, 
- `уровень серьезности`
- `сообщение, описывающее событие или ошибку, которые произошли`.
4. Лог перезаписываться при каждом запуске приложения.
</details>



___
> ___
___


## <p style="color:SteelBlue"> Пример работы функций в модуле `masks.py`: [⮭](#содержание)  </p>

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

## <p style="color:SteelBlue"> Пример работы функций в модуле `widget.py`: [⮭](#содержание)  </p>

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

## <p style="color:SteelBlue"> Пример работы функций в модуле `processing.py`: [⮭](#содержание)  </p>

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

## <p style="color:SteelBlue"> Пример работы функций в модуле `generators.py`: [⮭](#содержание)  </p>

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

___

## <p style="color:SteelBlue"> Пример работы функций в модуле `decorators.py`: [⮭](#содержание)  </p>

___

### Функция декоратор `log`
<details><summary> Описание декоратора: </summary>

Декоратор `log` автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
Декоратор принимает необязательный аргумент `filename`, который определяет, куда будут записываться логи 
(в файл или в консоль):

- Если `filename` задан, логи записываются в указанный файл.
- Если `filename` не задан, логи выводятся в консоль.

Логирование включает:
- Имя функции и результат выполнения при успешной операции.
- Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
</details>

<details><summary> Пример использования декоратора: </summary>

```bash
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
```
Ожидаемый вывод в лог-файл `mylog.txt` при успешном выполнении:
```bash
my_function ok
```
Ожидаемый вывод при ошибке:
```bash
my_function error: тип ошибки. Inputs: (1, 2), {}
```
Где `тип ошибки` заменяется на текст ошибки.

</details>


## <p style="color:SteelBlue"> JSON-файл. Пример работы функций в модулях `utils` и `external_api`: [⮭](#содержание)  </p>

___

### Функция  `read_json_file`
<details><summary> Описание функции: </summary>

- Функцию размещена в модуле `utils`.
- Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. 
- Если файл пустой, содержит не список или не найден, функция возвращает пустой список. 
- Файл с данными о финансовых транзациях помещается в `operations.json` в директорию `data/` в корне проекта.

 Ссылка на файл: [operations.json](https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view).
</details>

### Функция  `api_convert_currency`
<details><summary> Описание функции: </summary>

- Функция-конвертация размещена в модуле `external_api`.
- Функция принимает на вход транзакцию и возвращает сумму транзакции (`amount`) в `рублях`, тип данных — 
`float`. 
- Если транзакция была в `USD` или `EUR`, происходит обращение к внешнему API для получения текущего курса 
валют и конвертации суммы операции в рубли. 
- Для конвертации валюты применяется `Exchange Rates Data API`:
https://apilayer.com/exchangerates_data-api.
</details>