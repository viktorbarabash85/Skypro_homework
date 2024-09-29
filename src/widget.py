from typing import Union

# import datetime


def mask_account_card(card_info: Union[str]) -> Union[str]:
    """
    Маскирует информацию о карте или счете с применением функций из masks.py
    """
    from src.masks import get_mask_account, get_mask_card_number

    # Маскируем номер карты с добавлением типа карты
    # Маскируем номер счета с добавлением слова "Счет"
    card_types = ["Visa Classic", "Visa Gold", "Visa Platinum", "Maestro", "MasterCard"]
    for card_type in card_types:
        if card_type in card_info:
            card_number = card_info.split()[-1]
            return f"{card_type} {get_mask_card_number(int(card_number))}"
    if "Счет" in card_info:
        account_number = card_info.split()[-1]
        return f"{card_info.split()[0]} {get_mask_account(int(account_number))}"
    else:
        raise ValueError("Неизвестный тип карты")


def get_date(date_str: Union[str]) -> Union[str]:
    """
    Конвертирует строку с датой в формат "ДД.ММ.ГГГГ"
    Вход: "2024-03-11T02:26:18.671407"
    Выход: "11.03.2024"
    """
    # Разбиваем строку на части по символу 'T'
    date_part, time_part = date_str.split("T")
    # Разбиваем дату на части по символу '-'
    year, month, day = date_part.split("-")
    # Формируем строку в формате "дд.мм.гггг"
    result = f"{day}.{month}.{year}"

    return result


# """ Реализация функции для конвертирования строки с датой
#     в формат "ДД.ММ.ГГГГ" с помощью встроенного модуля datetime """
# def get_date(date_str: Union[str]) -> Union[str]:
# """
# Конвертирует строку с датой в формат "ДД.ММ.ГГГГ".
# Вход: "2024-03-11T02:26:18.671407"
# Выход: "11.03.2024"
# """
# dt = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
# return dt.strftime("%d.%m.%Y")
