# Створіть словник з чотирма назвами мов програмування
# (ключі) та іменами розробників цих мов (значення).
# Виведіть по черзі для усіх елементів словника повідомлення типу
# My favorite programming language is Python. It was created by Guido van Rossum..
# Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.

my_lang_dict = {'Python': 'Guido van Rossum', 'JS': 'Brendan Eich', 'C++': 'Bjarne Stroustrup', 'Java': 'James Gosling'}

for key, item in my_lang_dict.items():
    print(f'My favorite programming language is {key}. It was created by {item}.')

del my_lang_dict['JS']

print(my_lang_dict)
