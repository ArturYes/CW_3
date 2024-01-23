import json
import pytest
from src.utils import (load_json, mask_account_number, convert_date, display_transaction, mask_card_number,
                       display_last_5_transactions)
from config import TEST_JSON_PATH, TEST_2_JSON_PATH


@pytest.fixture
def transaction():
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
    return test_dict


def test_load_json():
    """Тест для загрузки json"""
    assert load_json(TEST_2_JSON_PATH) == [1, 2, 3]


def test_mask_account_number():
    """Тест для маскировки счета"""
    assert mask_account_number("Счет 96527012349577388612") == "Счет **8612"


def test_convert_date():
    """Тест для конвертации даты"""
    assert convert_date("2019-01-05T00:52:30.108534") == "05.01.2019"


def test_display_transaction(transaction):
    """Тест для получения информации о транзакции"""
    assert display_transaction(transaction) == ('05.01.2019 Перевод со счета на счет\n'
                                                'Счет **8409 -> Счет **8266\n'
                                                '87941.37 руб.')


def test_mask_card_number():
    """Тест для маскировки карты"""
    assert mask_card_number("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"


def test_display_last_5_transactions():
    """Тест для получения последних пяти транзакций """
    with open(TEST_JSON_PATH) as file:
        data_json = json.load(file)
    assert display_last_5_transactions(data_json) == ('26.08.2019 Перевод организации\n'
                                                      'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                                      '31957.58 руб.\n\n'
                                                      '19.08.2018 Перевод с карты на карту\n'
                                                      'Visa Classic 6831 98** **** 7658 -> '
                                                      'Visa Platinum 8990 92** **** 5229\n'
                                                      '56883.54 USD\n\n'
                                                      '23.03.2018 Открытие вклада\n'
                                                      '*** -> Счет **2431\n'
                                                      '48223.05 руб.\n\n')




