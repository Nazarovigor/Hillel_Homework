# Знайти найуспішнішого менеджера за підсумковою сумою продажів.
# Як відповідь потрібно через пробыл вказати спершу його ім'я, потім прізвище і після загальну суму його продажів.
# Файл manager_sales.json

import json
from Homework1 import file_validate


def best_salesperson(sales):
    with open(sales) as f:
        managers_dict = json.load(f)
        max_sales = 0
        first_name = None
        last_name = None
        for manager in managers_dict:
            total_manager = 0
            for car in manager['cars']:
                total_manager += car['price']
            if total_manager > max_sales:
                max_sales = total_manager
                first_name = manager['manager']['first_name']
                last_name = manager['manager']['last_name']
        return f'The best sales manager is {first_name} {last_name}, his result is {max_sales}'


if __name__ == '__main__':
    file = file_validate('manager_sales.json')
    print(best_salesperson(file))