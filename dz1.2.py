if __name__ == '__main__':

    time = int(input('Введите время в секундах: '))
    minute = time // 60
    sec = time - minute * 60
    hour = minute // 60
    minute = minute - hour * 60
    print('Вы ввели время: %(hour)02d:%(minute)02d:%(sec)02d' % {'hour':hour, 'minute':minute, 'sec':sec})