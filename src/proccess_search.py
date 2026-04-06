import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей"""
    result = []
    for operation in data:
        # Ищем значение во ВСЕХ строковых полях словаря
        # (на случай, если описание лежит в другом ключе)
        for value in operation.values():
            if value and re.search(search, str(value), re.I):
                result.append(operation)
                break
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Список словарей с данными о банковских операциях и список категорий операций"""
    counts = Counter()

    for item in data:
        description = item.get("description")
        for category in categories:
            if category.lower() in description.lower():
                counts[category] += 1

    return counts
