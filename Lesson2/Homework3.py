# Написати програму для підрахунку конвертації валюти: UAH --> USD
# USD --> UAH
# UAH --> EUR
# EUR --> UAH

print('Hello, I can change currency', 'I can work with USD, UAN, EUR', sep = '\n')

while True:
    cur1 = input('What do you want to change? (USD, UAN, EUR): ')
    cur2 = input('What do you want to get? (USD, UAN, EUR): ')
    val = input('Enter value of carrency: ')
    if ((cur1 and cur2) not in ('USD', 'UAN', 'EUR')) or not val.isnumeric():
        print('Please enter a valid currency (USD, UAN, EUR) or value (number)')
        if (n := input("For stopping programm enter 'Exit', for continuing enter any other symbol: ")) == 'Exit':
            break
    else:
        if (cur1 == 'UAN') and (cur2 == 'USD'):
            print(f'{val}{cur1} is {float(val)/36}{cur2}')
        elif (cur1 == 'UAN') and (cur2 == 'EUR'):
            print(f'{val}{cur1} is {float(val)/40}{cur2}')
        elif (cur1 == 'USD') and (cur2r2 == 'UAN'):
            print(f'{val}{cur1} is {float(val)*36}{cur2}')
        elif (cur1 == 'USD') and (cur2 == 'EUR'):
            print(f'{val}{cur1} is {float(val)/0.9}{cur2}')
        elif (cur1 == 'EUR') and (cur2 == 'UAN'):
            print(f'{val}{cur1} is {float(val)*40}{cur2}')
        elif (cur1 == 'EUR') and (cur2 == 'USD'):
            print(f'{val} {cur1} is {float(val)*0.9} {cur2}')
        break