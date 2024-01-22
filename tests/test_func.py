import json

from CW_3.utils import mask_account_number,convert_date,display_transaction,mask_card_number,display_last_5_transactions
from config import TEST_JSON_PATH

def test_mask_account_number():
    assert mask_account_number("Счет 96527012349577388612") == "Счет **8612"

def test_convert_date():
    assert convert_date("2019-01-05T00:52:30.108534") == "05.01.2019"

def test_display_transaction():
    test_dict = {
        "id": 957763565,
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534",
        "operationAmount": {
          "amount": "87941.37",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 46363668439560358409",
        "to": "Счет 18889008294666828266"
      }
    assert display_transaction(test_dict) == """05.01.2019 Перевод со счета на счет\nСчет **8409 -> Счет **8266\n87941.37 руб."""

def test_mask_card_number():
    assert mask_card_number("Счет 19628854383215954147") == "Счет **4147"

def test_display_last_5_transactions():
    with open(TEST_JSON_PATH) as file:
        data_json = json.load(file)
    assert display_last_5_transactions(data_json) == ('26.08.2019 Перевод организации\n'
                                                     'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                                     '31957.58 руб.\n\n'
                                                     '19.08.2018 Перевод с карты на карту\n'
                                                     'Visa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229\n'
                                                     '56883.54 USD\n\n'
                                                     '23.03.2018 Открытие вклада\n'
                                                     '*** -> Счет **2431\n'
                                                     '48223.05 руб.\n\n')




