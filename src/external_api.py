import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> float:
    """
    Принимает транзакцию, возвращает сумму в рублях (float).
    Если валюта USD или EUR, конвертирует через API.
    """
    #  Достаем данные. Если ключей нет, берем 0 и 'RUB'
    amount_data = transaction.get("operationAmount", {})
    amount = float(amount_data.get("amount", 0))
    currency = amount_data.get("currency", {}).get("code", "RUB")

    # Если уже в рублях — возвращаем сразу
    if currency == "RUB":
        return amount

    # Конвертация для USD и EUR
    if currency in ["USD", "EUR"]:
        url = "https://api.apilayer.com"
        params = {"to": "RUB", "from": currency, "amount": amount}
        headers = {"apikey": API_KEY}

        try:
            # timeout=10 не даст программе зависнуть, если сервер API упадет
            response = requests.get(url, headers=headers, params=params, timeout=10)

            # Проверяем успешность запроса
            if response.status_code == 200:
                data = response.json()
                return float(data.get("result", 0))
            else:
                # Если сервер ответил ошибкой (например, 521), выводим инфо и возвращаем 0
                print(f"Ошибка API {response.status_code}: {response.text[:50]}")
                return 0.0

        except (requests.RequestException, Exception) as e:
            # Если нет интернета или другая критическая ошибка
            print(f"Ошибка при обращении к API: {e}")
            return 0.0

    # Если валюта не RUB/USD/EUR, возвращаем исходную сумму (или можно тоже 0.0)
    return amount
