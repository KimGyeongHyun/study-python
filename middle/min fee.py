def min_fee(pages_to_print):
    # 코드를 작성하세요.
    pages_to_print.sort()
    time_sum = 0
    for time_index in range(len(pages_to_print)):
        time_sum += pages_to_print[time_index] * (len(pages_to_print) - time_index)

    return time_sum

# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
