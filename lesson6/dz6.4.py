if __name__ == '__main__':
    class Car:

        def __init__(self, speed, color, name, is_police=False):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_police

        def go(self):
            print('Автомобиль поехал')

        def stop(self):
            print('Автомобиль остановился')

        def turn(self, direction):
            print(f'Автомобиль повернул на {direction}')

        def show_speed(self):
            print(f'Скорость автомобиля составляет: {self.speed} км/ч')

    class TownCar(Car):

        def show_speed(self):
            if self.speed > 60:
                print('Превышение скорости!')
            else:
                print(f'Скорость автомобиля составляет: {self.speed} км/ч')

    class SportCar(Car):
        pass

    class WorkCar(Car):

        def show_speed(self):
            if self.speed > 40:
                print('Превышение скорости!')
            else:
                print(f'Скорость автомобиля составляет: {self.speed} км/ч')

    class PoliceCar(Car):
        pass

    car1 = TownCar(50, 'черный', 'BMW')
    print(car1.speed)
    print(car1.name)
    print(car1.color)
    print(car1.is_police)
    car1.go()
    car1.turn('лево')
    car1.show_speed()
    car1.stop()

    car2 = TownCar(65, 'синий', 'VW')
    print(car2.speed)
    print(car2.name)
    print(car2.color)
    print(car2.is_police)
    car2.go()
    car2.turn('право')
    car2.show_speed()
    car2.stop()

    car3 = SportCar(300, 'красный', 'Lamborghini')
    print(car3.speed)
    print(car3.name)
    print(car3.color)
    print(car3.is_police)
    car3.go()
    car3.turn('лево')
    car3.show_speed()
    car3.stop()

    car4 = WorkCar(35, 'белый', 'рено')
    print(car4.speed)
    print(car4.name)
    print(car4.color)
    print(car4.is_police)
    car4.go()
    car4.turn('право')
    car4.show_speed()
    car4.stop()

    car5 = WorkCar(45, 'белый', 'рено')
    car5.go()
    car5.turn('право')
    car5.show_speed()
    car5.stop()

    car6 = PoliceCar(180, 'белый', 'MercedesBenz', True)
    print(car6.speed)
    print(car6.name)
    print(car6.color)
    print(car6.is_police)
    car6.go()
    car6.turn('лево')
    car6.show_speed()
    car6.stop()
