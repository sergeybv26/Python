if __name__ == '__main__':
    word_list = list(input('Введите слова: ').split())
    for ind, el in enumerate(word_list, 1):
        print(ind, el[:10])
