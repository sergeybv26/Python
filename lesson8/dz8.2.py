if __name__ == '__main__':
    class OwnError(Exception):
        def __init__(self, txt):
            self.txt = txt

    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))

    try:
        if num2 == 0:
            raise OwnError('На ноль делить нельзя!')
        result = num1 / num2
    except OwnError as err:
        print(err)
    else:
        print(f'Результат деления первого числа на второе: {round(result, 2)}.')
