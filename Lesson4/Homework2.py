# Є список друзів ["John", "Marta", "James", "Amanda", "Marianna"].
# Виведіть імена в консолі, кожен з нового рядка, вирівнюючи праву сторону,
# використовуючи метод рядка та форматування через F String.
# Також над іменами першим рядком виведіть NAME, де NAME має бути посередині(string.center()),
# а решта простору заповнена символом "*"


# Вариант 1 - выравниваем по правой стороне самого длинного слова


my_friends_name = ["John", "Marta", "James", "Amanda", "Marianna"]
max_width = max(len(item) for item in my_friends_name)
title = 'name'
print(title.center(max_width, "*"))
for friend in my_friends_name:
    print(f'{friend.rjust(max_width)}')



# Вариант 2 - выравниваем по правой стороне консоли - запускать через консоль

# import shutil
#
# screen_width, _ = shutil.get_terminal_size()
#
# my_friends_name = ["John", "Marta", "James", "Amanda", "Marianna"]
# title = 'name'
# print(title.center(screen_width, "*"))
# for friend in my_friends_name:
#     print(f'{friend.rjust(screen_width)}')
#


# Вариант 3 - самый красивый при выводе))

# my_friends_name = ["John", "Marta", "James", "Amanda", "Marianna"]
# #max_width = max(len(item) for item in my_friends_name)
# title = 'name'
# print(title.center(16, "*"))
# for friend in my_friends_name:
#     print(f'{friend.rjust(16)}')