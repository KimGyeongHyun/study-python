def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0
    left_list = [0]     # 왼쪽 제일 큰 빌딩 높이
    right_list = [0]    # 오른쪽 제일 큰 빌딩 높이

    for i in range(1, len(buildings)-1):

        if left_list[i-1] <= buildings[i-1]:
            left_list.append(buildings[i-1])
        else:
            left_list.append(left_list[i-1])

        rev_i = len(buildings)-1-i
        if right_list[i-1] <= buildings[rev_i+1]:
            right_list.append(buildings[rev_i+1])
        else:
            right_list.append(right_list[i-1])

    # ([0, 3, 3, 3, 3], [0, 4, 4, 4, 4])
    # ([0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3], [0, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3])

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(left_list[i], right_list[-i])

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
