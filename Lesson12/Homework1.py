# Використовуючи модуль argparse створити програму розрахунку квадратного рівняння.
# (Реалізацію самого рівняння можете взяти з минулих ДЗ)
# Запуск програми python main.py -a={} -b={} c={} де параметри (a, b, c - параметри квадратного рівняння),
# за замовчуванням параметр а = 0
# При виклику програми з прапорцем --help вивести інформацію про програму та про параметри

import argparse


class DiscriminantError(Exception):
    def __str__(self):
        return f"Your discriminant is less than zero"


def calculate_discriminant(a, b, c):
    discriminant = int(b) ** 2 - 4 * int(a) * int(c)

    if discriminant < 0:
        raise DiscriminantError

    return discriminant


def main():
    parser = argparse.ArgumentParser(description='Program for solving quadratic equations.')

    parser.add_argument('-a', type=float, default=0, help='value for a')
    parser.add_argument('-b', type=float, help='value for b')
    parser.add_argument('-c', type=float, help='value for с')

    args = parser.parse_args()

    try:
        discr = calculate_discriminant(args.a, args.b, args.c)

        x1 = (-args.b + discr ** 0.5) / (2 * args.a)
        x2 = (-args.b - discr ** 0.5) / (2 * args.a)

        print(f"The solutions are x1 = {x1}, x2 = {x2}.")

    except DiscriminantError:
        raise DiscriminantError

    except ValueError:
        print('Wrong data, please try again')

    except ZeroDivisionError:
        print("You can't divide to zero")
