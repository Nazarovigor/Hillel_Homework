# Створити декоратор який кожен раз буде записувати у файл результат роботи якоїсь функції після її виклику
# (наприклад функція яка прораховує суму всіх переданих аргументів *args).
# Запис в файл формату ""Function launched at {час запуску} with result {результат роботи функції}
import datetime
import time


def record_decorator(func):
    def wrapper(*args):
        with open('result.txt', 'a') as file:
            start_time = datetime.datetime.now()
            func_result = func(*args)
            file.write(f'Function launched at {start_time} with result {func_result}\n')
        return file
    return wrapper


@record_decorator
def my_sum(*args):
    try:
        result = sum(args)
    except TypeError:
        return 'Your args should be numbers only!!!'
    return result


# result1 = my_sum(1, 'd', 3)
# time.sleep(3)
# result2 = my_sum(1, 2, 3, 5)
# time.sleep(4)
# result3 = my_sum(1, 2, 3, 6)