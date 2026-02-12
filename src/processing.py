def filter_by_state(data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует список словарей по ключу"""

    filtered_list = []  # создаем пустой список.

    for item in data_list:
        if item.get("state") == state:  # Проверяем значение.
            filtered_list.append(item)  # Добавляем в новый список, если значение соответствует.

    return filtered_list


def sort_by_date(data_list: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортирует список словарей по дате"""

    return sorted(data_list, key=lambda x: x["date"], reverse=reverse)
