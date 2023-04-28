# Написати програму, яка вміє переводити температуру з C в Фаренгетів і Кельвінів Наприклад: дана температура в Цельсіях 25 С
# Фаренгейт: 45.9F - вважається за формулою (C+32) * 5/9
# Кельвіни: 298.16K - вважається за формулою C + 273.16


while True:
    temp_сel = input('Enter temperature in Celsius: ')
    if not temp_сel.isnumeric():
        print('Please enter a numb')
    else:
        while True:
            convert_temp = input('What temperature to convert? Kelvin - K, Fahrenheit - F: ')
            if convert_temp == 'K':
                print(f'{float(temp_сel)} degrees Celsius equals {float(temp_сel) + 273.16} degrees Kelvin')
                break
            elif convert_temp == 'F':
                print(f'{float(temp_сel)} degrees Celsius equals {(float(temp_сel) * 1.8 + 32)} degrees Fahrenheit')
                break
            else:
                print('Please enter valid value (F or K)')
        break