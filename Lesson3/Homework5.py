# Користувач водить текст через пробіл.
# Конвертувати текст у список.
# Вивести остані 3 елементи зі списку,
# якщо список містить менше 3-х елементів, вивести повідомлення про те що кількість елементів менша за 3
# і вказати кількість елементів поточного списку

my_text = input('Enter your text: ')
my_list = my_text.split(' ')
if len(my_list) >= 3:
    print(my_list[-3:])
else:
    print(f'Your list has less than 3 elements, you have only {len(my_list)} elements')