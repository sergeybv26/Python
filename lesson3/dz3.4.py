if __name__ == '__main__':
	def my_func(x, y):
		"""Возвращает х в степени у"""
		return x ** y


	print(my_func(4, -2))

	"""=========================================="""
	def my_func1(x, y):
		"""Возвращает х в степени у без использования оператора **"""
		res_x = 1
		for _ in range(y, 0):
			res_x = x * res_x
		return 1 / res_x


	print(my_func1(4, -2))
