# Написать свой тип данных для сложения и вычитания, сравнение комплексных чисел.
# А так же правильного отображение их в консоли(magic method __str__).

class ComplexNumber:
    """Create a complex number"""

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self):
         return f"{self.real} + {self.imaginary}i"


z1 = ComplexNumber(3, 5)
z2 = ComplexNumber(3, 9)


print(z1 - z2)
print(z1 == z2)
print(z1+z2)
print(z1)