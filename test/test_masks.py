from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234567812345678") == " 1234 56** **** 5678"
    assert get_mask_card_number("") == "Неполный ввод,такой карты нет."
    assert get_mask_card_number("1235467") == "Неполный ввод,такой карты нет."
    assert get_mask_account("12345678912345689789") == " **9789"
    assert get_mask_account("") == "Неправильный ввод."
    assert get_mask_account("112535657") == "Неправильный ввод."
