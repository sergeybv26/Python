if __name__ == '__main__':
    def user_data(name, city, phone_number, surname='Аноним', year=1900, email='Не указан'):
        """Возвращает данные о пользователе в одной строке"""
        return f'{name} {surname}, родился в {year} году, проживает в городе {city}.' \
               f' Контактные данные: адрес электронной почты - {email},' \
               f' номер телефона - {phone_number}'


    print(user_data(name='Василий', surname='Пупкин', year=1980, city='Челябинск', email='aaa@mail.ru',
                    phone_number='8(800) 999-99-99'))
