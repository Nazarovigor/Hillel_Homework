# Написать калькулятор с основными операциями(+, -, *, /)
# Користувач вводить два числа та арефметичну операцію

while True:
    num1, num2 = input('Enter number1: '), input('Enter number2: ')
    if not num1.isnumeric() or not num2.isnumeric():
        print('Please enter a numb')
        if (n := input("For stopping programm enter 'Exit', for continuing enter any other symbol: ")) == 'Exit':
            break
    else:
        while True:
            operand = input('Please enter operand (+, -, *, /): ')
            if operand in '+-*/':
                match operand:
                    case '+':
                        print(f'Result is {float(num1)+float(num2)}')
                        break
                    case '-':
                        print(f'Result is {float(num1)-float(num2)}')
                        break
                    case '*':
                        print(f'Result is {float(num1)*float(num2)}')
                        break
                    case '/':
                        print(f'Result is {float(num1)/float(num2)}')
                        break

            else:
                print('Please enter a valid operand')
        break