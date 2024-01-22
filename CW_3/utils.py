import json
from datetime import datetime


def load_json(file_patch):
    with open(file_patch, 'r') as file:
        data = json.load(file)
    return data


def convert_date(date):
    date = date.split("T")[0].split("-")
    return f"{date[2]}.{date[1]}.{date[0]}"


def mask_card_number(card_number):
    if card_number:
        card_number1 = card_number.split()
        if card_number1[0].lower() == "счет":
            return mask_account_number(card_number)
        else:
            return f"{' '.join(card_number1[:-1])} {card_number1[-1][:4]} {card_number1[-1][4:6]}** **** {card_number1[-1][-4:]}"


def mask_account_number(account_number):
    account_number = account_number.split()
    return f"{account_number[0]} **{account_number[-1][-4:]}"


def display_transaction(transaction):
    date = convert_date(transaction['date'])
    description = transaction.get('description')
    operation_amount = (f'{transaction['operationAmount']['amount']} '
                        f'{transaction['operationAmount']['currency']['name']}')
    if transaction.get('from'):
        masked_from = mask_card_number(transaction.get('from', ''))
        masked_to = mask_card_number(transaction.get('to', ''))
    else:
        masked_from = '***'
        masked_to = mask_card_number(transaction.get('to', ''))

    return f"{date} {description}\n{masked_from} -> {masked_to}\n{operation_amount}"


def display_last_5_transactions(operations):
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    last_5_executed = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]

    output = ''
    for transaction in last_5_executed:
        output += display_transaction(transaction) + '\n\n'

    return output
