# Напишіть інтерактивний калькулятор.
# Передбачається, що користувач вводить формулу, що складається з числа, оператора (як мінімум + і -) та іншого числа,
# розділених пробілом (наприклад, 1 + 1). Використовуйте str.split()
#
# a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн FormulaError.
#
# b. Спробуйте перетворити перший і третій елемент на float ( float_value = float(str_value)).
# Спіймайте будь-яку ValueError і згенеруйте замість нього FormulaError
#
# c. Якщо другий елемент не є «+» або «-», киньте ексепшн FormulaError


# Вариант 1 с + и -
class FormulaError(Exception):
    def __str__(self):
        return f"You make a mistake in the formula"


try:
    formula = input()
    list_formula = formula.split(' ')
    a, operand, b = list_formula

    if len(list_formula) != 3:
        raise FormulaError
    elif operand not in '+-':
        raise FormulaError

    float_a = float(a)
    float_b = float(b)

    print(f'The result of {formula} is {eval(formula)}')

except ValueError:
    raise FormulaError


# Вариант 2 где можно писать длинную формулу Например 2 + 3 * 3 - 1
# class FormulaError(Exception):
#     def __str__(self):
#         return f"You make a mistake in the formula"
#
#
# try:
#     formula = input()
#     list_formula = formula.split(' ')
#
#     for i in list_formula[1::2]:
#         if i not in '+-*/':
#             raise FormulaError
#     if len(list_formula) < 3:
#         raise FormulaError
#     else:
#         ...
#
#     for i in list_formula[::2]:
#         float(i)
#
#
#     print(f'The result of {formula} is {eval(formula)}')
#
# except NameError:
#     raise FormulaError
#
# except ValueError:
#     raise FormulaError
#
