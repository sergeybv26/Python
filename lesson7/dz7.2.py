if __name__ == '__main__':

    from abc import ABC, abstractmethod

    class Clothes(ABC):

        @abstractmethod
        def q_cloth(self):
            pass

    class Coat(Clothes):

        def __init__(self, size):
            self.size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, size):
            if size < 30 or size > 72:
                self.__size = None
            else:
                self.__size = size

        def q_cloth(self):
            try:
                return round(self.size/6.5 + 0.5, 2)
            except Exception:
                return 'Ошибка в размере пальто! Размер пальто должен быть от 30 до 72.'

    class Suit(Clothes):
        def __init__(self, height):
            self.height = height

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            if height < 110 or height > 200:
                self.__height = None
            else:
                self.__height = height

        def q_cloth(self):
            try:
                return round(2 * self.height + 0.3, 2)
            except Exception:
                return 'Ошибка в размере костюма! Рост должен быть в диапазоне от 110 до 200 см'


    cl1 = Coat(50)
    print(cl1.q_cloth())
    cl2 = Suit(110)
    print(cl2.q_cloth())
    try:
        print(f'Для пошива одежды потребуется {cl1.q_cloth() + cl2.q_cloth()} м ткани')
    except TypeError:
        print('Введен неверный размер одежды!')
