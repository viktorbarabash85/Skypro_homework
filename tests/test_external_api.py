import os
import unittest
from unittest.mock import MagicMock, Mock, patch

import requests
from dotenv import load_dotenv

from src.external_api import api_convert_currency

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


class TestConvertToRub(unittest.TestCase):

    @patch("requests.get")
    def test_api_convert_currency_usd_to_rub(self, mock_get: MagicMock) -> None:
        """
        Тестирование корректности конвертации USD в RUB
        """
        mock_get.return_value.json.return_value = {"result": 75.0}
        mock_get.return_value.status_code = 200

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}

        result = api_convert_currency(transaction)
        self.assertEqual(result, 75.0)
        mock_get.assert_called_once_with(
            "https://apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1", headers={"apikey": API_KEY}
        )

    @patch("requests.get")
    def test_api_convert_currency_eur_to_rub(self, mock_get: MagicMock) -> None:
        """
        Тестирование корректности конвертации EUR в RUB
        """
        mock_get.return_value.json.return_value = {"result": 85.0}
        mock_get.return_value.status_code = 200

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "EUR"}}}

        result = api_convert_currency(transaction)
        self.assertEqual(result, 85.0)
        mock_get.assert_called_once_with(
            "https://apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1", headers={"apikey": API_KEY}
        )

    def test_api_convert_currency_rub_to_rub(self) -> None:
        """
        Тестирование корректности конвертации RUB в RUB
        """
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}

        result = api_convert_currency(transaction)
        self.assertEqual(result, 100)

    def test_api_convert_currency_other_to_rub(self) -> None:
        """
        Тестирование корректности конвертации  других валют в RUB
        """
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "GBP"}}}

        result = api_convert_currency(transaction)
        self.assertEqual(result, 0.0)

    @patch("requests.get")
    def test_api_convert_currency_failure(self, mock_get: MagicMock) -> None:
        """
        Тестирование конвертации ошибкой.
        """
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException(response=mock_response)
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}

        result = api_convert_currency(transaction)
        self.assertEqual(result, 0.0)

    @patch("requests.get")
    def test_api_convert_currency_invalid_currency(self, mock_get: MagicMock) -> None:
        """
        Тестирование конвертации с неверной валютой
        """
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "JPY"}}}

        result = api_convert_currency(transaction)
        self.assertEqual(result, 0.0)  # Ожидаем 0.0 для неподдерживаемой валюты

    @patch("requests.get")
    def test_api_convert_currency_request_exception(self, mock_get: MagicMock) -> None:
        """
        Тестирование обработки исключения при выполнении HTTP-запроса.
        Этот тест проверяет, что функция api_convert_currency корректно
        обрабатывает исключение, вызванное проблемами с сетью.
        """
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}

        result = api_convert_currency(transaction)
        self.assertEqual(result, 0.0)  # Ожидаем 0.0 при ошибке сети
