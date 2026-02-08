from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card_number: str) -> str:
    """Функция маскирует номер счета или карты"""

    parts = account_card_number.split()  # Разделяем строку на слова.

    number = parts[-1]  # Берем последнее слово из строки.
    name_parts = parts[:-1]  # Исключаем последнее слово при помощи среза.

    name = " ".join(name_parts)  # Соединяем слова для проверки кроме последнего.

    # Проверяем карта или счет по количеству цифр и вызывается соответствующая функлия.
    if len(number) == 16:
        masked_number = get_mask_card_number(number)
    else:
        masked_number = get_mask_account(number)
