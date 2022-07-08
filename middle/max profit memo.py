def max_profit_memo(price_list, count, cache):

    if count in cache:
        return cache[count]

    if count == 0:
        return price_list[0]

    if count == 1:
        return price_list[1]

    temp_value = 0
    for i in range(1, count//2 + 1):
        temp_value = max(max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count-i, cache),
                         temp_value)

    if count <= len(price_list)-1:
        temp_value = max(price_list[count], temp_value)

    cache[count] = temp_value
    return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
