if __name__ == '__main__':
    import re

    my_dict = {}
    lesson_sum = 0

    with open('file_5_6.txt', encoding='utf-8') as f_obj:
        while True:
            f_str = f_obj.readline().split(':')

            if f_str == ['']:
                break

            subject = f_str[0]

            num = re.findall(r'\d+', f_str[1])

            for el in num:
                lesson_sum += int(el)

            my_dict.update({subject: lesson_sum})
            lesson_sum = 0

    print(my_dict)
