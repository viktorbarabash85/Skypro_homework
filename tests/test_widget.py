import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_correct(card_info_correct: str) -> None:
    """
    Тестирование корректности маскирования информации о карте или счете
    """
    assert mask_account_card("Visa Platinum 7000792289606361") == card_info_correct


def test_mask_account_card_incorrect(card_info_incorrect: str) -> None:
    """
    Тестирование некорректности маскирования информации о карте или счете
    """
    assert mask_account_card("Unknown Card 7000792289606361") == card_info_incorrect


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Classic 4000000000000002", "Visa Classic 4000 00** **** 0002"),
        ("Maestro 5000000000000004", "Maestro 5000 00** **** 0004"),
        ("MasterCard 5100000000000004", "MasterCard 5100 00** **** 0004"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Unknown Card 7000792289606361", "Неизвестный тип карты"),
        ("", "Неизвестный тип карты"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


def test_get_date_correct(date_str_correct: str) -> None:
    """
    Применение фикстур. Тестирование корректности конвертации строки с датой.
    """
    assert get_date("2024-03-11T02:26:18.671407") == date_str_correct


def test_get_date_incorrect(date_str_incorrect: str) -> None:
    """
    Применение фикстур. Тестирование некорректности конвертации строки с датой
    """
    assert get_date("") == date_str_incorrect


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-02-20T12:00:00.000000", "20.02.2023"),
        ("", "Введен некорректный или нестандартный формат даты"),
        ("2024-03-11T02:26:18T671407", "Введен некорректный или нестандартный формат даты"),
        ("2024-03-11T02:26:18", "Введен некорректный или нестандартный формат даты"),
        ("2024-03-11T02:60:18.671407", "Введен некорректный или нестандартный формат даты")
    ],
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected
