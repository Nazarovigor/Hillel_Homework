#Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, вивести 'YES', інакше 'NO'

my_string = input('Enter your string: ')
find_word = input('Enter the word for searching: ')
if find_word in my_string:
    print('YES')
else:
    print('NO')