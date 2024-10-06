import pytest
from src.widget import mask_account_card, get_date

""" Тестирование правильности маскирования информации о карте или счете """
def test_mask_account_card_correct(card_info_correct):
    # Применение фикстур. Тестирование корректности маскирования информации о карте
    assert mask_account_card("Visa Platinum 7000792289606361") == card_info_correct

def test_mask_account_card_incorrect(card_info_incorrect):
    # Применение фикстур. Тестирование некорректности маскирования информации о карте
    assert mask_account_card("Unknown Card 7000792289606361") == card_info_incorrect

@pytest.mark.parametrize('value, expected', [
    ("Visa Classic 4000000000000002", "Visa Classic 4000 00** **** 0002"),
    ("Maestro 5000000000000004", "Maestro 5000 00** **** 0004"),
    ("MasterCard 5100000000000004", "MasterCard 5100 00** **** 0004"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Unknown Card 7000792289606361", "Неизвестный тип карты"),
    ("", "Неизвестный тип карты"),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


""" Тестирование правильности конвертации строки с датой """
def test_get_date_correct(date_str_correct):
    # Применение фикстур. Тестирование корректности конвертации строки с датой
    assert get_date("2024-03-11T02:26:18.671407") == date_str_correct


def test_get_date_incorrect(date_str_incorrect):
    # Применение фикстур. Тестирование некорректности конвертации строки с датой
    assert get_date("") == date_str_incorrect

@pytest.mark.parametrize('value, expected', [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-02-20T12:00:00.000000", "20.02.2023"),
    ("", "Некорректная дата"),
])
def test_get_date(value, expected):
    assert get_date(value) == expected
    with pytest.raises(ValueError) as exc_info:
        get_date(" ")