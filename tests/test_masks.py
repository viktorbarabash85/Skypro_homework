import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_correct(card_number_correct: str) -> None:
    """
    Тестирование корректности маскирования номера карты с применением фикстур и параметризации
    """
    assert get_mask_card_number(1234567890123456) == card_number_correct


def test_get_mask_card_number_incorrect(card_number_incorrect: str) -> None:
    """
    Тестирование некорректности маскирования номера карты с применением фикстур и параметризации
    """
    assert get_mask_card_number(0000000000000000) == card_number_incorrect
    # with pytest.raises(AssertionError) as exc_info:
    #     get_mask_card_number(card_number_incorrect)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        (" ", "Некорректно введен номер карты"),
        ("fahdhfjfkejdnfhn", "Некорректно введен номер карты"),
        ("XXXXXXXXXXXXXXXX", "Некорректно введен номер карты"),
        ("0000000000000000000000", "Некорректно введен номер карты"),
        ("1234567XXXXXXXXX", "Некорректно введен номер карты"),
    ],
)
def test_get_mask_card_number(value: str, expected: str) -> None:
    assert get_mask_card_number(value) == expected


def test_get_mask_account_correct(account_number_correct: str) -> None:
    """
    Тестирование корректности маскирования номера счета с применением фикстур и параметризации
    """
    assert get_mask_account(73654108430135874305) == account_number_correct


def test_get_mask_account_incorrect(account_number_incorrect: str) -> None:
    """
    Тестирование некорректности маскирования номера счета с применением фикстур и параметризации
    """
    assert get_mask_account(00000000000000000000) == account_number_incorrect


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305", "**4305"),
        (" ", "Некорректно введен номер счета"),
        ("fahdhfjfkejdnfhnhssa", "Некорректно введен номер счета"),
        ("XXXXXXXXXXXXXXXX", "Некорректно введен номер счета"),
        ("0000000000000000000000", "Некорректно введен номер счета"),
        ("1234567890XXXXXXXXXX", "Некорректно введен номер счета"),
    ],
)
def test_get_mask_account(value: str, expected: str) -> None:
    assert get_mask_account(value) == expected
