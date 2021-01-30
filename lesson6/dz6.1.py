from time import sleep

if __name__ == '__main__':

    class TrafficLight:

        __color = ['красный', 'желтый', 'зеленый']

        def running(self):

            print(f'На светофоре включен {self.__color[0]} огонь.')
            sleep(7)

            print(f'На светофоре включен {self.__color[1]} огонь.')
            sleep(2)

            print(f'На светофоре включен {self.__color[2]} огонь.')
            sleep(10)




    lights = TrafficLight()
    lights.running()
