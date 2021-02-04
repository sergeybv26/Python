if __name__ == '__main__':
    class Cell:

        def __init__(self, quantity_cell):
            self.quantity_cell = quantity_cell

        def __add__(self, other):
            return Cell(self.quantity_cell + other.quantity_cell)

        def __sub__(self, other):
            if self.quantity_cell - other.quantity_cell > 0:
                return Cell(self.quantity_cell - other.quantity_cell)
            else:
                return 'Ошибка! В результате вычитания клеток получилось отрицательное число'

        def __mul__(self, other):
            return Cell(self.quantity_cell * other.quantity_cell)

        def __truediv__(self, other):
            return Cell(round(self.quantity_cell / other.quantity_cell))

        def __str__(self):
            return f'Результат выполнения операции с клетками равен: {self.quantity_cell}'

        def make_order(self, cell_in_row):
            result = ''
            q_row = 0
            while self.quantity_cell > cell_in_row:
                result += '*' * cell_in_row + '\n'
                self.quantity_cell -= cell_in_row
            result += '*' * self.quantity_cell
            return result


    c1 = Cell(5)
    c2 = Cell(2)
    print(c1 + c2)
    print(c1 - c2)
    print(c2 - c1)
    print(c1 * c2)
    print(c1 / c2)

    c3 = Cell(12)
    print(c3.make_order(5))

    c4 = Cell(15)
    print(c4.make_order(5))