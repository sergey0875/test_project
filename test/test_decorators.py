import os

import pytest

from src.decorators import log


# вывод в консоль через capsys)
def test_log_success_console(capsys):
    @log()  # filename не задан, значит будет print
    def add(a: int, b: int) -> float:
        return a + b

    add(1, 2)

    # capsys перехватывает всё, что ушло в print
    captured = capsys.readouterr()

    # Проверяем, что в консоль вывелось имя_функции ok
    assert captured.out.strip() == "add ok"


# Ошибка (вывод в консоль через capsys)
def test_log_error_console(capsys):
    @log()
    def my_function(a: int, b: int) -> float:
        return a / b

    # Проверяем, что ошибка пробрасывается дальше (raise e)
    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    # Перехватываем вывод ошибки в консоль
    captured = capsys.readouterr()

    # Проверяем формат строки ошибки
    assert "my_function error: ZeroDivisionError" in captured.out


# Успешное выполнение (запись в ФАЙЛ)
def test_log_to_file() -> None:
    test_filename = "test_log.txt"

    # Удаляем файл, если он остался от прошлых запусков
    if os.path.exists(test_filename):
        os.remove(test_filename)

    @log(filename=test_filename)
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(3, 3)

    # Читаем созданный файл
    with open(test_filename, "r", encoding="utf-8") as f:
        content = f.read().strip()

    assert content == "multiply ok"

    # Удаляем временный файл после теста
    os.remove(test_filename)
