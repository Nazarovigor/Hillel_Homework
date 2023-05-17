# Написать класс для сущности Точка(содержит в себе координаты Х и Y).
# Написать классы для сущностей Треугольник, Квадрат, которые аггрегируют объекты класса Точка.
#
# Написать методы, которые считают площадь фигур, если координаты введены правильно.
# Если нет, то показать сообщение об ошибке

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:

    def __init__(self, a, b, c):
        # Проверяем, что координаты вершин не совпадают
        if a.x == b.x == c.x and a.y == b.y == c.y:
            raise ValueError("Все вершины находятся в одной точке")
        # Проверяем, что вершины не лежат на одной прямой
        if (b.y - a.y) * (c.x - b.x) == (c.y - b.y) * (b.x - a.x):
            raise ValueError("Вершины лежат на одной прямой")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Вычисляем длины сторон треугольника
        ab = ((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2) ** 0.5
        bc = ((self.b.x - self.c.x) ** 2 + (self.b.y - self.c.y) ** 2) ** 0.5
        ca = ((self.c.x - self.a.x) ** 2 + (self.c.y - self.a.y) ** 2) ** 0.5

        # Вычисляем полупериметр треугольника
        p = (ab + bc + ca) / 2

        # Вычисляем площадь треугольника по формуле Герона
        return (p * (p - ab) * (p - bc) * (p - ca)) ** 0.5


class Square:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        # Вычисляем длину стороны квадрата
        ab = ((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2) ** 0.5

        # Проверяем, что все стороны квадрата равны
        if ((self.b.x - self.c.x) ** 2 + (self.b.y - self.c.y) ** 2) ** 0.5 != ab:
            raise ValueError("You entered wrong coordinates")

        return ab**2


a: Point = Point(0, 0)
b: Point = Point(0, 1)
c: Point = Point(1, 1)
d: Point = Point(1, 0)

triangle: Triangle = Triangle(a, b, c)

print(round(triangle.area(), 2))

# square: Square = Square(a, b, c, d)
#
# print(square.area())