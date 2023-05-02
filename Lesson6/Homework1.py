# Дано натуральне число N.
# Виведіть слово YES, якщо число N є точним ступенем двійки, або слово NO інакше.
# 8 - YES, 3 - NO
from math import log


def enter_number():
    while True:
        try:
            number = int(input('Enter natural number: '))
            return number

        except ValueError:
            print('Your number is not natural')


def is_num_rec(number):
    num = log(number, 2)
    if num == int(num):
        return "YES"
    else:
        return "NO"



