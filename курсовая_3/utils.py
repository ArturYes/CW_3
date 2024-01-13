import json
from datetime import datetime


def convert_date(date):
    date = date.split("T")[0].split("-")
    return f"{date[2]}.{date[1]}.{date[0]}"

def mask_card_number(card_number):
    if card_number:
        card_number1 = card_number.split()
        if card_number1[0] == "Счет":
            return mask_account_number(card_number)
        return f"{' '.join(card_number1[:-1])} {card_number1[-1][:4]} {card_number1[-1][4:6]}** **** {card_number1[-1][-4:]}"


def mask_account_number(account_number):
    account_number = account_number.split()
    return f"{account_number[0]} **{account_number[1][-4:]}"


def display_transaction(transaction):
    date = convert_date(transaction['date'])
    masked_from = mask_card_number(transaction.get('from', ''))
    masked_to = mask_account_number(transaction.get('to', ''))

    print(f"{date} {transaction['description']}")
    print(f"{masked_from} -> {masked_to}")
    print(f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")

def display_last_5_transactions(operations):
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    last_5_executed = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]

    for transaction in last_5_executed:
        display_transaction(transaction)
        print()
