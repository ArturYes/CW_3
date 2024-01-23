from config import JSON_PATH
from src.utils import load_json, display_last_5_transactions


if __name__ == "__main__":
    # Получение данных json файла
    data = load_json(JSON_PATH)
    if data:
        # Получение информации о пяти транзакциях
        info_operation = display_last_5_transactions(data)
        print(info_operation)
    else:
        print('json file пустой')