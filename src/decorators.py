from functools import wraps
from typing import Any
from typing import Optional


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"

                # Записываем успешный лог
                _write(log_message, filename)

                return result

            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                _write(message, filename)
                raise e

        return wrapper

    return decorator


def _write(message: str, filename: Optional[str]) -> None:
    """Вспомогательная функция куда отправить готовую строку"""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)


@log()
def my_function(a: int, b: int) -> float:
    return a / b
