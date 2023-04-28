#Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'

# Varian1
print('+' if (word := input('Enter word: ')) == word[::-1] else '-')


# Variant2
# word = input('Enter word: ')
# if word == word[::-1]:
#     print('+')
# else:
#     print('-')