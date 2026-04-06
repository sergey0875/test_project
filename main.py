from src.processing import filter_by_state, sort_by_date
from src.process_csv import load_csv_data, import_excel_data
from src.proccess_search import process_bank_search
from src.utils import get_transactions
from src.generators import filter_by_currency
from src.widget import mask_account_card


def main()-> None:
    """Функция соеденяющая все функции в одну для совместной работы"""

    # Приветствие и выбор файла
    print("Привет! Добро пожаловать в программу работы\nс банковскими транзакциями\nВыберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Пути до файлов.
    path_to_file = "C:/Users/sepaa/PycharmProjects/test_project/data/operations.json"
    path_to_file_1 = "C:/Users/sepaa/PycharmProjects/test_project/data/transactions.csv"
    path_to_file_2 = "C:/Users/sepaa/PycharmProjects/test_project/data/transactions_excel.xlsx"

    user_word = input().strip()

    if user_word == "1":
        print("Для обработки выбран JSON-файл.")
        data = get_transactions(path_to_file)
    elif user_word == "2":
        print("Для обработки выбран CSV-файл.")
        data = load_csv_data(path_to_file_1)
    elif user_word == "3":
        print("Для обработки выбран XLSX-файл.")
        data = import_excel_data(path_to_file_2)
    else:
        print("Неверный выбор.")
        return

    #  Фильтрация по статусу.
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    user_status = input().strip().upper()
    status_list = ["EXECUTED", "CANCELED", "PENDING"]

    if user_status in status_list:
        data = filter_by_state(data, user_status)
        print(f"Операции отфильтрованы по статусу {user_status}")
    else:
        print(f"Статус операции {user_status} недоступен.")

    # Сортировка по дате
    print("Отсортировать операции по дате? Да/Нет")
    if input().lower().strip() == "да":
        print("Отсортировать по убыванию? Да/Нет (Нет = по возрастанию)")
        user_data_sort = input().lower().strip()
        data = sort_by_date(data, reverse=(user_data_sort == "да"))
    else:
        print("Печально, сортировка пропущена.")

    # 4. Фильтрация по валюте (RUB)
    print("Выводить только рублевые транзакции? Да/Нет")
    if input().lower().strip() == "да":

        data = list(filter_by_currency(data, "RUB"))
    else:
        print("Выдаю все доступные валюты")

    #  Фильтрация по ключевому слову
    print("Отфильтровать список транзакций по определенному слову\nв описании? Да/Нет")
    if input().lower().strip() == "да":
        user_search = input("Введите слово: ").strip()

        data = process_bank_search(data, user_search)
    else:
        print("Пропускаю фильтрацию")

    #  Итоговый вывод
    print("Распечатываю итоговый список транзакций...")

    #  list() на случай, если предыдущие фильтры вернули итератор
    final_data = list(data)

    if not final_data:
        print("В этой выборке нет транзакций.")
    else:
        for trans in final_data:
            #  Дата и описание
            print(f"{trans.get('date')} {trans.get('description')}")

            # Маскировка (с защитой от nan/None)
            sender = trans.get("from")
            receiver = trans.get("to")

            if sender and str(sender).lower() != "nan":
                print(f"{mask_account_card(str(sender))} -> {mask_account_card(str(receiver))}")
            else:
                print(f"{mask_account_card(str(receiver))}")

            op_amt = trans.get("operationAmount")
            if isinstance(op_amt, dict):

                amount = op_amt.get("amount")
            else:

                amount = trans.get("amount")

            print(f"{amount}\n")


if __name__ == "__main__":
    main()
