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
        # raise ValueError("Неизвестный тип карты")
        return "Неизвестный тип карты"


def get_date(date_str: Union[str]) -> Union[str]:
    """
    Конвертирует строку с датой в формат "ДД.ММ.ГГГГ"
    Вход: "2024-03-11T02:26:18.671407"
    Выход: "11.03.2024"
    """
    error_message = "Введен некорректный или нестандартный формат даты"

    if not date_str:
        return error_message

    parts = date_str.split("T")
    if len(parts) != 2:
        return error_message

    date_parts = parts[0].split("-")
    time_parts = parts[1].split(":")
    seconds_parts = time_parts[2].split(".")

    if len(date_parts) != 3 or len(time_parts) != 3 or len(seconds_parts) != 2:
        return error_message

    year, month, day = date_parts
    hours, minutes, seconds = time_parts[0], time_parts[1], seconds_parts[0]
    microseconds = seconds_parts[1]

    if (
        not (year.isdigit() and 1900 <= int(year) <= 2100)
        or not (month.isdigit() and 1 <= int(month) <= 12)
        or not (day.isdigit() and 1 <= int(day) <= 31)
        or not (hours.isdigit() and 0 <= int(hours) <= 23)
        or not (minutes.isdigit() and 0 <= int(minutes) <= 59)
        or not (seconds.isdigit() and 0 <= int(seconds) <= 59)
        or not (microseconds.isdigit() and 0 <= int(microseconds) <= 999999)
    ):
        return error_message

    result = f"{day}.{month}.{year}"
    return result


# """ Реализация функции для конвертирования строки с датой
#     в формат "ДД.ММ.ГГГГ" с помощью встроенного модуля datetime """
# def get_date(date_str: Union[str]) -> Union[str]:
#     """
#     Конвертирует строку с датой в формат "ДД.ММ.ГГГГ".
#     Вход: "2024-03-11T02:26:18.671407"
#     Выход: "11.03.2024"
#     """
#     dt = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
#     return dt.strftime("%d.%m.%Y")
