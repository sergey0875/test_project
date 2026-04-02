from unittest.mock import mock_open
from unittest.mock import patch

from src.utils import get_transactions


def test_get_transactions_success():
    """Файл успешно прочитан и содержит список"""
    # Данные, которые мы хотим «прочитать» из файла
    mock_data = '[{"id": 1, "amount": 100}]'

    # patch заменяет встроенную функцию open на специальный mock_open
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_transactions("data/operations.json")

        assert result == [{"id": 1, "amount": 100}]
        assert isinstance(result, list)


def test_get_transactions_file_not_found():
    """Тест: Файл не найден (FileNotFoundError)"""
    # side_effect заставляет mock выбросить ошибку при вызове
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = get_transactions("non_existent.json")

        assert result == []


def test_get_transactions_invalid_json():
    """Тест: В файле не JSON (JSONDecodeError)"""
    # Имитируем «битый» файл
    with patch("builtins.open", mock_open(read_data="не валидный json")):
        result = get_transactions("bad.json")

        assert result == []
