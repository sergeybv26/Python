if __name__ == '__main__':

	revenue = int(input('Введите выручку фирмы: '))
	cost = int(input('Введите сумму издержек фирмы: '))
	profit = revenue - cost
	if profit > 0:
		print('Фирма работает с прибылью')
		print(f'Рентабельность выручки составляет: {profit / revenue:.2f}')
		num_of_staff = int(input('Введите численность сотрудников: '))
		print(f'Прибыль фирмы в расчете на одного сотрудника равна: {profit / num_of_staff:.2f}')
	else:
		print('Фирма работает в убыток')