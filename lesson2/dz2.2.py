if __name__ == '__main__':
    my_list = list(input('Введите последовательность симолов для наполнения списка: '))
    new_list = []
    count = 0
    if len(my_list) == 2:
        new_list.insert(count, my_list[count + 1])
        new_list.insert(count + 1, my_list[count])
    for _ in range(len(my_list) - 2):
          if count + 1 <= len(my_list) - 1:
              new_list.insert(count, my_list[count + 1])
              new_list.insert(count + 1, my_list[count])
          count += 2
    if len(my_list) % 2 != 0:
        new_list.append(my_list[-1])
    print(new_list)