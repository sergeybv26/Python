if __name__ == '__main__':
    class Road:

        def __init__(self, length, width):
            self._length = length
            self._width = width

        def mass_asf(self):
            mass_m2 = 25
            thickness = 5
            print(f'Для покрытия дорожного полотна шириной {self._width} м и '
                  f'длиной {self._length} м потребуется '
                  f'{int(self._width * self._length * mass_m2 * thickness / 1000)} т асфальта')

    road_asf = Road(5000, 20)
    road_asf.mass_asf()
