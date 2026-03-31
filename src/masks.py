import logging
import os
from typing import Union

# Автоматический отступ к корню проекта, чтобы не падали тесты
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Авто-создание папки
os.makedirs(LOG_DIR, exist_ok=True)
# Полный путь к файлу
LOG_FILE = os.path.join(LOG_DIR, "masks.log")

# Логирование
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: Union[str, int]) -> str:
    """Функция маскирует номер карты"""
    try:
        logger.debug("Запускаю функцию маскировки")
        # Переводим в строку.
        number_card_str = str(number_card)
        # считаем количество введенных цифр и сравниваем с условием.
        if len(number_card_str) != 16:
            logger.warning("Ввод не корректен")
            return "Неполный ввод,такой карты нет."
        # Выводим результат при помощи срезов
        logger.debug("Корректный ввод")
        return f" {number_card_str[:4]} {number_card_str[4:6]}** **** {number_card_str[12:]}"
    except Exception as e:
        logger.error(f"Ошибка при маскировке: {e}")
        return "Ошибка данных"


def get_mask_account(number_account: Union[str, int]) -> str:
    """Функция маскерует номер счета, оставляя только последние 4 цифры"""
    try:

        logger.debug("Запускаю фцнкцию проверки счета")
        number_account_str = str(number_account)
        logger.debug("Проверяю на длину ввода")
        if len(number_account_str) != 20:
            logger.warning("Ввод не корректен")
            return "Неправильный ввод."

        # Выводим результат.
        logger.debug("Корректный ввод")
        return f" **{number_account_str[-4:]}"
    except Exception as e:
        logger.error(f"Ошибка при маскировке: {e}")
        return "Ошибка данных"
