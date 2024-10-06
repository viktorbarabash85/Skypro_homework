import pytest


""" Фикстуры для тестирования правильности маскирования номера карты """
@pytest.fixture
def card_number_correct():
    return "1234 56** **** 3456"


@pytest.fixture
def card_number_incorrect():
    return "Некорректно введен номер карты"
