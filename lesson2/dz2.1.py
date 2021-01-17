if __name__ == '__main__':
    my_list = [1, 2.3, complex(5, 6), 'строка', tuple('кортеж'), set('множество'),
               dict(who='мой', what='словарь'), None]
    for i in my_list:
        print(i)
        print('Тип данных:', type(i))
    print(my_list)
    print('Тип данных:', type(my_list))