import csv
from typing import Any

import pandas as pd


def load_csv_data(transactions: str) -> list[dict[str, Any]]:
    """Функция для считывания csv файла и возврата списка словарей."""

    with open(transactions, encoding="utf-8") as file:  # Открываем файл csv
        reader = csv.DictReader(file, delimiter=";")
        result = []
        for row in reader:  # Итерация по файлу csv
            result.append(row)
        return result  # Возвращаем список словарей


def import_excel_data(transactions_two: str) -> list[dict[str, Any]]:
    """Функция для считывания Exсel файла"""
    df = pd.read_excel(transactions_two)
    result = df.to_dict(orient="records")
    return result


# print(import_excel_data("C:/Users/sepaa/PycharmProjects/test_project/data/transactions_excel.xlsx"))
# print(load_csv_data("C:/Users/sepaa/PycharmProjects/test_project/data/transactions.csv"))
