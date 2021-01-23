if __name__ == '__main__':
    def funct_sum(num_list, num_sum=0):
        """Возвращает сумму чисел в списке и посчитанных ранее

        num_list -- список чисел, которые необходимо просуммировать
        num_sum -- сумма чисел, посчитанная ранее
        """
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        print('Сумма введенных чисел:', num_sum + sum(num_list))
        return num_sum + sum(num_list)


    sum_number = 0
    while True:
        user_answer = input('Введите последовательность чисел, разделенных пробелом (для завершения'
                            ' работы введите "/"): ').split()
        if '/' in user_answer:
            user_answer.remove('/')
            sum_number = funct_sum(user_answer, sum_number)
            break
        else:
            sum_number = funct_sum(user_answer, sum_number)
