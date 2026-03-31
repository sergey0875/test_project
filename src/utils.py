import json
import logging

# Логирование.
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(path):
    """Открываем и читаем файл operations.json"""
    try:
        logger.debug("Открываю файл")
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):  # Проверяем является ли списком
                logger.debug("Данные успешно прочитаны, это список")
                return data
            else:
                logger.warning("Файл прочитан, но данные не являются списком")
                return []

    except FileNotFoundError as f:
        logger.error(f"Произошла ошибка: {f}")
        return []  # Возвращаем пустой список при возникновении ошибки
    except json.JSONDecodeError as f:
        logger.error(f"Произошла ошибка: {f}")
        return []


print(get_transactions("test.json"))
