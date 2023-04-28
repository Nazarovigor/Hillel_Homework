#Користувач водить рядок. Якщо він починається на 'abc', замінити їх на 'www', інакше додати в кінець рядка 'zzz'.
original_string = input('Enter the string: ')
if original_string[:3] == 'abc':
    print(original_string.replace('abc', 'www'))
else:
    print(original_string + 'zzz')