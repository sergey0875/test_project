from typing import Any
from typing import Dict
from typing import Iterator


def filter_by_currency(transactions: list[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Принимает список транзакций и код валюты.
    Возвращает итератор транзакций, соответствующих заданной валюте.
    """
    for transaction in transactions:
        # Проверяем вложенную структуру: operationAmount -> currency -> code
        if (
            transaction.get("operationAmount")
            and transaction["operationAmount"].get("currency")
            and transaction["operationAmount"]["currency"].get("code") == currency
        ):
            yield transaction


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """
    Принимает список транзакций и возвращает итератор с описаниями операций.
    """
    for transaction in transactions:
        # Извлекаем описание, если ключа нет — вернет None или пустую строку
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
    """
    for number in range(start, stop + 1):
        # Превращаем число в строку из 16 цифр, дополняя нулями слева
        card_str = f"{number:016}"

        # Формируем блоки по 4 цифры через пробел
        formatted_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"

        yield formatted_card
