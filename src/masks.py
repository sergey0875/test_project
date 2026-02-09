from typing import Union


def get_mask_card_number(number_card: Union[str, int]) -> str:
    """Функция маскирует номер карты"""
    # Переводим в строку.
    number_card_str = str(number_card)
    # считаем количество введенных цифр и сравниваем с условием.
    if len(number_card_str) != 16:
        return "Неполный ввод,такой карты нет."
    # Выводим результат при помощи срезов
    return f" {number_card_str[:4]} {number_card_str[4:6]}** **** {number_card_str[12:]}"


def get_mask_account(number_account: Union[str, int]) -> str:
    """Функция маскерует номер счета, оставляя только последние 4 цифры"""

    number_account_str = str(number_account)
    if len(number_account_str) != 20:
        return "Неправильный ввод."

    # Выводим результат.
    return f" **{number_account_str[-4:]}"
