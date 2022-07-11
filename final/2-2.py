# 2-1 함수 기능과 동일
# Big-O -> O(n) 이 되도록 풀기

def sublist_max(profits):

    biggest_sum = 0         # 리스트 붙어있는 수의 총합 중 최대 값
    minus_sum_value = 0     # 붙어있는 음수의 총합
    plus_sum_value = 0      # 붙어있는 양수의 총합

    for i in range(len(profits)):

        # 이전 값이 양수, 현재 값이 음수일 경우
        # 다음 3가지 경우를 비교, 제일 큰 수를 채택
        # 1. 이전 총합의 최대 값
        # 2. 이전 총합의 최대 값에서 i-1 인덱스까지 더한 값 (현재 값이 음수이므로 i 값은 재외)
        # 3. 이전 총합의 최대 값 이후, 붙어있는 양수의 총합
        if i > 0 and profits[i-1] > 0 and profits[i] < 0:                   # 양수 -> 음수일 경우
            biggest_sum = max(biggest_sum,                                  # 1
                              biggest_sum+plus_sum_value-minus_sum_value,   # 2
                              plus_sum_value)                               # 3 중 채택
            plus_sum_value, minus_sum_value = 0, 0                          # 총합 초기화

        # 양수, 음수의 경우를 나눠 각 총합에 더함
        if profits[i] > 0:
            plus_sum_value += profits[i]
        else:
            minus_sum_value -= profits[i]

        if i == len(profits)-1:                 # 마지막이라면
            return biggest_sum+plus_sum_value   # 지금까지 나온 최대값에 플러스 값만큼 더해서 리턴


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
