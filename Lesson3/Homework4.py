# Написати валідатор для пошти.
# Користувач вводить пошту, а програма повинна перевірити, що в пошті є символ '@' і '.',
# і якщо це так, вивести "YES", інакше "NO"

my_mail = input('Enter your email: ')
if ('@' and '.') in my_mail:
    position1 = my_mail.index('@')
    position2 = my_mail.index('.')
    print('YES' if position1 < position2 else 'NO')
else:
    print('NO')