if __name__ == '__main__':
    numb_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    numb_word = []

    with open('file_5_4.txt') as f_obj:

        while True:
            f_str = f_obj.readline().split('-')

            if f_str == ['']:
                break

            numb_word.append(f_str)

    with open('file_5_4_new.txt', 'w') as f_obj:
        for i in range(len(numb_word)):
            key = numb_word[i][0]
            numb_word[i][0] = numb_dict.get(key)

            print(numb_word[i][0] + '-' + numb_word[i][1], file=f_obj)
