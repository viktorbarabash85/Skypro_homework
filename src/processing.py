from typing import Union


def filter_by_state(transactions: list, state: str = "EXECUTED") -> Union[list, str]:
    """
    Функция фильтрует список словарей по значению ключа state.
    Вход:
    transactions (list): Список словарей с данными о банковских операциях.
    state (str, optional): Значение для ключа state (по умолчанию 'EXECUTED').
    Выход:
    list: Новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
    """
    filtered_transactions = []
    for transaction in transactions:
        if transaction["state"] == state:
            filtered_transactions.append(transaction)
    if not filtered_transactions:
        return "Информация отсутствует или некорректно введен запрашиваемый статус"
    else:
        return filtered_transactions


def sort_by_date(transactions: list, reverse: bool = True) -> list:
    """
    Функция сортирует список словарей по дате.
    Вход:
    transactions (list): Список словарей с данными о банковских операциях.
    reverse (bool, optional): Параметр, задающий порядок сортировки (по умолчанию True).
    Выход:
    list: Новый список словарей, отсортированный по дате.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
