#Створити декоратор який вимірює час виконання функції

import time
import datetime


def time_decorator(func):
    def wrapper():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        result = end_time - start_time
        return result
    return wrapper


@time_decorator
def example():
    time.sleep(3)
    print('Hello World!')


#print(example())

