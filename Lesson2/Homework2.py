# Змішано V1 літрів води з температурою T1 та V2 літрів з температурою T2.
# Написати програму, яка порахує обєм і температуру суміші, що вийшла
# обчислюється за формулою (v1*t1 + v2*t2) / (v1 + v2)
# Всі параметри виводяться в консолі, вивести обьєм та температуру

while True:
    v1, t1 = input('Enter volume1: '), input('Enter temperature for volume1: ')
    v2, t2 = input('Enter volume2: '), input('Enter temperature for volume2: ')

    if not v1.isnumeric() or not t1.isnumeric() or not v2.isnumeric() or not t2.isnumeric():
        print('Please enter a correct value of volume or temperature')
        if (n := input("For stopping programm enter 'Exit', for continuing enter any other symbol: ")) == 'Exit':
            break



    else:
        print(f'Total volume is {float(v1) + float(v2)}')
        print(f'Total temperature is {(float(v1)*float(t1) + float(v2)*float(t2)) / (float(v1) + float(v2))}')
        break