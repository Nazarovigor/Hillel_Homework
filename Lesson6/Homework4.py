# Напишіть функцію change_list, яка приймає список і змінює місця його перший і останній елемент.
# У вихідному списку щонайменше 2 елементи.

def enter_list():
    while True:
        my_list = input('Enter elements of your list separated by a space: ').split(' ')

        if len(my_list) < 2:
            print('Enter more than 1 elements')
        else:
            return my_list

def change_list(my_list):

        my_list[0], my_list[-1] = my_list[-1], my_list[0]

        return my_list
