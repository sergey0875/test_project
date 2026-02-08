from typing import Union


def get_mask_card_number(number_card: Union[str, int]) -> str:
    """Функция маскирует номер карты"""
    # Переводим в строку.
    number_card_str = str(number_card)
    # считаем количество введенных цифр и сравниваем с условием.
    if len(number_card_str) != 16:
        return "Неполный ввод,такой карты нет."
    # Выводим результат при помощи срезов
    return f"Карта Mir {number_card_str[:4]} {number_card_str[4:6]}** **** {number_card_str[12:]}"


print(get_mask_card_number(9811444477772822))


def get_mask_account(number_account: Union[str, int]) -> str:
    """Функция маскерует номер счета, оставляя только последние 4 цифры"""
    # выводим результат
    return f"Номер счета **{str(number_account)[-4:]}"


print(get_mask_account(25555555555559811444477772822555555555))
