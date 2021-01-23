if __name__ == '__main__':
	def division_num(numf1, numf2):
		"""Возвращает частное от деления

		num 1 -- делимое
		num 2 -- делитиль
		"""
		if numf2 == 0:
			return 'На ноль делить нельзя!'
		else:
			return f'В результате деления числа {numf1} на число {numf2} получим число {round(numf1 / numf2, 2)}'


	num1 = int(input('Введите первое число: '))
	num2 = int(input('Введите второе число: '))
	print(division_num(num1, num2))
