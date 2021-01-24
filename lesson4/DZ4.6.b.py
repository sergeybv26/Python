from itertools import cycle

my_list = ['Вася', 'Таня', 'Федя', 'Надя']
count = 0

for i in cycle(my_list):
    if count > 11:
        break
    else:
        print(i)
    count += 1
