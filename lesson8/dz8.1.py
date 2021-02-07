if __name__ == '__main__':
    class Data:

        date = None

        def __init__(self, date=None):
            Data.date = date

        @classmethod
        def parse_date(cls, date=None):
            if date is not None:
                date_list_cm = date.split('-')
            elif cls.date is not None:
                date_list_cm = cls.date.split('-')
            return f'Число: {int(date_list_cm[0])}, месяц: {int(date_list_cm[1])}, год: {int(date_list_cm[2])}'

        @staticmethod
        def valid_date(date):
            msg = ''
            date_list = date.split('-')
            if 1900 <= int(date_list[2]) <= 2021:
                msg += 'Год введен корректно\n'
                if 1 <= int(date_list[1]) <= 12:
                    msg += 'Месяц введен корректно\n'
                    if (1 <= int(date_list[0]) <= 31 and int(date_list[1]) != 2 and
                            ((int(date_list[1]) < 8 and int(date_list[1]) % 2 != 0) or
                             (int(date_list[1]) >= 8 and int(date_list[1]) % 2 == 0))):
                        msg += 'Число введено корректно'
                    elif (1 <= int(date_list[0]) <= 30 and int(date_list[1]) != 2 and
                            ((int(date_list[1]) < 8 and int(date_list[1]) % 2 == 0) or
                             (int(date_list[1]) >= 8 and int(date_list[1]) % 2 != 0))):
                        msg += 'Число введено корректно'
                    elif (1 <= int(date_list[0]) <= 29 and int(date_list[1]) == 2 and
                          (int(date_list[2]) % 4 == 0 and int(date_list[2]) % 100 != 0
                           or int(date_list[2]) % 400 == 0)):
                        msg += 'Число введено корректно'
                    elif (1 <= int(date_list[0]) <= 28 and int(date_list[1]) == 2 and
                            int(date_list[2]) % 4 != 0 and int(date_list[2]) % 100 == 0):
                        msg += 'Число введено корректно'
                    else:
                        msg += 'Число введено не верно'
                else:
                    msg += 'Месяц введен неверно\n'
            else:
                msg += 'Год введен не верно. Введите год от 1900 до 2021\n'

            return msg


    print(Data.parse_date('07-02-2021'))
    date1 = Data('28-02-2020')
    print(date1.parse_date())
    date2 = Data()
    print(date2.parse_date('01-01-1990'))

    print(Data.valid_date('01-01-1995'))
    print(Data.valid_date('29-02-2021'))
    print(Data.valid_date('29-02-2020'))
    print(Data.valid_date('31-04-2020'))
    
