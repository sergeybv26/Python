from sys import argv
from itertools import count

script_name, number = argv

number = int(number)

for i in count(number):
    if i > number + 10:
        break
    else:
        print(i)
