if __name__ == '__main__':
    class ComplexNumber:
        def __init__(self, complex_number):
            self.complex_number = complex_number

        def __add__(self, other):
            return ComplexNumber(self.complex_number + other.complex_number)

        def __mul__(self, other):
            return ComplexNumber(self.complex_number * other.complex_number)

        def __str__(self):
            return f'Результат выполнения операции: {self.complex_number}'


    cn1 = ComplexNumber(1+2j)
    cn2 = ComplexNumber(4+6j)

    print(cn1 + cn2)
    print(cn1 * cn2)
