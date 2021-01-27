if __name__ == '__main__':
    from random import randint

    number_list = []
    num_sum = 0

    for i in range(11):
        number_list.append(str(randint(1, 100)))

    numb_str = ' '.join(number_list)

    with open('file_5_5.txt', 'w') as f_obj:
        f_obj.write(numb_str)

    with open('file_5_5.txt', 'r+') as f_obj:

        f_str = f_obj.readline().split()

    for el in f_str:
        num_sum += int(el)

    print(f'Сумма чисел равна: {num_sum}')
