if __name__ == '__main__':
	def int_funct(word):
		"""Выполняет замену первой буквы каждого слова со строчной на прописную"""

		return word.title()
		# first_symb = ord(word[0])
		# first_symb = first_symb - 32
		# new_word = chr(first_symb) + word[1:]
		# return new_word

	user_word = input('Введите слово строчными латинскими буквами: ')
	print('Преобразованное слово:', int_funct(user_word))

	user_str = input('Введите строку из слов, разделенных пробелами: ')
	print('Преобразованная строка:', int_funct(user_str))

	# user_str = input('Введите строку из слов, разделенных пробелами: ').split()
	# for i in range(len(user_str)):
	# 	print(int_funct(user_str[i]), end=' ')
