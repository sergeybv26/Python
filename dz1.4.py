if __name__ == '__main__':

	number = int(input('Введите целое положительное число: '))
	max_num = 0
	while number > 0:
		digit = number % 10
		if digit >= max_num:
			max_num = digit
		number = number // 10
	print('Самая большая цифра в введенном числе:', max_num)