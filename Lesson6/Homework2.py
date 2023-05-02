# Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата,
# і повертає 3 значення (за допомогою кортежу): периметр квадрата, площа квадрата та діагональ квадрата.

def enter_number():
    while True:
        try:
            side = float(input('Enter the len of the side: '))
            return side

        except ValueError:
            print('Enter a valid value')


def square(side):

    perimetr = 4 * side
    area = side ** 2
    diagonal = round((2 * area) ** (0.5), 2)

    return perimetr, area, diagonal




