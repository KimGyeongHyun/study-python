# 주식 리스트 중 한 번 사고 한 번 팔 때 최대 이익 리턴

def max_profit(stock_list):
    biggest_profit = stock_list[1] - stock_list[0]
    min_value = stock_list[0]

    for i in range(1, len(stock_list)):

        biggest_profit = max(biggest_profit, stock_list[i]-min_value)
        min_value = min(min_value, stock_list[i])

    return biggest_profit


# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))