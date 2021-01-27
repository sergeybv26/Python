if __name__ == '__main__':
    with open('file_5_1.txt', 'w') as f_obj:

        while True:
            user_data = input('Введите строку для записи в файл: ')
            if user_data != '':
                f_obj.write(user_data + '\n')
            else:
                break
