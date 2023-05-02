# Напишіть функцію sum_range(start, end),
# яка підсумовує всі цілі числа від значення start до величини end включно.
# Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.

def enter_numbers():
    while True:
        try:
            start = int(input('Enter start point: '))
            end = int(input('Enter end point: '))
            if start > end:
                start, end = end, start
            return start, end
        except ValueError:
            print('Wrong numbers')


def sum_range(first, second):
    return sum(range(first, second+1))


