import json
from utils import display_last_5_transactions


if __name__ == "__main__":
    with open('operations.json', 'r') as file:
        data = json.load(file)
        display_last_5_transactions(data)
