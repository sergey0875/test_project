from unittest.mock import ANY
from unittest.mock import patch

from src.external_api import get_transaction_amount


@patch("requests.get")
def test_get_transaction_amount_usd(mock_get):
    # Настраиваем фейковый ответ сервера
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500.0}

    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}

    result = get_transaction_amount(transaction)

    # 1. Проверяем результат
    assert result == 7500.0

    # 2. Проверяем, что запрос ушел на правильный URL с правильными параметрами
    # Используем ANY для заголовка, так как нам важно само наличие ключа
    mock_get.assert_called_once_with(
        "https://api.apilayer.com",
        headers={"apikey": ANY},
        params={"to": "RUB", "from": "USD", "amount": 100.0},
        timeout=10,
    )
