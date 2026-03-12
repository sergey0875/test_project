from typing import Any

import pytest


@pytest.fixture
def sample_data() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def same_dates_data() -> list[dict]:

    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T12:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2024-01-01T12:00:00"},
    ]


@pytest.fixture
def transactions_data() -> list[dict[str, Any]]:
    return [
        {"id": 1, "description": "Перевод организации", "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "description": "Перевод со счета на счет", "operationAmount": {"currency": {"code": "RUB"}}},
        {"id": 3, "description": "Оплата услуг", "operationAmount": {"currency": {"code": "USD"}}},
    ]
