import pytest
from src.masks import get_mask_card_number


""" Тестирование правильности маскирования номера карты с применением фикстур и параметризации """
def test_get_mask_card_number_correct(card_number_correct):
    # Применение фикстур. Тестирование корректности номера карты и маскирования номера карты
    assert get_mask_card_number(1234567890123456) == card_number_correct

def test_get_mask_card_number_incorrect(card_number_incorrect):
    # Применение фикстур. Тестирование некорректности введенного номера карты
    assert get_mask_card_number(0000000000000000) == card_number_incorrect
    # with pytest.raises(AssertionError) as exc_info:
    #     get_mask_card_number(card_number_incorrect)

@pytest.mark.parametrize('value, expected', [
    ('1234567890123456', '1234 56** **** 3456'),
    (' ', 'Некорректно введен номер карты'),
    ('fahdhfjfkejdnfhn', 'Некорректно введен номер карты'),
    ('XXXXXXXXXXXXXXXX', 'Некорректно введен номер карты'),
    ('0000000000000000000000', 'Некорректно введен номер карты'),
    ('1234567XXXXXXXXX', 'Некорректно введен номер карты')
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected