from unittest.mock import mock_open
from unittest.mock import patch

import pandas as pd

from src.process_csv import import_excel_data
from src.process_csv import load_csv_data


def test_load_csv_data():
    # Имитируем содержимое CSV файла (заголовки и одна строка)
    csv_content = "id;amount;currency\n1;100;RUB"

    # Патчим open, чтобы он не лез на диск, а отдавал наш csv_content
    with patch("builtins.open", mock_open(read_data=csv_content)) as mocked_file:
        result = load_csv_data("fake_path.csv")

        # Проверяем результат
        assert result == [{"id": "1", "amount": "100", "currency": "RUB"}]
        mocked_file.assert_called_once_with("fake_path.csv", encoding="utf-8")


@patch("pandas.read_excel")
def test_import_excel_data(mock_read):
    # Создаем фейковый DataFrame
    mock_read.return_value = pd.DataFrame([{"id": 2, "amount": 500}])

    result = import_excel_data("fake.xlsx")

    # Проверяем, что функция правильно вызвала pandas и выдала список словарей
    assert result == [{"id": 2, "amount": 500}]
    mock_read.assert_called_once_with("fake.xlsx")
