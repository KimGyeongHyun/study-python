# Brute Force 로 붙어있는 숫자 간 총합이 제일 큰 수를 리턴

def sublist_max(profits):

    biggest_sum = profits[0]

    for i in range(len(profits)):
        for j in range(i, len(profits)):
            temp_sum = 0
            for k in range(i, j+1):
                temp_sum += profits[k]
            if biggest_sum < temp_sum:
                biggest_sum = temp_sum
            # print('i : {}, j : {}, sum : {}'.format(i, j,temp_sum))

    return biggest_sum


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))