if __name__ == '__main__':
    from functools import reduce

    my_list = [el for el in range(100, 1001) if el % 2 == 0]
    proizv = reduce(lambda a, b: a * b, my_list)

    print('Произведение чисел сгенерированного списка равно:', proizv)
