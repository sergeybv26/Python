if __name__ == '__main__':
    count_str = 0
    worker_list = []
    salary_sum = 0

    with open('file_5_3.txt', encoding='utf-8') as f_obj:

        while True:
            f_str = f_obj.readline().split()

            if not f_str:
                break

            count_str += 1

            if int(f_str[1]) < 20000:
                worker_list.append(f_str[0])

            salary_sum += int(f_str[1])

    print('Оклад менее 20 тыс. имеют сотрудники: ', end='')
    print(*worker_list, sep=', ')

    print(f'Средняя величина дохода сотрудников составляет: {salary_sum / count_str} рублей')
