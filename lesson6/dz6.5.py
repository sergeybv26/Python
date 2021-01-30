if __name__ == '__main__':
    class Stationery:

        def __init__(self, title):
            self.title = title

        def draw(self):
            print('Запуск отрисовки')

    class Pen(Stationery):

        def draw(self):
            print(f'Выполняется отрисовка {self.title} ручкой')

    class Pencil(Stationery):

        def draw(self):
            print(f'Выполняется отрисовка {self.title} карандашом')

    class Handle(Stationery):

        def draw(self):
            print(f'Выполняется отрисовка {self.title} маркером')


    dr1 = Pen('портрет')
    dr1.draw()
    dr2 = Pencil('пейзаж')
    dr2.draw()
    dr3 = Handle('калиграфия')
    dr3.draw()
