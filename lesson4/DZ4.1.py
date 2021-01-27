from sys import argv

script_name, hour, cost, prize = argv

wages = int(hour) * int(cost) + int(prize)
print('Заработная плата сотрудника составит:', wages)
