if __name__ == '__main__':
	def my_func(var1, var2, var3):
		"""Возвращает сумму наибольших двух аргументов"""
		var_list = [var1, var2, var3]
		num_max1 = max(var_list)
		var_list.remove(num_max1)
		num_max2 = max(var_list)
		return num_max1 + num_max2


	print('Сумма двух наибольших аргументов равна:', my_func(5, 6, 7))
