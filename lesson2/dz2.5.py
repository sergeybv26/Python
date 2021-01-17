if __name__ == '__main__':
    my_list = [7, 5, 3, 3, 2]
    user_number = int(input('Введите новый элемент рейтинга: '))
    for i in range(len(my_list)):
        if user_number > my_list[i]:
            my_list.insert(i, user_number)
            break
        elif user_number < my_list[i] and i < len(my_list) - 1:
            continue
        elif i == len(my_list) - 1:
            my_list.append(user_number)
    print(my_list)
