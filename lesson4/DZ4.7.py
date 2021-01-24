if __name__ == '__main__':
    from math import factorial

    def fact(num):
        for i in range(1, num + 1):
            yield factorial(i)


    number = int(input('Введите число: '))

    for el in fact(number):
        print(f'Факториал числа равен: {el}')
