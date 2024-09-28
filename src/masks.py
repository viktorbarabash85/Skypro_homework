from typing import Union


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Маскирует номер банковской карты"""
    card_number_str = str(card_number)

    return " ".join(
        [
            card_number_str[:4],
            # заменяем середину на **
            card_number_str[4:6] + "*" * 2,
            # заменяем середину на ****
            "*" * 4,
            card_number_str[-4:],
        ]
    )


def get_mask_account(account_number: Union[int]) -> Union[str]:
    """Маскирует номер банковского счета"""
    account_number_str = str(account_number)

    return "*" * 2 + account_number_str[-4:]
