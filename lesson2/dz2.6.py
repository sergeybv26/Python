if __name__ == '__main__':
    goods_list = []
    count = 1
    goods_prop = {}
    name_set = set()
    cost_set = set()
    quantity_set = set()
    unit_set = set()
    while True:
        name = input('Введите наименование товара: ')
        cost = input('Введите цену товара: ')
        quantity = input('Введите количество товара: ')
        unit = input('Введите единицу измерения товара: ')
        goods_list.append((count, {'название': name, 'цена': cost, 'количество': quantity, 'ед': unit}))
        user_answer = input('Добавить еще один товар? (да - введите д, нет - нажмите Enter): ')
        if user_answer.lower() != 'д':
            break
        count += 1
    for i in range(len(goods_list)):
        name_set.add(goods_list[i][1].get('название', 'Товар без названия'))
        cost_set.add(goods_list[i][1].get('цена', 'цена не указана'))
        quantity_set.add(goods_list[i][1].get('количество', 'количество не указано'))
        unit_set.add(goods_list[i][1].get('ед', 'единица измерения не указана'))
    goods_prop['название'] = list(name_set)
    goods_prop['цена'] = list(cost_set)
    goods_prop['количество'] = list(quantity_set)
    goods_prop['ед'] = list(unit_set)
    print(goods_list)
    print(goods_prop)
