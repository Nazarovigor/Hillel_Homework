# Знайти ідентифікатор групи, де знаходиться найбільша кількість жінок, народжених після 1977 року.
# Як відповідь необхідно вказати через пробыл ідентифікатор знайденої групи
# і скільки в ній було жінок, народжених після 1977 року. Файл group_people.json

import json
import os


def file_validate(file):
    if os.path.exists(file):
        return file
    else:
        return "File doesn't exist"


def max_women(path, year=1977):
    try:
        with open(path) as f:
            file_dict = json.load(f)
            max_amount = 0
            id_group = None
            for group in file_dict:
                group_amount = 0
                for person in group['people']:
                    if (person['year'] > year) & (person['gender'] == 'Female'):
                        group_amount += 1
                if group_amount > max_amount:
                    max_amount = group_amount
                    id_group = group['id_group']
        return f'The biggest group is №{id_group}, it includes {max_amount} women who were born after {year} year'

    except json.decoder.JSONDecodeError:
        return 'There is a not valid data in the file'


if __name__ == '__main__':
    file = file_validate('group_people.json')
    print(max_women(file))
