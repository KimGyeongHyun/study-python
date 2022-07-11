# Divide and Conquer 로 list 안 붙어있는 숫자 합 제일 큰 것 리턴

def sublist_max(profits, start, end):

    if start == end:            # 길이가 0이라면
        return profits[start]   # 그 값을 리턴한다

    # 중앙 index 를 관통하는 총합의 제일 큰 수를 구한다
    mid = (start + end) // 2        # 중앙 index
    biggest_sum = profits[start]    # 중앙 index 를 관통하는 총합의 제일 큰 수 초기화
    for i in range(start, mid+1):               # 왼쪽 index
        left_sum, left_right_sum = 0, 0             # 왼쪽 ~ 중앙 총합, 왼쪽 ~ 오른쪽 총합
        for l in range(i, mid+1):               # 왼쪽 부분 총합 먼저 처리
            left_sum += profits[l]                  # 왼쪽 ~ 중앙 총합 구함
            left_right_sum = left_sum               # 해당 값으로 왼쪽 ~ 오른쪽 총합 변수 초기화
        for j in range(mid+1, end+1):           # 오른쪽 index

            left_right_sum += profits[j]                        # 왼쪽 ~ 중앙 총합 에서 오른쪽 값을 하나씩 더함
            biggest_sum = max(biggest_sum, left_right_sum)      # 더한 값이 더 크다면 해당 값으로 갱신

    # 왼쪽 최댓값, 오른쪽 최댓값, 중앙을 관통하는 최댓값 중 제일 큰 수를 리턴
    return max(sublist_max(profits, start, mid),
               sublist_max(profits, mid+1, end),
               biggest_sum)


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))