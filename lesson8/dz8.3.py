if __name__ == '__main__':
    class OwnError(ValueError):
        pass

    num_list = []
    while True:
        try:
            user_input = input('Введите число (для прекращения ввода введите "stop"): ')
            if user_input.lower() == 'stop':
                break
            if not user_input.isdigit():
                raise OwnError(user_input)
            num_list.append(int(user_input))
        except OwnError as err:
            print(f'"{err}" не является числом! Введите число!')
    print(*num_list)
