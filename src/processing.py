def filter_by_state (transactions: list, state: str = 'EXECUTED') -> list:
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
        if transaction['state'] == state:
            filtered_transactions.append(transaction)
    return filtered_transactions
