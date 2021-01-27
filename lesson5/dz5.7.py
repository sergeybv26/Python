if __name__ == '__main__':

    import json

    firm_dict = {}
    firm_list = []
    profit_dict = {'average_profit': None}
    count_firm = 0
    profit_sum = 0

    with open('file_5_7.txt', encoding='utf-8') as f_obj:

        while True:
            f_str = f_obj.readline().split()

            if not f_str:
                break

            profit = int(f_str[2]) - int(f_str[3])
            firm_dict.update({f_str[0]: profit})

            if profit > 0:
                count_firm += 1
                profit_sum += profit

    profit_dict['average_profit'] = profit_sum / count_firm

    firm_list.append(firm_dict)
    firm_list.append(profit_dict)

    with open('file_5_7.json', 'w') as f_obj:
        json.dump(firm_list, f_obj)
