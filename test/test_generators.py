from typing import Any

import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions

# --- Тесты для filter_by_currency ---


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),
        ("RUB", 1),
        ("EUR", 0),  # Случай, когда транзакции в валюте отсутствуют
    ],
)
def test_filter_by_currency(transactions_data: list[dict[str, Any]], currency: str, expected_count: int) -> None:
    result = list(filter_by_currency(transactions_data, currency))
    assert len(result) == expected_count
    for item in result:
        assert item["operationAmount"]["currency"]["code"] == currency


def test_filter_by_currency_empty_list() -> None:
    # Проверка работы с пустым списком
    assert list(filter_by_currency([], "USD")) == []


@pytest.mark.parametrize(
    "input_data, expected_outputs",
    [
        ([{"description": "A"}, {"description": "B"}], ["A", "B"]),
        ([{"description": "Тест"}], ["Тест"]),
        ([], []),  # Пустой список
    ],
)
def test_transaction_descriptions(input_data: list[dict[str, Any]], expected_outputs: list[str]) -> None:
    result = list(transaction_descriptions(input_data))
    assert result == expected_outputs


# --- Тесты для card_number_generator ---


@pytest.mark.parametrize(
    "start, stop, expected_first, expected_last, total",
    [
        (1, 2, "0000 0000 0000 0001", "0000 0000 0000 0002", 2),
        (9999999999999999, 9999999999999999, "9999 9999 9999 9999", "9999 9999 9999 9999", 1),
    ],
)
def test_card_number_generator_logic(
    start: int, stop: int, expected_first: str, expected_last: str, total: int
) -> None:
    gen = card_number_generator(start, stop)
    results = list(gen)

    assert len(results) == total
    assert results[0] == expected_first
    assert results[-1] == expected_last


def test_card_number_generator_format() -> None:
    # Проверка именно формата (16 цифр + 3 пробела = 19 символов)
    gen = card_number_generator(1, 1)
    card = next(gen)
    assert len(card) == 19
    assert card.count(" ") == 3
    # Проверяем, что это цифры (после удаления пробелов)
    assert card.replace(" ", "").isdigit()
