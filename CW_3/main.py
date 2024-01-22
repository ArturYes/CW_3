import os

from CW_3.utils import load_json, display_last_5_transactions

OPERATIONS_JSON = os.path.join("operations.json")


if __name__ == "__main__":
    data = load_json(OPERATIONS_JSON)
    if data:
        info_operation = display_last_5_transactions(data)
        print(info_operation)
    else:
        print('json file пустой')