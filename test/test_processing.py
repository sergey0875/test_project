import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.mark.parametrize("state, expected_count", [("EXECUTED", 2), ("CANCELED", 1), ("NON_EXISTENT", 0)])
def test_filter_by_state(sample_data: list[dict], state: str, expected_count: int) -> None:
    """корректность фильтрации"""
    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count


def test_sort_by_date(same_dates_data: list[dict]) -> None:
    """Тест: проверка одинаковых дат"""
    result = sort_by_date(same_dates_data)
    assert len(result) == 2
    assert result[0]["id"] == 1


def test_sort_by_date_empty() -> None:
    """Тест: Обработка пустого списка"""
    assert sort_by_date([]) == []
