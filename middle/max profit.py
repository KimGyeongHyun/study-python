def max_profit(price_list, count):
    # 코드를 작성하세요.
    profit_dic = {}

    if count in profit_dic.keys():
        return profit_dic[count]

    if count == 1:
        profit_dic[1] = price_list[0]
        return profit_dic[1]

    if count == 2:
        profit_dic[2] = max(2 * max_profit(price_list, 1), price_list[1])
        return profit_dic[2]

    profit_dic[count] = max(max_profit(price_list, count-1) + max_profit(price_list, count-2), price_list[count-1])
    return profit_dic[count]

    # if count == 3:
    #     profit_dic[3] = max(max_profit(price_list, 2) + max_profit(price_list, 1), price_list[2])
    #     return profit_dic[3]

# 테스트
print(max_profit([100, 400, 800, 900, 1000], 5))
