# 3. Написать три класса:
# 3.1 класс Справочник(Записная книга, Телефонная книга), описывающий взаимодействие с телефонным справочником.
# Объект этого класса аггрегирует в себе объекты другого класса - Запись(множество записей)
# 3.2 класс Запись(Абонент), хранящий такие данные: Имя, Фамилия(необязательно), Телефон, Дата рождения(необязательно).
# Обеспечить валидацию данных и запрет на изменение этих данных другим классом
# 3.3 класс Интерфейс, которые обеспечивает взаимодействие с пользователем, который вводит данные в терминал.
# Обеспечить защиту от неверного ввода
# 3.4 В функции __main__() написать точку входа и выхода их программы(для ввода пользователя).
#
# Данная программа должна обеспечить: добавление, удаление, редактирование записей с терминала.
# По умолчание в справочнике есть номера экстренных служб, которые нельзя удалить или изменить
# (ни юзеру, ни другому программисту).

import re
import unittest


class Subscriber:
    def __init__(self, name, phone, lastname=None, birthday=None):
        self.__name = name
        self.__lastname = lastname
        self.__phone = phone
        self.__birthday = birthday

    def __eq__(self, other):
        if isinstance(other, Subscriber):
            return self.__name == other.__name and self.__phone == other.__phone
        return False

    def __hash__(self):
        return hash((self.__name, self.__phone))

    def get_name(self):
        return self.__name

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def get_birthday(self):
        return self.__birthday

    def __str__(self):
        return f"{self.__name} {self.__lastname}, Phone: {self.__phone}, Birthday: {self.__birthday}"


class Directory:
    def __init__(self):
        self.__subscribers = []

    def add_subscriber(self, subscriber):
        self.__subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.__subscribers.remove(subscriber)

    def get_subscribers(self):
        return self.__subscribers

    def __str__(self):
        if len(self.__subscribers) == 0:
            return "The directory is empty."
        else:
            return "\n".join(str(subscriber) for subscriber in self.__subscribers)


class Interface:
    @staticmethod
    def phone_validate(phone):
        # Простая валидация: допускаются только цифры и символы +, -, (, )
        if re.match(r'^[\d+\-()]+$', phone):
            return True
        return False

    @staticmethod
    def date_validate(date):
        # Простая валидация: допускаются только цифры, точки и дефисы
        if re.match(r'^[\d.-]+$', date):
            return True
        return False

    @staticmethod
    def enter_sub():
        name = input("Enter name: ")
        lastname = input("Enter lastname (it is not necessary): ")
        phone = input("Enter phone: ")
        birthday = input("Enter birthday (it is not necessary): ")

        if not Interface.phone_validate(phone):
            raise ValueError("Wrong phone format")

        if birthday and not Interface.date_validate(birthday):
            raise ValueError("Wrong date format")

        return Subscriber(name, phone, lastname, birthday)


def main():
    directory = Directory()

    # Номера экстренных служб
    emergency = [
        Subscriber("Fire Department", "101"),
        Subscriber("Emergency", "103"),
        Subscriber("Police", "102")
    ]

    for i in emergency:
        directory.add_subscriber(i)

    while True:
        print("Menu:")
        print("1. Show all subscribers")
        print("2. Add subscriber")
        print("3. Remove subscriber")
        print("4. Exit")

        choose = input("Choose action: ")

        if choose == "1":
            print(directory)
        elif choose == "2":
            try:
                subscriber = Interface.enter_sub()
                directory.add_subscriber(subscriber)
                print("The subscriber was added.")
            except ValueError as e:
                print(f"Error: {str(e)}")
        elif choose == "3":
            remove_sub = Interface.enter_sub()
            if remove_sub in emergency:
                print("You can't delete this subscription.")
            else:
                directory.remove_subscriber(remove_sub)
                print("The subscriber was removed.")
        elif choose == "4":
            break
        else:
            print("Wrong choose. Try again")


if __name__ == '__main__':
    main()


class TestDirectory(unittest.TestCase):

    def test_add_subscriber(self):
        directory = Directory()
        subscriber = Subscriber("Иван", "12345")
        directory.add_subscriber(subscriber)
        self.assertEqual(directory.get_subscribers(), [subscriber])

    def test_remove_subscriber(self):
        directory = Directory()
        subscriber1 = Subscriber("Иван", "12345")
        subscriber2 = Subscriber("Петр", "54321")
        directory.add_subscriber(subscriber1)
        directory.add_subscriber(subscriber2)
        directory.remove_subscriber(subscriber1)
        self.assertEqual(directory.get_subscribers(), [subscriber2])


class TestSubscriber(unittest.TestCase):
    def test_get_name(self):
        subscriber = Subscriber("Иван", "12345")
        self.assertEqual(subscriber.get_name(), "Иван")

    def test_get_phone(self):
        subscriber = Subscriber("Иван", "12345")
        self.assertEqual(subscriber.get_phone(), "12345")


if __name__ == "__main__":
    unittest.main()

