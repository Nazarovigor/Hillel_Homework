# Створити реалізацію квадратного рівняння
# a•x²+b•x + c = 0
# (користувач вводить a, b, c),
# якщо дискримінант від'ємний - викликати виняток DiscriminantError і вивести відповідне повідомлення.

class DiscriminantError(Exception):
    def __str__(self):
        return f"Your discriminant is less than zero"


def calculate_discriminant(a, b, c):
    discriminant = int(b) ** 2 - 4 * int(a) * int(c)

    if discriminant < 0:
        raise DiscriminantError

    return discriminant


try:
    a = float(input())
    b = float(input())
    c = float(input())

    discr = calculate_discriminant(a, b, c)

    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)

    print(f"The solutions are x1 = {x1}, x2 = {x2}.")

except DiscriminantError:
    raise DiscriminantError

except ValueError:
    print('Wrong data, please try again')

