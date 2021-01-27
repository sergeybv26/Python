if __name__ == '__main__':
    count_str = 0

    with open('file_5_2.txt') as f_obj:

        while True:
            f_str = f_obj.readline().split()

            if not f_str:
                break

            count_str += 1
            print(f'В строке {count_str} имеется {len(f_str)} слов')

    print(f'Всего в файле {count_str} строк')
