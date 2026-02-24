from src.widget import get_date
from src.widget import mask_account_card


def test_mask_account_card() -> None:
    assert mask_account_card("Visa 11112121589654789523") == "Visa  **9523"
    assert mask_account_card("Visa 1234567812341234") == "Visa  1234 56** **** 1234"


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.6714078") == "11.03.2024"
    assert get_date("") == "Дата отсутсвует"
