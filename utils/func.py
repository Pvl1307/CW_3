import json

# Чтение данных из файла
with open('operations.json', encoding='utf-8') as file:
    data = json.load(file)


def get_executed_operations(data):
    '''
    Получение списка выполненных (EXECUTED) операций
    '''
    executed_list = []
    for item in data:
        if item.get('state') == 'EXECUTED':
            executed_list.append(item)
    return executed_list


def get_operation_date(operation):
    '''
    Получение даты с дальнейшей сортировкой выполненных операций
    '''
    return operation["date"]


# Получение списка выполненных операций
executed_operations = get_executed_operations(data)

# Сортировка операций по дате на возрастание
sorted_operations = sorted(executed_operations, key=get_operation_date)

# Вывод последних 5 операций
latest_operations = sorted_operations[-5:]


def hiden_card_number(card_number):
    '''
    Скрытие цифр счета(номера карты)
    '''
    if len(card_number) == 1:
        return card_number
    else:
        card_info = card_number.split()
        card_type = ' '.join(card_info[:-1])
        digits = card_info[-1]
        if len(digits) == 20:
            digits = f'**{digits[-4:]}'
        else:
            digits_ = digits[:6] + '******' + digits[-4:]
            digits = ' '.join([digits_[i:i + 4] for i in range(0, len(digits_), 4)])
        return f'{card_type} {digits}'


def print_last_operation(operations):
    '''
    Вывод операций в нужном стиле
    '''
    for operation in operations:
        date = operation['date'][:10]
        formatted_date = '.'.join(date.split('-')[::-1])

        description = operation['description']

        from_a = operation.get('from', ' ')
        from_ac = hiden_card_number(from_a)

        to_account = operation.get('to')
        to_a = hiden_card_number(to_account)

        amount = operation['operationAmount']['amount']
        name = operation['operationAmount']['currency']['name']
        print(f'{formatted_date} {description}')
        if from_a:
            print(f'{from_ac} -> {to_a}')
        print(f'{amount} {name}')
        print()


print_last_operation(latest_operations)
