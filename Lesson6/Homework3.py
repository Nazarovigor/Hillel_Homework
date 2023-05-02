# Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000,
# і повертає True, якщо це просте число, і False в іншому випадку.

def enter_number():
    while True:
        try:
            num = int(input('Enter a number from 2 to 1000: '))

            if num < 2 or num > 1000:
                print('You entered wrong number')
            else:
                return num

        except ValueError:
            print('You entered wrong number')


def is_prime(num):

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True




