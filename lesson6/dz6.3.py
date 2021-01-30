if __name__ == '__main__':
    class Worker:

        def __init__(self, name, surname, position, wage, bonus):
            self.name = name
            self.surname = surname
            self.position = position
            self._income = {'wage': wage, 'bonus': bonus}


    class Position(Worker):

        def get_full_name(self):
            return f'Полное имя сотрудника: {self.name} {self.surname}'

        def get_total_income(self):
            return f'Доход с учетом премии составляет: {self._income.get("wage") + self._income.get("bonus")} рублей'


    w1 = Position('Иван', 'Иванов', 'маркетолог', 50000, 2000)
    w2 = Position('Петр', 'Петров', 'водитель', 100000, 1000)

    print(f'Имя: {w1.name}')
    print(f'Фамилия: {w1.surname}')
    print(f'Должность: {w1.position}')
    print(f'Доход: {w1._income}')
    print(w1.get_full_name())
    print(w1.get_total_income())

    print(f'Имя: {w2.name}')
    print(f'Фамилия: {w2.surname}')
    print(f'Должность: {w2.position}')
    print(f'Доход: {w2._income}')
    print(w2.get_full_name())
    print(w2.get_total_income())
