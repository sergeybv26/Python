if __name__ == '__main__':
    from abc import ABC, abstractmethod

    class Clothes(ABC):
        @abstractmethod
        def coat(self, size):
            pass

        @abstractmethod
        def suit(self, size):
            pass

    class Cloth(Clothes):
        def __init__(self, quantity_cloth=0):
            self.quantity_cloth = quantity_cloth

        def coat(self, size):
            self.quantity_cloth = round(size / 6.5 + 0.5, 2)

        def suit(self, size):
            self.quantity_cloth = round(2 * size + 0.3, 2)

        def __add__(self, other):
            return Cloth(self.quantity_cloth + other.quantity_cloth)

        def __str__(self):
            return f'Для пошива одежды потребуется {self.quantity_cloth} м ткани'

        # @property
        # def quantity_cloth(self):
        #     return self.__quantity_cloth
        #
        # @quantity_cloth.setter
        # def quantity_cloth(self, type_clothes):
        #     if type_clothes.lowercase() == 'пальто':
        #         self.__quantity_cloth = self.size / 6.5 + 0.5
        #     elif type_clothes.lowercase() == 'костюм':
        #         self.__quantity_cloth = 2 * self.size + 0.3
        #
        # def __add__(self, other):
        #     return Cloth()

    closes1 = Cloth()
    closes2 = Cloth()
    closes1.coat(50)
    closes2.suit(50)
    print(closes1 + closes2)
