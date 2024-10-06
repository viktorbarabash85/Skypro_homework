from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Маскирует номер банковской карты"""
    card_number_str = str(card_number)
    #if card_number_str.isdigit() and card_number != 0 and len(card_number_str) == 16:
    if (card_number_str.isdigit()
            and int(card_number) != 0
            and len(card_number_str) == 16):
        return " ".join(
            [
            card_number_str[:4],
            #заменяем середину на **
            card_number_str[4:6] + "*" * 2,
            #заменяем середину на ****
            "*" * 4,
            card_number_str[-4:],
            ]
            )
    else:
        return "Некорректно введен номер карты"

def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Маскирует номер банковского счета"""
    account_number_str = str(account_number)
    if (account_number_str.isdigit()
            and int(account_number) != 0
            and len(account_number_str) == 20):
        return "*" * 2 + account_number_str[-4:]
    else:
        return "Некорректно введен номер счета"