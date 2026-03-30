import json


def get_transactions(path):
    """Открываем и читаем файл operations.json"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):  # Проверяем является ли списком
                return data
            else:
                return []

    except FileNotFoundError:
        return []  # Возвращаем пустой список при возникновении ошибки
    except json.JSONDecodeError:
        return []
